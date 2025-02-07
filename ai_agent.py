# Step 1:Setup api keys for Groq and Tavily
import os 
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAV_API_KEY')
GEM_API_KEY = os.getenv('GEM_API_KEY')


# Step 2:Setup  LLm and tools
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI 
from langchain_community.tools.tavily_search import TavilySearchResults

gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",api_key=GEM_API_KEY)
groq_llm = ChatGroq(model='llama-3.3-70b-versatile')
# deepseek_llm = ChatOpenAI(
#         base_url="http://127.0.0.1:1234/v1",  # Ensure this matches LM Studio API settings
#         model="deepseek-r1-distill-qwen-1.5b",
#         api_key="lm-studio",
#         temperature=0.5
#     )
search_tool = TavilySearchResults(max_results=4, api_key=TAVILY_API_KEY)


# Step 3:Setup AI agent with search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = 'Act as an AI Chatbot who is smart and friendly'

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=='Groq':
        llm=ChatGroq(model=llm_id)
    elif provider=='Gemini':
        llm=ChatGoogleGenerativeAI(model=llm_id)
    # elif provider=='LMStudio':
    #     llm=ChatOpenAI(model=llm_id)
    agent = create_react_agent(
        model=llm,
        tools=[search_tool],
        state_modifier=system_prompt
    )
    tools = [TavilySearchResults(max_results=2, api_key=TAVILY_API_KEY)] if allow_search else [] 
    
    state = {"messages":query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]
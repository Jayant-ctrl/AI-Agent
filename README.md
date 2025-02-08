# 🚀 AI Agent Project

This project is an AI-powered chatbot agent that allows users to interact with different large language models (LLMs) such as LLaMA 3, DeepSeek, Mixtral, and Whisper. It uses FastAPI for the backend and Streamlit for the frontend.

---

## 📌 Features

- Select from multiple LLM models (LLaMA 3, DeepSeek, Mixtral, Whisper)
- Define a custom system prompt for the agent
- Choose between Groq or Gemini API providers
- Optional web search functionality powered by Tavily
- Interactive UI built with Streamlit
- FastAPI-powered backend for seamless interaction

---

## 🛠 Tech Stack

### **Frontend:**
- Streamlit (UI)

### **Backend:**
- FastAPI (API Framework)
- Uvicorn (ASGI Server)
- Pydantic (Schema Validation)
- LangChain (LLM Integration)
- LangGraph (Agentic Framework)
- Tavily (Web Search API)

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
 git clone https://github.com/your-username/ai-agent.git
 cd ai-agent
```

### **2️⃣ Set Up Virtual Environment (Recommended)**
```sh
 python -m venv venv
 source venv/bin/activate  # macOS/Linux
 venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```sh
 pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the `backend/` folder and add:
```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GEM_API_KEY=your_gemini_api_key
```

You can find an example `.env.example` file in the repository.

---

## 🚀 Running the Project

### **Run Backend (FastAPI)**
```sh
 cd backend
 uvicorn backend:app --host 127.0.0.1 --port 9999
```
The FastAPI docs can be accessed at: [http://127.0.0.1:9999/docs](http://127.0.0.1:9999/docs)

### **Run Frontend (Streamlit UI)**
```sh
 cd frontend
 streamlit run frontend.py
```

Now, open [http://localhost:8501](http://localhost:8501) in your browser to access the UI.

---

## 📡 API Endpoints

### **POST /chat**
- **Description:** Interacts with the AI agent and returns a response.
- **Request Body:**
```json
{
  "model_name": "llama3-70b-8192",
  "model_provider": "Groq",
  "system_prompt": "Act as a smart AI chatbot",
  "messages": ["Hello, what can you do?"],
  "allow_search": true
}
```
- **Response:**
```json
{
  "response": "Hello! I am your AI agent. How can I assist you today?"
}
```

---

## 📜 Folder Structure
```bash
ai-agent/
│── backend/
│   │── ai_agent.py        # Core AI agent logic
│   │── backend.py         # FastAPI backend
│── frontend/
│   │── frontend.py        # Streamlit UI
│── .env.example           # Environment variable example
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── .gitignore             # Ignored files
│── LICENSE                # License
│── run.sh                 # Script to start backend and frontend
```

---

## 🎥 Demo Video
![Watch the demo](demo.mp4)

---

## 🏆 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License.

---

## 🎯 Future Improvements
- Add authentication for API access
- Deploy using Docker
- Improve UI with advanced visualizations
- Implement additional AI providers

---

## ⭐ Acknowledgments
Thanks to the creators of FastAPI, Streamlit, and LangChain for their amazing tools!

🚀 **Feel free to star this repo and contribute!** 🎯


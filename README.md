# LangChain Gemma Assistant

A minimal Streamlit web application powered by LangChain and Ollama, running Google's `gemma:2b` model locally with integrated LangSmith tracking.

## Features

- **Local LLM Execution**: Runs `gemma:2b` locally using Ollama—no paid API keys required for model inference.
- **LangChain Integration**: Utilizes LCEL (`ChatPromptTemplate | Ollama | StrOutputParser`) for pipeline execution.
- **LangSmith Tracing**: Observability and monitoring enabled via `.env` configuration.
- **Streamlit UI**: Clean and straightforward web interface for interactive Q&A.

## Prerequisites

1. **Ollama Installed & Running**
   Download and install [Ollama](https://ollama.ai/), then pull the Gemma model:
   ```bash
   ollama pull gemma:2b
   ```

2. **Python 3.9+**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/devendra-kashyap9/langchain-gemma-assistant.git
   cd langchain-gemma-assistant
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**:
   Create a `.env` file in the root directory:
   ```env
   LANGCHAIN_API_KEY=your_langsmith_api_key_here
   LANGCHAIN_PROJECT=langchain-gemma-demo
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to interact with the assistant.

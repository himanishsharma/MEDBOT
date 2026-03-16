# 🩺 Medical Report Chatbot
![Screenshot](Screenshot%202025-07-24%20at%2010.01.24%20PM.png)


An **AI-powered chatbot** that can read medical PDF reports and answer questions based on their content.  
Built using **Streamlit**, **ChromaDB**, **SentenceTransformers**, and **LLaMA 3** running locally via **Ollama**.

> "AI that reads your reports and answers like a medical assistant."
---

## 🧠 How It Works

1. 📄 **Upload** a medical report PDF.
2. 🧾 **Text is extracted** from the PDF.
3. 🔍 **Text is chunked and embedded** using `all-MiniLM-L6-v2`.
4. 🧠 **Query is embedded** and relevant chunks are retrieved from `ChromaDB`.
5. 🤖 **LLaMA 3 via Ollama** generates the final answer based on the context and your question.

---

```
pip install -r requirements.txt
```
### LLAMA
1. install ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```
2. pull 
```
ollama pull llama3
```
3. Run
```
ollama run llama3
```

- Make sure it's accessible at http://localhost:11434

```
streamlit run app.py
```

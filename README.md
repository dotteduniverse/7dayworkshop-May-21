<!--
Colorful README for AI Solution Architect Workshop
Icons from: https://github.com/ikatyang/emoji-cheat-sheet
Badges from: https://shields.io/
-->

<div align="center">

# 🧠 AI Solution Architect Workshop

### *From Data Foundations to Production-GenAI & Agentic Systems*

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-2.0+-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C.svg?logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-000000.svg?logo=pinecone)](https://www.pinecone.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Your 7‑day guided journey to rebuild your AI engineering stack from scratch**  
*Based on real-world experience (Standard Chartered, Uber, Genpact)*

[📅 Workshop Tracker](#-7-day-workshop-tracker--with-resources) • [🚀 Quick Start](#-quick-start--day-0) • [📁 Repo Structure](#-repository-structure) • [📊 Progress Log](#-your-progress-log)

</div>

---

## 📌 Overview

This repository contains the complete **hands‑on workshop** for an AI Solution Architect. Over seven days you will:

- ✅ Relearn **Python + Pandas** for data acquisition & wrangling  
- ✅ Build a **RAG pipeline** (loading → chunking → embeddings → vector search)  
- ✅ Optimise retrieval with **hybrid search & re‑ranking**  
- ✅ Create **Agentic AI** with tools and Model Context Protocols (MCP)  
- ✅ Productionalise with **security, real‑time pipelines & governance (GDPR/SOC2)**  
- ✅ Plan & blueprint a **Financial Document Q&A Agent** (like the StanChart POC)  

Your final deliverable: a **rebuilt GitHub repository** with well‑commented notebooks, an architecture design doc, and a roadmap for further learning.

> 💡 **Memory aid**: All commands, code snippets, and decisions are documented inside the `/notebooks` folder. Use it as your personal reference.

---

## 🚀 Quick Start (Day 0)

Before diving into daily activities, set up your environment:

```bash
# 1. Clone this repo
git clone https://github.com/dotteduniverse/ai-solution-architect-workshop.git
cd ai-solution-architect-workshop

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
# or
venv\Scripts\activate          # Windows

# 3. Install required packages
pip install -r requirements.txt

# 4. Create .env file with your API keys (Pinecone, OpenAI, Cohere, etc.)
echo "PINECONE_API_KEY=your_key_here" > .env
echo "OPENAI_API_KEY=your_key_here" >> .env
## 📁 Repository Structure
ai-solution-architect-workshop/
│
├── notebooks/                     # Daily Jupyter notebooks
│   ├── day1_pandas_foundation.ipynb
│   ├── day2_data_acquisition.ipynb
│   ├── day3_rag_ingestion.ipynb
│   ├── day4_rag_optimization.ipynb
│   ├── day5_agentic_ai.ipynb
│   ├── day6_production_governance.ipynb
│   └── day7_capstone_blueprint.ipynb
│
├── data/                          # Sample datasets (downloaded during workshop)
│   └── sample_financial_docs/
│
├── docs/                          # Architecture designs & governance artefacts
│   ├── financial_qa_agent_design.md
│   ├── roadmap.md
│   └── gdpr_audit_report.md
│
├── src/                           # Reusable Python modules (e.g., MCP server)
│   └── mcp_time_server.py
│
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment variables
├── .gitignore
└── README.md                      # <-- You are here

🗓️ 7 Day Workshop Tracker (with Resources)
Use the table below each day. After finishing, write your Real Outcome (e.g., what worked, what was hard, what you learned).
Day	Todo	Objective	Real Outcome (fill after completion)	Resources / Links
Prep (Day 0)	1. Create Python virtual environment.
2. Install libraries (see requirements.txt).
3. Sign up for Pinecone & get API key.
4. Store keys in .env.	Have a fully functional reproducible environment.		Python venv docs • Pinecone signup • python-dotenv guide

Day 1	Morning:
pandas Series & DataFrame.
pd.read_csv() & .head(), .info(), .describe().
Afternoon:
loc, iloc, boolean filtering.
.rename(), .sort_values(), .fillna(), .groupby().mean().	Build strong pandas fundamentals for data wrangling.		📘 Dataquest Pandas Cheat Sheet • 📙 Official Pandas PDF • 📺 Exploring Data with pandas

Day 2	Morning:
pd.read_html() from Wikipedia.
API call with requests → JSON → DataFrame.
Afternoon:
Scrape books.toscrape.com with BeautifulSoup.
Clean scraped data into DataFrame.	Acquire data from web sources (HTML tables, APIs, scraping).		🕸️ BeautifulSoup Complete Guide (Kanaries) • 🧼 Detailed BeautifulSoup tutorial • 🎥 Comprehensive Video tutorial

Day 3	Morning:
Load PDF/text with LangChain document loaders.
Split into overlapping chunks (RecursiveCharacterTextSplitter).
Afternoon:
Generate embeddings (HuggingFace/OpenAI).
Store in Pinecone via LangChain.
Run similarity search.	Build the core RAG ingestion pipeline.		📄 PyPDFLoader full tutorial (GitCode) • ✂️ RecursiveCharacterTextSplitter guide • 🧠 HuggingFace sentence-transformers • 🔍 Official Pinecone + LangChain docs

Day 4	Morning:
Implement hybrid search (vector + keyword).
Add re-ranking (Cohere).
Afternoon:
Evaluate RAG (faithfulness & answer relevance).
Experiment with different prompts.	Optimise retrieval quality and measure RAG performance.		🔎 LangChain Pinecone Sparse Vector • 🏷️ Production Reranker Layer (Dev.to) • 📊 RAG Triad metrics (DeepEval) • 📈 RAG evaluation metrics (Atlan)

Day 5	Morning:
Read agent design patterns (Hugging Face).
Build simple LangChain ReAct agent (calculator tool).
Afternoon:
Create basic MCP server (get current time).
Integrate Day 3 vector DB as agent tool.	Understand agentic AI – reasoning, tools, and Model Context Protocols.		🤖 LangChain 1.0 ReAct guide • 🦜 LangGraph ReAct template • 🔌 Official MCP docs • 🛠️ MCP GitHub & SDKs • 🧰 VectorStore as tool (LangChain)

Day 6	Morning:
Study real time embedding pipeline (Google blog).
Learn prompt injection prevention.
Afternoon:
Design data lineage diagram (OpenLineage).
Write mock GDPR audit report for RAG pipeline.	Productionize AI systems with security, real time performance, and governance.		⚡ Google Dataflow + EmbeddingGemma • 🛡️ PromptGuard framework (Nature 2026) • 🧪 Awesome Prompt Injection Defense (GitHub) • 📜 OpenLineage guide • ⚖️ GDPR for AI – 12 point checklist

Day 7	Morning:
Create GitHub repo & write README.md blueprint.
Organise notebooks into /notebooks.
Afternoon:
Write architecture design doc for “Financial Document Q&A Agent”.
Add ROADMAP.md for next 4–6 weeks.	Rebuild your professional GitHub repository and plan a real world GenAI project.		🏗️ LangChain RAG template reference • 🤝 AI PDF chatbot example • 📚 Complete RAG pipeline example

________________________________________


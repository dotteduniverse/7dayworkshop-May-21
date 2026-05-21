# 4–6 Week Learning Roadmap (Post‑Workshop)

Now that you have completed the 7‑day workshop, this roadmap will solidify and extend your skills toward a **senior AI Solution Architect** level.

## Week 1–2: Deepen RAG & Evaluation

- [ ] **Implement advanced chunking** – experiment with semantic chunking (LangChain `SemanticChunker`) vs fixed size.
- [ ] **Build a RAG evaluation pipeline** using `RAGAS` or `DeepEval` on a custom finance dataset.
- [ ] **Try alternative vector DB** – Qdrant (self‑hosted) or Milvus (for scale).
- [ ] **Add reranking** with a cross‑encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`).

## Week 2–3: Agentic AI & MCP in Production

- [ ] **Build a multi‑tool agent** – combine: vector DB lookup + SQL database query + web search.
- [ ] **Implement proper MCP server** (Node.js or Python SDK) that exposes real banking APIs (simulated).
- [ ] **Add human‑in‑the‑loop** – for critical actions (e.g., fund transfer).
- [ ] **Deploy agent as a microservice** using FastAPI + Docker.

## Week 3–4: Production & Governance

- [ ] **Set up real‑time embedding pipeline** using Kafka + Spark Structured Streaming (inspired by Uber’s feature store).
- [ ] **Instrument data lineage** with OpenLineage + Marquez.
- [ ] **Create automated data quality checks** (Great Expectations) for ingestion.
- [ ] **Write a full BCBS 239 compliance report** for your assistant.

## Week 4–5: Cloud & DevOps

- [ ] **Deploy RAG pipeline on AWS** – using SageMaker for embeddings, OpenSearch Serverless (vector), Lambda for orchestration.
- [ ] **Or Azure alternative** – AI Search + OpenAI + Functions.
- [ ] **Infrastructure as Code** – Terraform scripts for the whole stack.
- [ ] **CI/CD pipeline** – GitHub Actions to test & deploy on commit.

## Week 5–6: Capstone Project – Financial Multi‑Agent System

Build a system that:
- Accepts a user query like *“Compare our Q2 risk exposure to last year and draft an email to the CRO.”*
- Orchestrates:
  - Agent 1: RAG over compliance documents
  - Agent 2: SQL query on internal risk DB (synthetic)
  - Agent 3: Write email draft
- Logs all interactions for audit.
- Deploy on cloud with monitoring (Prometheus + Grafana).

## Recommended Resources

- **Book**: *Designing Data‑Intensive Applications* – Martin Kleppmann (for governance & scaling)
- **Courses**: DeepLearning.AI – “Building Systems with the ChatGPT API”
- **YouTube**: “RAG from Scratch” (LangChain official)
- **Practice data**: [SEC EDGAR](https://www.sec.gov/edgar) financial filings

## Weekly review template

Every Sunday, answer:
1. What did I build that works?
2. What broke / what was confusing?
3. What will I change next week?
# Financial Document Q&A Agent – Architecture Design

## 1. Overview

This document describes the architecture for a **Generative AI‑powered Knowledge Assistant** tailored to financial regulatory documents. The system enables compliance officers and analysts to query thousands of PDFs, policy documents, and reports using natural language, receiving accurate, referenced answers.

This design is based on the **Standard Chartered Regulatory Knowledge Assistant POC** (70% reduction in compliance research time).

## 2. System Architecture Diagram
┌─────────────────────────────────────────────────────────────────────┐
│ User Interface │
│ (Web UI / Slack Bot / API) │
└─────────────────────────────────┬───────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────┐
│ Orchestration Layer │
│ (FastAPI + LangChain Agent) │
│ - Query routing → RAG or direct tool call │
│ - Prompt templating + guardrails │
└─────────────────────────────────┬───────────────────────────────────┘
│
┌───────────────────┼───────────────────┐
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Retrieval │ │ Vector DB │ │ LLM Gateway │
│ Pipeline │◄──┤ (Pinecone) │ │ (Azure OpenAI) │
│ (Embeddings) │ │ - Hybrid │ │ GPT-4 / 4-turbo│
└─────────────────┘ │ search │ └─────────────────┘
└─────────────────┘
▲
│
┌─────────────────────────────────────────────────────────────────────┐
│ Ingestion Pipeline │
│ (Event‑driven – Azure Data Factory + Kafka) │
│ PDF → Load → Chunk → Embed → Store in Pinecone + Metadata in PG │
└─────────────────────────────────────────────────────────────────────┘

## 3. Component Breakdown

| Component                | Technology Choice                     | Justification                                                                 |
|-------------------------|---------------------------------------|-------------------------------------------------------------------------------|
| **Document Loading**     | LangChain `PyPDFLoader` + `DirectoryLoader` | Handles diverse financial PDFs (scanned + text).                              |
| **Chunking Strategy**    | `RecursiveCharacterTextSplitter` (chunk size: 512, overlap: 64) | Preserves semantic boundaries; overlap ensures context continuity.            |
| **Embeddings**           | `OpenAI text-embedding-3-small` or `Cohere embed-english-v3.0` | High retrieval accuracy for financial jargon.                                 |
| **Vector Database**      | Pinecone (pod-based)                  | Low latency, hybrid search support, SOC2 compliant.                           |
| **Orchestration**        | LangChain + FastAPI                   | Production‑ready, easy integration with tools and agents.                     |
| **LLM**                  | Azure OpenAI GPT-4 (temperature=0.2)  | Deterministic answers, data residency, compliance.                            |
| **Caching**              | Redis                                 | Cache frequent queries to reduce cost & latency.                              |
| **Governance & Logging** | OpenLineage + Great Expectations      | Data lineage, quality checks, audit trail for every Q&A.                      |

## 4. Data Flow (Query Time)

1. User asks: *“What is the capital adequacy requirement under Basel III?”*
2. Orchestrator rewrites query (if needed) and calls vector DB.
3. Pinecone returns top‑5 relevant chunks (hybrid search: 0.7 vector + 0.3 keyword).
4. Re‑ranker (Cohere) reorders chunks by relevance.
5. Prompt injection guardrails check for malicious input.
6. LLM receives: *Context: [chunks] + Question: ...*
7. LLM generates answer with citations (source document + page number).
8. Answer + metadata logged to audit database (PostgreSQL).

## 5. Compliance & Governance

- **GDPR / Right to be forgotten**: Pinecone supports namespace deletion; mapping between user PII and vector IDs stored in encrypted PostgreSQL.
- **SOC2 / BCBS239**: All Q&A pairs logged immutably; access restricted via Azure AD.
- **Data retention**: Vectors older than 7 years are archived to cold storage (Azure Blob).
- **Prompt injection prevention**: Input sanitisation + `PromptGuard` model before LLM call.

## 6. Evaluation Metrics

| Metric           | Target | Tool                     |
|-----------------|--------|--------------------------|
| Faithfulness     | >0.85  | DeepEval / RAGAS         |
| Answer Relevance | >0.90  | DeepEval / RAGAS         |
| Context Recall   | >0.80  | RAGAS                    |
| Latency (p95)    | <2 sec | Custom instrumentation   |

## 7. Future Enhancements

- **Agentic capabilities**: Allow agent to call internal banking APIs (balance, transaction history) using Model Context Protocol (MCP).
- **Multimodal support**: Extract tables and charts from PDFs using GPT‑4V.
- **Continuous learning**: Fine‑tune embedding model on internal finance corpus every quarter.
# Mock GDPR Audit Report – RAG Knowledge Assistant

**Audit Date:** 2026‑05‑21  
**System Audited:** Financial Document Q&A Agent (RAG pipeline + Pinecone vector store)  
**Auditor:** Internal Data Protection Team  

## 1. Scope

This audit assesses compliance of the AI assistant with the **General Data Protection Regulation (GDPR)**, focusing on:
- Article 5 – Data minimisation & purpose limitation
- Article 17 – Right to erasure (“right to be forgotten”)
- Article 25 – Data protection by design and by default
- Article 32 – Security of processing
- Article 35 – Data Protection Impact Assessment (DPIA)

## 2. Findings

| GDPR Article | Requirement                          | Status | Evidence / Remediation Plan                    |
|--------------|--------------------------------------|--------|------------------------------------------------|
| Art. 5(1)(c) | Data minimisation                    | ✅ Pass | No PII stored in vector embeddings; only chunked financial text. |
| Art. 17       | Right to erasure                     | ⚠️ Partial | Pinecone namespace deletion implemented, but no automated user PII mapping. **Action:** Add mapping table (user_id → vector IDs) in encrypted PostgreSQL. |
| Art. 25       | Privacy by design                    | ✅ Pass | Embeddings generated without raw PII; all logs anonymised within 30 days. |
| Art. 32       | Security                             | ✅ Pass | Data encrypted at rest (AES‑256) and in transit (TLS 1.3). Access via Azure AD with MFA. |
| Art. 35       | DPIA                                 | ✅ Pass | DPIA conducted (attached separately). No high residual risk. |

## 3. Data Flow & Lineage

```mermaid
graph LR
    A[Source: Financial PDFs] --> B[Chunking]
    B --> C[Embedding Model]
    C --> D[Pinecone Vector Store]
    D --> E[LLM Query]
    E --> F[User Answer]
    G[PostgreSQL Audit Log] --> E
    G --> H[Anonymised after 30d]
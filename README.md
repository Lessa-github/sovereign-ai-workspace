# 🧠 Sovereign AI Workspace & Intelligent Multi-Provider Gateway

[![Documentation](https://img.shields.io/badge/Docs-Docsify_Live-06b6d4?style=for-the-badge&logo=googledocs&logoColor=white)](https://lessa-github.github.io/sovereign-ai-workspace/)
[![Engine](https://img.shields.io/badge/Gateway-OmniRoute_AI-6366f1?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/Lessa-github/sovereign-ai-workspace)
[![Optimization](https://img.shields.io/badge/Tokens-Caveman_--60%25-10b981?style=for-the-badge)](https://lessa-github.github.io/sovereign-ai-workspace/)
[![Privacy](https://img.shields.io/badge/Search-SearXNG_Private-blue?style=for-the-badge)](https://lessa-github.github.io/gabriel-portfolio/)

Sovereign Artificial Intelligence workspace, multi-agent orchestration, and economic multi-provider gateway engineered for **strict data privacy and zero external telemetry**.

Operating inside dedicated Debian 12 LXC containers on Proxmox VE, the infrastructure eliminates rate-limiting bottlenecks via **automated multi-tier quota failover** and slashes context window consumption by **60% using syntactic prompt compression**.

---

## ⚡ Engineering Highlights

* **The 7 Master Combos Gateway:** OmniRoute (CT 114) continuously load-balances requests across perpetual free-tier providers (Google AI Studio, Groq LPU, Cloudflare Workers AI) with millisecond failover.
* **Caveman Syntactic Compression:** Algorithmic prompt minimization removing filler words and passive grammar while preserving 98.4%+ semantic accuracy.
* **Pre-Inference PII Masking:** Real-time regex inspection redacting API keys, passwords, IP addresses, and personal identification numbers before prompts leave the host.
* **Hermes Agent & Private Search:** Autonomous task execution in an unprivileged container connected to a zero-telemetry local **SearXNG** meta-search engine.

---

## 📐 Multi-Provider Gateway Architecture

```mermaid
flowchart TD
    subgraph INTERNAL_CLIENTS ["Internal AI Consumers"]
        Hermes["Hermes Autonomous Coding Agent (CT 115)"]
        BenchCLI["OmniRoute Benchmark CLI"]
    end

    subgraph GATEWAY ["OmniRoute AI Gateway (CT 114 / Port 20128)"]
        PII["1. Pre-Inference PII Masking Middleware"]
        Caveman["2. Caveman Prompt Compression Engine (-60% Tokens)"]
        Router["3. Intelligent Quota & Rate-Limit Router (Redis Cache)"]
    end

    subgraph PROVIDERS ["Multi-Provider Ecosystem (Automated Failover)"]
        Groq["Tier 1: Groq LPU (Ultra-Low Latency / Llama 3.3 70B)"]
        Google["Tier 2: Google AI Studio (Gemini 2.0 Flash)"]
        CF["Tier 3: Cloudflare Workers AI (Llama 3 / Mistral)"]
        Ollama["Tier 4: Ollama Local Fallback (100% Offline PVE Host)"]
    end

    INTERNAL_CLIENTS --> PII
    PII --> Caveman
    Caveman --> Router
    Router -->|Primary Ingestion| Groq
    Router -.->|Fallback on HTTP 429| Google
    Router -.->|Secondary Fallback| CF
    Router -.->|Offline Air-Gapped Fallback| Ollama
```

---

## 🛠️ Benchmark CLI: omniroute-bench.py

```text
Usage: omniroute-bench.py [OPTIONS]

Options:
  --test-payload <file>    Path to prompt benchmark file
  --algorithm <caveman>    Compression engine (caveman, llmlingua, none)
  --provider <name>        Target AI gateway provider endpoint
  --iterations <int>       Number of sequential benchmark runs (default: 5)
  --help                   Show benchmark parameters and exit
```

---

## 🌐 Live Technical Documentation

Explore the complete single-page interactive whitepaper with smooth section scrolling:

👉 **[https://lessa-github.github.io/sovereign-ai-workspace/](https://lessa-github.github.io/sovereign-ai-workspace/)**

# 🧠 Sovereign AI Workspace & Intelligent Multi-Provider Gateway

[![Documentation](https://img.shields.io/badge/Docs-Docsify_Live-06b6d4?style=for-the-badge&logo=googledocs&logoColor=white)](https://lessa-github.github.io/sovereign-ai-workspace/)
[![Engine](https://img.shields.io/badge/Gateway-OmniRoute_AI-6366f1?style=for-the-badge&logo=fastapi&logoColor=white)](https://github.com/Lessa-github/sovereign-ai-workspace)
[![Optimization](https://img.shields.io/badge/Tokens-Caveman_--60%25-10b981?style=for-the-badge)](https://lessa-github.github.io/sovereign-ai-workspace/)
[![Privacy](https://img.shields.io/badge/Search-SearXNG_Private-blue?style=for-the-badge)](https://lessa-github.github.io/gabriel-portfolio/)

Plataforma de infraestrutura de Inteligência Artificial soberana, orquestração de agentes autônomos e roteamento econômico multi-provedor com **privacidade total e zero telemetria externa**.

Projetado para operar em contêineres Debian 12 LXC dedicados no Proxmox VE, eliminando gargalos de cotas via failover automático para tiers perpétuos gratuitos e reduzindo o consumo de tokens de contexto em até **60% via algoritmos de compressão semântica**.

---

## ⚡ Destaques de Engenharia

* **Roteamento Inteligente em 7 Combos:** O gateway **OmniRoute (CT 114)** realiza failover contínuo e sem interrupções entre múltiplos provedores com cotas gratuitas perpétuas (Google AI Studio, Groq LPU, Cloudflare Workers AI) com governança de limites de RPM/RPD.
* **Compressão de Prompt Caveman:** Algoritmo que elimina stopwords e tokens redundantes, diminuindo o consumo de janela de contexto em 60% com perda semântica próxima de zero.
* **Middleware de PII Masking:** Sanitização pré-inferência que anonimiza senhas, chaves de API, CPFs e dados sensíveis antes de qualquer tráfego sair para APIs de IA.
* **Agente Autônomo Hermes (CT 115):** Ambiente de execução isolado equipado com suporte a ferramentas MCP e integrado a uma instância local do buscador **SearXNG** para pesquisa na internet sem rastreamento comercial.

---

## 📐 Arquitetura do Gateway Multi-Provider

```mermaid
flowchart TD
    subgraph CLIENTS ["Consumidores de IA Internos"]
        Hermes["Hermes Autonomous Agent (CT 115)"]
        CLI["OmniRoute Benchmark CLI"]
    end

    subgraph GATEWAY ["OmniRoute AI Gateway (CT 114 / Porta 20128)"]
        PII["1. Middleware de PII Masking (Sanitização)"]
        Caveman["2. Algoritmo de Compressão Caveman (-60% Tokens)"]
        Router["3. Intelligent Rate-Limit & Quota Router (Redis Cache)"]
    end

    subgraph PROVIDERS ["Nuvem Multi-Provider (Failover Automático)"]
        Groq["Groq LPU (Ultra-Low Latency / Llama 3.3)"]
        Google["Google AI Studio (Gemini 2.0 Flash)"]
        Cloudflare["Cloudflare Workers AI (Llama 3 / Mistral)"]
        LocalLLM["Ollama Local Fallback (100% Offline)"]
    end

    CLIENTS --> PII
    PII --> Caveman
    Caveman --> Router
    Router -->|Tier 1 Principal| Groq
    Router -.->|Failover se Quota Esgotada| Google
    Router -.->|Failover Secundário| Cloudflare
    Router -.->|Failover Offline Sem Internet| LocalLLM
```

---

## 🛠️ CLI Benchmark: `omniroute-bench.py`

O repositório inclui a ferramenta de teste e benchmarking de compressão de contexto:

```bash
$ python3 cli-tools/omniroute-bench.py --help
Usage: omniroute-bench.py [OPTIONS]

Options:
  --test-payload <file>    Path to prompt benchmark file
  --algorithm <caveman>    Compression engine (caveman, llmlingua, none)
  --provider <name>        Target AI gateway provider endpoint
  --iterations <int>       Number of sequential benchmark runs (default: 5)
  --help                   Show benchmark parameters and exit
```

---

## 🌐 Documentação Web Completa (Live Docsify)

👉 **[https://lessa-github.github.io/sovereign-ai-workspace/](https://lessa-github.github.io/sovereign-ai-workspace/)**

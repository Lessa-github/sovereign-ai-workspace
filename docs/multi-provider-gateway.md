# 🌐 Gateway Multi-Provider & Master Combos

O gateway **OmniRoute (CT 114)** atua como um proxy reverso inteligente compatível com a especificação da OpenAI API (`/v1/chat/completions`).

---

## 🔀 A Estratégia dos 7 Master Combos

Para garantir alta disponibilidade contínua sem depender de cartões de crédito ou faturamentos imprevistos, o gateway implementa roteamento em camadas:

```mermaid
flowchart TD
    Req["Requisição de Inferência do Cliente"] --> Auth["Autenticação Interna Bearer Token"]
    Auth --> Router["OmniRoute Routing Engine"]

    subgraph TIER1 ["Tier 1: Ultra-Rápido & Alta Cota"]
        Router -->|Prioridade 1| Groq["Groq LPU (Llama 3.3 70B Versatile)"]
    end

    subgraph TIER2 ["Tier 2: Janela de Contexto Longa"]
        Router -.->|Fallback se 429| Google["Google AI Studio (Gemini 2.0 Flash)"]
    end

    subgraph TIER3 ["Tier 3: Distribuição Global"]
        Router -.->|Fallback Secundário| CF["Cloudflare Workers AI (Mistral / Llama)"]
    end

    subgraph TIER4 ["Tier 4: Resiliência Máxima / Air-Gapped"]
        Router -.->|Fallback sem Internet| Ollama["Ollama Local Fallback (Host PVE)"]
    end
```

---

## ⚡ Governança de Rate Limits

O OmniRoute utiliza um cache Redis em memória para rastrear métricas em tempo real:
* **RPM (Requests Per Minute):** Contador com janela deslizante (*sliding window*).
* **RPD (Requests Per Day):** Bloqueio preventivo antes de atingir o limite estrito da API.
* **Failover Transparente:** Se a resposta retornar status de erro temporário (503 ou 429), a requisição é reenviada para o próximo membro do combo sem que o usuário final perceba.

# 🤖 Agente Autônomo Hermes & Busca SearXNG

O container **CT 115 (`ai-workspace`)** hospeda o ambiente de execução do **Hermes Agent**, operando sobre um contêiner Debian 12 com isolamento de privilégios.

---

## 🔍 Busca na Web Privada com SearXNG

Diferente de agentes que utilizam motores de busca comerciais que indexam as consultas e realizam telemetria sobre as intenções de busca do pesquisador, nosso agente consulta exclusivamente uma instância local do **SearXNG**:
* **Meta-search Agregador:** Consulta Google, DuckDuckGo, Bing, Wikipedia e GitHub simultaneamente.
* **Zero Logs:** A instância não armazena cookies, histórico nem endereços IP de origem.
* **Formato JSON Nativo:** Retorna respostas em formato estruturado pronto para consumo pelo modelo.

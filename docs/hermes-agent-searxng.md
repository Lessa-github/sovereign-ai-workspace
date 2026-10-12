# 🤖 Hermes Autonomous Agent & Private SearXNG Meta-Search

Container **CT 115 (`ai-workspace`)** hosts the runtime environment for the **Hermes Autonomous Agent**, operating within an unprivileged Debian 12 LXC environment with strict capability restrictions.

---

## 🔍 Zero-Telemetry Web Search via Self-Hosted SearXNG

Unlike commercial AI agents that query proprietary search engines which log search intentions, profile user queries, and inject tracker cookies, our autonomous agent routes all web research exclusively through a local instance of **SearXNG**:
* **Aggregated Meta-Search Engine:** Queries Google, DuckDuckGo, Bing, Wikipedia, and GitHub concurrently in the background.
* **Zero Logging Guarantee:** The engine retains zero cookies, search histories, or originating IP addresses.
* **Native JSON API Delivery:** Returns sanitized, structured markdown results directly into the agent's MCP tool context without scraping overhead.

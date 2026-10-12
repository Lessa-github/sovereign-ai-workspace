# 🛠️ omniroute-bench: CLI de Benchmarking

Utilitário de linha de comando para medir o impacto de algoritmos de compressão e tempos de resposta de provedores de IA.

---

## 💻 Interface de Linha de Comando (`--help`)

```text
Usage: omniroute-bench.py [OPTIONS]

Options:
  --test-payload <file>    Path to prompt benchmark file
  --algorithm <caveman>    Compression engine (caveman, llmlingua, none)
  --provider <name>        Target AI gateway provider endpoint
  --iterations <int>       Number of sequential benchmark runs (default: 5)
  --help                   Show benchmark parameters and exit
```

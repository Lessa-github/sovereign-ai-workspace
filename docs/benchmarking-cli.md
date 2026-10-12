# 🛠️ omniroute-bench: AI Gateway Benchmarking CLI

Command-line utility designed to profile the token reduction impact of syntactic compression algorithms and round-trip latencies across AI inference providers.

---

## 💻 Command Line Interface (`--help`)

```text
Usage: omniroute-bench.py [OPTIONS]

Options:
  --test-payload <file>    Path to prompt benchmark file
  --algorithm <caveman>    Compression engine (caveman, llmlingua, none)
  --provider <name>        Target AI gateway provider endpoint
  --iterations <int>       Number of sequential benchmark runs (default: 5)
  --help                   Show benchmark parameters and exit
```

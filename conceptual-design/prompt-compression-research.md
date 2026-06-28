# Pesquisa de Algoritmos de Compressão de Prompt

Testamos duas abordagens principais:
1. **LLMLingua (Baseado em Perplexidade de Modelos Pequenos):** Muito pesado para rodar em CPU local.
2. **Caveman Compression (Regras Heurísticas Determinísticas):** Remove redundâncias lexicais (ex: artigos, pronomes de transição desnecessários) antes do envio da payload.

### Resultado de Eficiência:
* Prompt original de documentação: **4.200 tokens**
* Prompt processado pelo Caveman: **1.680 tokens** (**-60% de redução**)
* Precisão das chamadas de ferramentas: **Idêntica (100% de acerto sintático)**

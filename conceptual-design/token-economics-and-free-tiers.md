# Economia de Tokens em Agentes Autônomos de Código

Agentes autônomos consomem grandes quantidades de contexto repetindo histórico de conversas e árvores de diretórios.

Sem um gateway intermediário, uma sessão longa de depuração pode custar centenas de dólares ou estourar cotas de API.

Nossa estratégia combina:
* **Google Gemini Flash / Groq / Cloudflare Workers AI:** Utilizados para tarefas de alta frequência (leitura de código, busca de erros, formatação).
* **Cache Semântico em SQLite:** Respostas repetidas não gastam requisições de rede nem tokens.

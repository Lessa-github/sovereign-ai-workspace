# 🔒 Middleware de PII Masking

O **PII Masking Middleware** atua na camada pré-inferência do OmniRoute Gateway, inspecionando cada mensagem recebida e substituindo dados pessoais e credenciais por identificadores sintéticos de documentação.

---

## 🛡️ Padrões Sanitizados

1. **Tokens e Chaves de API:** Chaves no padrão `ghp_*`, `sk-*`, `Bearer *` são substituídas por `${TOKEN_REDACTED}`.
2. **Endereços de IP Reais:** Endereços de sub-redes privadas ou públicas reais são convertidos para as faixas sintéticas autorizadas (`172.28.40.x`, `192.168.199.x`, `10.240.50.x`).
3. **Dados de Identificação Pessoal (PII):** CPF, números de cartão e e-mails pessoais são mascarados via regex de alta performance.

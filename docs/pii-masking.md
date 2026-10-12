# 🔒 Pre-Inference PII Masking & Secret Redaction Middleware

The **PII Masking Middleware** intercepts prompt payloads at the pre-inference layer of the OmniRoute Gateway, sanitizing sensitive strings and substituting real identities with synthetic documentation references.

---

## 🛡️ Sanitization Rules & Detection Patterns

1. **API Keys & Cryptographic Tokens:** Tokens matching patterns `ghp_*`, `sk-*`, `Bearer *`, or high-entropy hex strings are automatically replaced with `${TOKEN_REDACTED}`.
2. **Production Network Coordinates:** Real local or public IPv4/IPv6 addresses are dynamically translated to standardized synthetic documentation ranges (`172.28.40.x`, `192.168.199.x`, `10.240.50.x`).
3. **Personally Identifiable Information (PII):** National identification numbers, credit card sequences, and personal email addresses are sanitized via compiled high-performance regular expressions prior to outbound cloud dispatch.

# Algoritmo de Compressão Semântica Caveman para Redução de Tokens
import re

STOP_PHRASES = [
    r"\bpor favor\b", r"\bcomo você sabe\b", r"\bé importante notar que\b",
    r"\bno mundo de hoje\b", r"\bno que diz respeito a\b", r"\bcom certeza\b"
]

def compress_prompt(text: str) -> str:
    """Reduz tamanho de prompts longos removendo preenchimento vazio sem perder significado técnico."""
    compressed = text
    for pattern in STOP_PHRASES:
        compressed = re.sub(pattern, "", compressed, flags=re.IGNORECASE)
    
    # Normalização de espaços
    compressed = re.sub(r'\s+', ' ', compressed).strip()
    return compressed

if __name__ == "__main__":
    sample = "Por favor, é importante notar que no mundo de hoje o container Docker precisa de limites de memória."
    print("Original:", sample)
    print("Comprimido:", compress_prompt(sample))

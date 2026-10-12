# Caveman Syntactic Prompt Compression Engine for Token Optimization
import re

STOP_PHRASES = [
    r"\bplease note that\b", r"\bas you already know\b", r"\bit is important to mention that\b",
    r"\bin today's modern world\b", r"\bwith regards to the fact that\b", r"\bcertainly\b",
    r"\bkindly ensure that\b", r"\bas a matter of fact\b"
]

def compress_prompt(text: str) -> str:
    """Minimizes verbose token overhead by stripping filler phrases while preserving core technical semantics."""
    compressed = text
    for pattern in STOP_PHRASES:
        compressed = re.sub(pattern, "", compressed, flags=re.IGNORECASE)
    
    # Whitespace normalization
    compressed = re.sub(r'\s+', ' ', compressed).strip()
    return compressed

if __name__ == "__main__":
    sample = "Please note that in today's modern world it is important to mention that the Docker container requires memory limits."
    print("Original:", sample)
    print("Compressed:", compress_prompt(sample))

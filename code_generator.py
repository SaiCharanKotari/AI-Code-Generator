"""
Generate source code from a natural‑language specification.
"""

from transformers import pipeline

# A small, permissively licensed code model.
# Replace with a larger model if you have the GPU resources.
MODEL_NAME = "Salesforce/codegen-350M-mono"

# Use text-generation rather than text2text-generation for code models
generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device_map="auto",          # uses GPU if available
    torch_dtype="auto",         # dtype appropriate for the model
)

SYSTEM_PROMPT = """You are an expert {language} developer.
Write clear, idiomatic {language} code with helpful inline comments.
Return ONLY the code—no explanations, markdown fences, or extra text.
"""

def generate_code(spec: str, language: str = "Python") -> str:
    """
    Create source code that satisfies *spec* in the chosen *language*.

    Parameters
    ----------
    spec : str
        Natural‑language description of what the code should do.
    language : str, optional
        Programming language for the output (default "Python").

    Returns
    -------
    str
        Generated source code.
    """
    prompt = (
        SYSTEM_PROMPT.format(language=language)
        + "\n\n"
        + f"Task: {spec.strip()}\n\n"
        + f"# Begin {language} code\n"
    )

    # Sampling settings balance quality and diversity.
    outputs = generator(
        prompt,
        max_length=512,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        num_return_sequences=1,
        eos_token_id=generator.tokenizer.eos_token_id,
    )
    # The model returns a single string; strip off the prompt.
    generated_full = outputs[0]["generated_text"]
    generated_code = generated_full.replace(prompt, "", 1).strip()

    return generated_code

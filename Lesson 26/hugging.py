import config
from huggingface_hub import InferenceClient

MODELS = getattr(
    config,
    "HF_MODELS",
    ["deepseek-ai/DeepSeek-V3"]
)

def generate(prompt: str, temperature: float = 0.3, max_token: int = 512) -> str:
    key = getattr(config, "HF_API_KEY", None)

    if not key:
        return "API NOT FOUND IN CONFIG FILE"
    
    last_err = None

    for m in MODELS:
        try:
            c = InferenceClient(model=m, token=key)
            r = c.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_token
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err = e
            
    return(
        "Hugging face model failed, change API / model" \
        f"Error faced was: {type(last_err).__name__}: {last_err}"
    )
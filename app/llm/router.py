from app.core.config import settings

def query_llm(prompt: str) -> str:
    """
    Заглушка для LLM: возвращает имитацию ответа.
    Позже сюда можно подключить OpenAI, HuggingFace и т.д.
    """
    return f"LLM response for: {prompt}"

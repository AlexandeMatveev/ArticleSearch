def preprocess_query(query: str) -> str:
    """
    Простая предобработка текста запроса:
    - убираем лишние пробелы
    - приводим к нижнему регистру
    """
    return query.strip().lower()



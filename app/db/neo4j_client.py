from neo4j import GraphDatabase
from app.config.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Инициализируем драйвер при импорте (singleton)
_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def get_driver():
    """Возвращает Neo4j driver."""
    return _driver


def close_driver():
    """Закрывает драйвер (вызывать при shutdown приложения)."""
    global _driver
    try:
        if _driver:
            _driver.close()
    except Exception:
        pass

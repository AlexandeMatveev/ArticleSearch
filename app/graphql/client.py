from typing import List
from app.db.neo4j_client import get_driver
from app.models.schemas import Article, Author, Journal, Topic

def _record_to_article(record) -> Article:
    """
    Преобразует запись Neo4j в Article (pydantic)
    """
    a_node = record.get("a")
    j_node = record.get("j")
    authors_raw = record.get("authors", [])
    topics_raw = record.get("topics", [])

    authors = []
    for au in authors_raw:
        try:
            name = au.get("name")
            if name:
                authors.append(Author(name=name))
        except Exception:
            continue

    topics = []
    for t in topics_raw:
        try:
            name = t.get("name")
            if name:
                topics.append(Topic(name=name))
        except Exception:
            continue

    journal = None
    if j_node:
        jname = j_node.get("name")
        jlink = j_node.get("link")
        journal = Journal(name=jname, link=jlink)

    return Article(
        title=a_node.get("title"),
        description=a_node.get("description"),
        journal=journal,
        authors=authors,
        topics=topics
    )


def get_articles_by_keyword(keyword: str) -> List[Article]:
    """
    Поиск статей по ключевому слову в title/description.
    """
    driver = get_driver()
    with driver.session() as session:
        query = """
        MATCH (a:Article)
        WHERE toLower(a.title) CONTAINS toLower($kw) 
           OR toLower(a.description) CONTAINS toLower($kw)
        OPTIONAL MATCH (a)-[:PUBLISHED_IN]->(j:Journal)
        OPTIONAL MATCH (au:Author)-[:WROTE]->(a)
        OPTIONAL MATCH (a)-[:HAS_TOPIC]->(t:Topic)
        RETURN a, j, collect(DISTINCT au) AS authors, collect(DISTINCT t) AS topics
        LIMIT 100
        """
        result = session.run(query, kw=keyword)
        articles = []
        for rec in result:
            articles.append(_record_to_article(rec))
        return articles


def get_related_articles(title: str) -> List[Article]:
    """
    Возвращает связанные статьи по RELATE_TO или по общим темам.
    """
    driver = get_driver()
    with driver.session() as session:
        # сначала по RELATED_TO
        query = """
        MATCH (a:Article {title:$title})-[:RELATED_TO]->(b:Article)
        OPTIONAL MATCH (b)-[:PUBLISHED_IN]->(j:Journal)
        OPTIONAL MATCH (au:Author)-[:WROTE]->(b)
        OPTIONAL MATCH (b)-[:HAS_TOPIC]->(t:Topic)
        RETURN b AS a, j, collect(DISTINCT au) AS authors, collect(DISTINCT t) AS topics
        LIMIT 50
        """
        result = session.run(query, title=title)
        articles = []
        for rec in result:
            articles.append(_record_to_article(rec))
        return articles

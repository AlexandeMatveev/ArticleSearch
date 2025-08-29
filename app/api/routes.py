from fastapi import APIRouter, Query
from typing import List
from app.models.schemas import Article, UserQuery
from app.db.neo4j_client import neo4j_client
from app.core.middleware import preprocess_query

router = APIRouter()

@router.get("/search", response_model=List[Article])
def search_articles(query: str = Query(..., description="Search query")):
    """
    Поиск статей по тексту запроса.
    """
    query_text = preprocess_query(query)
    cypher = """
    MATCH (a:Article)
    WHERE toLower(a.title) CONTAINS $query OR toLower(a.abstract) CONTAINS $query
    RETURN a.id AS id, a.title AS title, a.abstract AS abstract, a.authors AS authors
    LIMIT 10
    """
    results = neo4j_client.run_query(cypher, {"query": query_text})
    return results



@router.get("/article/{article_id}", response_model=Article)
def get_article(article_id: str):
    """
    Получение конкретной статьи по ID.
    """
    cypher = """
    MATCH (a:Article {id: $id})
    RETURN a.id AS id, a.title AS title, a.abstract AS abstract, a.authors AS authors
    """
    results = neo4j_client.run_query(cypher, {"id": article_id})
    if not results:
        return {"error": "Article not found"}
    return results[0]

@router.get("/recommend/{article_id}", response_model=List[Article])
def recommend_articles(article_id: str):
    """
    Рекомендует статьи, схожие с указанной по ID.
    """
    cypher = """
    MATCH (a:Article {id: $id})-[:SIMILAR_TO]->(b:Article)
    RETURN b.id AS id, b.title AS title, b.abstract AS abstract, b.authors AS authors
    LIMIT 5
    """
    results = neo4j_client.run_query(cypher, {"id": article_id})
    return results

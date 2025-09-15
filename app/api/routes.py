from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import UserQuery, Article
from app.graphql.client import get_articles_by_keyword

router = APIRouter(prefix="/api", tags=["api"])


@router.post("/search", response_model=List[Article])
def search_articles(payload: UserQuery):
    q = payload.query.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Query is empty")
    results = get_articles_by_keyword(q)
    return results

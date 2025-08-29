from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    id: str
    title: str
    abstract: str
    authors: List[str]

class UserQuery(BaseModel):
    query: str

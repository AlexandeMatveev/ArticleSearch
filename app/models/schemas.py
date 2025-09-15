from pydantic import BaseModel
from typing import List, Optional


class Journal(BaseModel):
    name: str
    link: Optional[str] = None


class Author(BaseModel):
    name: str


class Topic(BaseModel):
    name: str


class Article(BaseModel):
    title: str
    description: Optional[str] = None
    journal: Optional[Journal] = None
    authors: List[Author] = []
    topics: List[Topic] = []


class UserQuery(BaseModel):
    query: str

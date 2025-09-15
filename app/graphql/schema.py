import strawberry
from typing import List, Optional
from strawberry.fastapi import GraphQLRouter
from app.graphql.client import get_articles_by_keyword, get_related_articles

@strawberry.type
class JournalType:
    name: str
    link: Optional[str]

@strawberry.type
class AuthorType:
    name: str

@strawberry.type
class TopicType:
    name: str

@strawberry.type
class ArticleType:
    title: str
    description: Optional[str]
    journal: Optional[JournalType]
    authors: List[AuthorType]
    topics: List[TopicType]


@strawberry.type
class Query:
    @strawberry.field
    def search_articles(self, keyword: str) -> List[ArticleType]:
        results = get_articles_by_keyword(keyword)
        # Strawberry автоматически сериализует pydantic -> dataclass-like,
        # но приводим к нужным типам
        return [
            ArticleType(
                title=a.title,
                description=a.description,
                journal=JournalType(name=a.journal.name, link=a.journal.link) if a.journal else None,
                authors=[AuthorType(name=au.name) for au in a.authors],
                topics=[TopicType(name=t.name) for t in a.topics]
            )
            for a in results
        ]

    @strawberry.field
    def related_articles(self, title: str) -> List[ArticleType]:
        results = get_related_articles(title)
        return [
            ArticleType(
                title=a.title,
                description=a.description,
                journal=JournalType(name=a.journal.name, link=a.journal.link) if a.journal else None,
                authors=[AuthorType(name=au.name) for au in a.authors],
                topics=[TopicType(name=t.name) for t in a.topics]
            ) for a in results
        ]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)   # импортируем в main.py

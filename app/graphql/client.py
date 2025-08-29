import requests
from app.core.config import settings

class GraphQLClient:
    def __init__(self, url=settings.GRAPHQL_URL):
        self.url = url

    def query(self, query: str, variables: dict = None):
        response = requests.post(
            self.url,
            json={"query": query, "variables": variables or {}}
        )
        response.raise_for_status()
        return response.json()

graphql_client = GraphQLClient()

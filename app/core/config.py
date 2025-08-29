import os

class Settings:
    NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "Psalom90")
    GRAPHQL_URL: str = os.getenv("GRAPHQL_URL", "http://localhost:5000/graphql")
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "your-api-key")

settings = Settings()

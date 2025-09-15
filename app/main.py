from fastapi import FastAPI
from app.config.config import APP_NAME, GRAPHQL_PREFIX
from app.core.middleware import LoggingMiddleware
from app.api.routes import router as api_router
from app.llm.router import router as llm_router
from app.graphql.schema import graphql_app
from app.db.neo4j_client import close_driver

app = FastAPI(title=APP_NAME)

# Middlewares
app.add_middleware(LoggingMiddleware)

# REST API
app.include_router(api_router)

# LLM routes
app.include_router(llm_router)

# GraphQL mounted at /graphql (prefix in config)
app.include_router(graphql_app, prefix=GRAPHQL_PREFIX)

@app.get("/", include_in_schema=False)
def root():
    return {"status": "ok", "app": APP_NAME}


@app.on_event("shutdown")
def shutdown_event():
    # Закрываем Neo4j драйвер
    try:
        close_driver()
    except Exception:
        pass

from fastapi import FastAPI
from app.api.routes import router as api_router


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Scholar Search API")

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Scholar Search API is running"}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # или ["*"] для разработки
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутов API
from app.api import routes
app.include_router(routes.router)
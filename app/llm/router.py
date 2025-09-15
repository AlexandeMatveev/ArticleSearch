from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/llm", tags=["llm"])


class PingResponse(BaseModel):
    status: str


@router.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(status="ok")

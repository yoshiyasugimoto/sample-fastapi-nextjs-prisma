from logging import getLogger
from fastapi import APIRouter

router = APIRouter()

logger = getLogger(__name__)

@router.get("/")
def health_check():
    return {"status": "ok"}

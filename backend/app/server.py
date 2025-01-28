from contextlib import asynccontextmanager
from logging import Filter, LogRecord, basicConfig, getLogger

from fastapi import FastAPI

from .database import db
from .api.route import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(router)


# ヘルスチェックのログを出力しないようにする
class HealthCheckFilter(Filter):
    def filter(self, record: LogRecord):
        return record.getMessage().find("GET / HTTP/") == -1


getLogger("uvicorn.access").addFilter(HealthCheckFilter())

basicConfig(level="INFO")

from logging import Filter, LogRecord, basicConfig, getLogger

from fastapi import FastAPI

from .api.route import router

app = FastAPI()
app.include_router(router)


# ヘルスチェックのログを出力しないようにする
class HealthCheckFilter(Filter):
    def filter(self, record: LogRecord):
        return record.getMessage().find("GET / HTTP/") == -1


getLogger("uvicorn.access").addFilter(HealthCheckFilter())

basicConfig(level="INFO")

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.db.cache import connect_cache_db, disconnect_cache_db
from app.core.db.database import session_manager
from app.core.middlewares.logging_middleware import LoggingMiddleware
from app.core.middlewares.request_id_middleware import RequestIDMiddleware
from app.core.server import create_fastapi_app


@asynccontextmanager
async def app_lifespan(fastapi_app: FastAPI):
    await connect_cache_db()
    yield
    await disconnect_cache_db()
    if session_manager.engine is not None:
        await session_manager.close()


app = create_fastapi_app(
    name=settings.PROJECT_NAME,
    desc=settings.PROJECT_DESC,
    prefix=settings.API_V1_PREFIX,
    cors_origin=settings.CORS_ORIGINS,
    debug=settings.DEBUG,
    lifespan=app_lifespan,
)

# Register middleware here
app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIDMiddleware)

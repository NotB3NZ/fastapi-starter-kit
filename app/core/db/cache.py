from typing import NewType

from redis.asyncio.client import Redis
from redis.asyncio.connection import ConnectionPool
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError

from app.core.config import settings as s

CacheClient = NewType("CacheClient", Redis)


class CacheDB:
    client: CacheClient = None
    pool: ConnectionPool = None


_cache = CacheDB()


def get_cache_client() -> CacheClient:
    return _cache.client


async def connect_cache_db():
    if _cache.pool is None:
        _cache.pool = ConnectionPool(
            host=s.REDIS_HOST,
            port=s.REDIS_PORT,
            password=s.REDIS_PASS,
            db=0,
            decode_responses=True,
            health_check_interval=15,
            socket_connect_timeout=5,
        )
    retry = Retry(ExponentialBackoff(), 3)
    _cache.client = Redis(
        connection_pool=_cache.pool,
        retry=retry,
        retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError],
    )


async def disconnect_cache_db():
    await _cache.client.aclose()
    await _cache.pool.aclose()

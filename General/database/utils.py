from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from General import config as cfg


async def create_db_session():
    engine = create_async_engine(
        make_connection_string(),
        future=True
    )

    async_session = AsyncSession(engine)
    return async_session


def make_connection_string(async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{cfg.DB_USERNAME}:{cfg.DB_PASSWORD}@{cfg.DB_HOST}:"
        f"{cfg.DB_PORT}/{cfg.DB_NAME}"
    )

    if async_fallback:
        result += "?async_fallback=True"

    return result

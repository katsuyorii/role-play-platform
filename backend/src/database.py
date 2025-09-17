from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .settings import database_settings


class DatabaseConfig:
    def __init__(self, db_url: str, echo: bool = True, echo_pool: bool = True, autoflush: bool = False, expire_on_commit: bool = False):
        self.async_engine = create_async_engine(url=db_url, echo=echo, echo_pool=echo_pool)
        self.async_session = async_sessionmaker(bind=self.async_engine, autoflush=autoflush, expire_on_commit=expire_on_commit)
    
    async def get_session(self):
        async with self.async_session() as session:
            yield session


database_config = DatabaseConfig(database_settings.DATABASE_URL)
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database_config
from .repositories import UsersRepository


def get_users_repository(session: AsyncSession = Depends(database_config.get_session)) -> UsersRepository:
    return UsersRepository(session)
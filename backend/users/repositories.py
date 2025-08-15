from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import UserModel


class UsersRepository(DatabaseBaseRepository):
    def __init__(self, session: AsyncSession, model: UserModel = UserModel):
        super().__init__(session, model)
    
    async def get_by_email_or_username(self, email: str, username: str) -> UserModel | None:
        user = await self.session.execute(select(UserModel).where(or_(UserModel.email == email, UserModel.username == username)))

        return user.scalar_one_or_none()
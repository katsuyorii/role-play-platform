from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from enum import Enum

from core.models.base import BaseModel


class UserRole(str, Enum):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class UserModel(BaseModel):
    __tablename__ = 'users'
    
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str]

    username: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(5), default=UserRole.USER)

    # avatar_url
    # active_character

    is_active: Mapped[bool] = mapped_column(default=False)
    is_mailing: Mapped[bool] = mapped_column(default=True)
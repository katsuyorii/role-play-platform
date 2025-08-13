from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from enum import Enum

from datetime import datetime, date

from core.models.base import BaseModel


class UserRole(str, Enum):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class UserGender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'


class UserModel(BaseModel):
    __tablename__ = 'users'
    
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str]

    username: Mapped[str] = mapped_column(String(255), unique=True)
    role: Mapped[str] = mapped_column(String(5), default=UserRole.USER)
    gender: Mapped[str] = mapped_column(String(6), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(nullable=True)

    # avatar_url
    # active_character

    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    is_active: Mapped[bool] = mapped_column(default=False)
    is_mailing: Mapped[bool] = mapped_column(default=True)
# TODO добавить уровни для форумчан ввиде перечисления

import enum
from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import DateTime, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    ENJOYER = "enjoyer"


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="userrole", create_type=False), default=UserRole.ENJOYER
    )
    display_name: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self) -> str:
        return f"<User {self.email}>, Role: {self.role}"

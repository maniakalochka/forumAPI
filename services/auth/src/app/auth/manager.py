import logging
import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.backend import auth_backend
from app.auth.deps import get_user_manager
from app.core.config import settings
from app.models.orm_models.user import User

log = logging.getLogger(__name__)


class UserManager(BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = settings.VERIFICATION_TOKEN_SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(
            "User %r has forgot their password", user.id
        )

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning(
            "Verification requested for user %r", user.id
        )

    def parse_id(
            self,
            value: str,
    ) -> uuid.UUID:
        return uuid.UUID(value)


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)


@asynccontextmanager
async def user_manager_context(session: AsyncSession):
    user_db = SQLAlchemyUserDatabase(session, User)
    manager = UserManager(user_db)
    try:
        yield manager
    finally:
        return

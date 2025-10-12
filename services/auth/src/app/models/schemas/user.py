import uuid
from typing import Optional

from fastapi_users import schemas as fu_schemas
from pydantic import ConfigDict

from app.models.orm_models.user import UserRole
from app.utilities.alias_gen import to_camel


class UserRead(fu_schemas.BaseUser[uuid.UUID]):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool = True
    role: UserRole = UserRole.ENJOYER
    supervisor_id: Optional[uuid.UUID] = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class UserCreate(fu_schemas.BaseUserCreate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    role: UserRole = UserRole.ENJOYER
    supervisor_id: Optional[uuid.UUID] = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=to_camel,
    )


class UserUpdate(fu_schemas.BaseUserUpdate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[UserRole] = None
    supervisor_id: Optional[uuid.UUID] = None

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
    )

from fastapi_users.authentication import AuthenticationBackend

from app.auth.deps import get_access_token_db
from app.auth.transport import cookie_transport

auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_access_token_db,  # type: ignore
)

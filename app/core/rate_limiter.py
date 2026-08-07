from slowapi import Limiter
from starlette.requests import Request


def user_rate_limit_key(request: Request) -> str:

    user = getattr(request.state, "user", None)

    if user:
        return f"user:{user.id}"

    return request.client.host


limiter = Limiter(
    key_func=user_rate_limit_key,
)
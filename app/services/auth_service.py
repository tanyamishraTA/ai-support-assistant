from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt import create_access_token
from app.auth.password import (
    hash_password,
    verify_password,
)

from app.exceptions.auth import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.schemas.user import (
    UserCreate,
    UserResponse,
)


class AuthService:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.user_repository = UserRepository(db)

    async def register(
        self,
        user_data: UserCreate,
    ) -> UserResponse:

        existing_user = await self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise UserAlreadyExistsException()

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            ),
        )

        created_user = await self.user_repository.create(
            user
        )

        return UserResponse.model_validate(
            created_user
        )

    async def login(
        self,
        credentials: LoginRequest,
    ) -> TokenResponse:

        user = await self.user_repository.get_by_email(
            credentials.email
        )

        if user is None:
            raise InvalidCredentialsException()

        if not verify_password(
            credentials.password,
            user.password_hash,
        ):
            raise InvalidCredentialsException()

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role": user.role.value,
            }
        )

        return TokenResponse(
            access_token=token
        )
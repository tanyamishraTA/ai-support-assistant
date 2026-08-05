from fastapi import Depends, HTTPException, status

from app.auth.current_user import get_current_user
from app.models.user import User, UserRole


async def require_admin(
    current_user: User = Depends(get_current_user),
):

    if current_user.role != UserRole.ADMIN:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user


async def require_employee(
    current_user: User = Depends(get_current_user),
):

    if current_user.role not in (
        UserRole.ADMIN,
        UserRole.EMPLOYEE,
    ):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Employee access required",
        )

    return current_user
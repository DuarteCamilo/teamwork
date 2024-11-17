from app.entities.user_entity import UserEntity
from app.schemas.user import LoginUser

from fastapi import HTTPException


def login(login_user: LoginUser):
    """
    Authenticate a user by their email and password.
    Args:
        login_user (LoginUser): Schema that includes email and password.
    Returns:
        dict: A dictionary containing the authenticated user and their related data (dentist or patient).
    Raises:
        HTTPException: If the credentials are invalid, raises an Unauthorized exception.
    """

    # Buscar al usuario en la base de datos por el email
    user = UserEntity.get_or_none(
        UserEntity.email == login_user.email
        and UserEntity.password == login_user.password
    )

    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid credentials: User not found."
        )

    return user

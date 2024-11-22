from app.entities.user_entity import UserEntity
from app.schemas.user import LoginUser
from app.helpers.hash_helper import HashHelper

from fastapi import HTTPException


def login(login_user: LoginUser):
    """
    Authenticate a user by their email and password.
    Args:
        login_user (LoginUser): Schema that includes email and password.
    Returns:
        dict: A dictionary containing the authenticated user
              and their related data (dentist or patient).
    Raises:
        HTTPException: If the credentials are invalid, raises an Unauthorized exception.
    """

    # Buscar al usuario en la base de datos por el email
    user = UserEntity.get_or_none(UserEntity.email == login_user.email)

    if not user:
        raise HTTPException(
            status_code=401, detail="Invalid credentials: User not found."
        )

    # Verificar que la contraseña sea correcta
    if not HashHelper.verify_password(login_user.password, user.password):
        raise HTTPException(
            status_code=401, detail="Invalid credentials: Incorrect password."
        )

    return user

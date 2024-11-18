from fastapi import APIRouter

from app.schemas.user import LoginUser, User
from app.services import login_service

login_router = APIRouter()


@login_router.post("/")
def login(login_user: LoginUser) -> User:
    """
    Authenticate a user by their email and password.
    Raises an HTTPException if the user is not found or the password is incorrect.
    """
    return login_service.login(login_user)


def get_login_router():
    return login_router

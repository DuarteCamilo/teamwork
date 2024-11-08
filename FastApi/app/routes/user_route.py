"""
This module contains the user route for the FastAPI application.
"""

from services import user_service
from fastapi import APIRouter

user_route = APIRouter()


@user_route.post("/users/")
def login_user(email: str, password: str):
    """
    Authenticate a user by their email and password.
    Raises an HTTPException if the user is not found or the password is incorrect.
    Args:
      email (str): The email address of the user.
      password (str): The password provided by the user.
    Returns:
      UserModel: The authenticated user object.
    """
    return user_service.login_user(email, password)

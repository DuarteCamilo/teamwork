"""
This module provides services related to user operations such as retrieving a user by email,
verifying passwords, and logging in a user.
Functions:
  get_user_by_email(email: str):
    Retrieves a user from the database by their email address.
  verify_password(plain_password: str, hashed_password: str):
    Verifies if the provided plain text password matches the hashed password.
  login_user(email: str, password: str):
    Authenticates a user by their email and password.
    Raises HTTPException if the user is not found or the password is incorrect.
"""

import os
from services.dentist_service import get_dentist
from services.patient_service import get_patient
from dotenv import load_dotenv
from fastapi import HTTPException
from config.database import UserModel

load_dotenv()


def get_user_by_email(email: str):
    """
    Retrieve a user from the database by their email address.
    Args:
      email (str): The email address of the user to retrieve.
    Returns:
      UserModel: The user object if found, otherwise None.
    """
    user = UserModel.select().where(UserModel.email == email).first()
    return user


def get_user_by_username(username: str):
    """
    Retrieve a user from the database by their username.
    Args:
      username (str): The username of the user to retrieve.
    Returns:
      UserModel: The user object if found, otherwise None.
    """
    user = UserModel.select().where(UserModel.username == username).first()
    return user


def verify_password(plain_password: str, hashed_password: str):
    """
    Verify if the provided plain text password matches the hashed password.
    Args:
      plain_password (str): The plain text password to verify.
      hashed_password (str): The hashed password to compare against.
    Returns:
      bool: True if the passwords match, False otherwise.
    """
    return plain_password == hashed_password


def login_user(email: str, username: str, password: str):
    """
    Authenticates a user based on email/username and password.
    Args:
      email (str): The email of the user. Either email or username must be provided.
      username (str): The username of the user. Either email or username must be provided.
      password (str): The password of the user.
    Raises:
      HTTPException: If neither email nor username is provided.
      HTTPException: If password is not provided.
      HTTPException: If the user is not found.
      HTTPException: If the password is incorrect.
    Returns:
      User: The authenticated user object.
    """

    if not email and not username:
        raise HTTPException(status_code=400, detail="Email or username is required")
    if not password:
        raise HTTPException(status_code=400, detail="Password is required")

    if email:
        user = get_user_by_email(email)
    else:
        user = get_user_by_username(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    if user.role == os.getenv("DENTIST_ROLE"):
        user.person = get_dentist(user.id_user)
    elif user.role == os.getenv("PATIENT_ROLE"):
        user.person = get_patient(user.id_user)

    return user

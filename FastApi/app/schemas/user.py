"""
This module defines Pydantic models for user dtos.
"""

from pydantic import Field, validator

from app.schemas.base_schema import BaseSchema
from app.schemas.user_and_role import UserAndRole


class User(BaseSchema):
    """
    Schema for a user.
    """

    id: int = None
    email: str = None
    password: str = None
    name: str = None
    lastname: str = None
    roles: list[UserAndRole] = Field([], exclude=True)
    role_ids: list[int] = []

    # pylint: disable=no-self-argument
    @validator("role_ids", pre=True, always=True)
    def set_role_ids(v, values):
        """
        Set the role ids.
        """

        roles: list[UserAndRole] = values.get("roles", [])
        return {role.role_id for role in roles}

    # pylint: enable=no-self-argument


class UserCreate(BaseSchema):
    """
    Schema for creating a new user.
    """

    email: str = Field(..., max_length=320)
    password: str = Field(..., max_length=255)
    name: str = Field(..., max_length=255)
    lastname: str = Field(..., max_length=255)
    role_ids: list[int]


class UserUpdate(BaseSchema):
    """
    Schema for updating a user.
    """

    email: str = Field(None, max_length=320)
    password: str = Field(None, max_length=255)
    name: str = Field(None, max_length=255)
    lastname: str = Field(None, max_length=255)
    role_ids: list[int] = None

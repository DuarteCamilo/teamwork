"""
This module defines Pydantic models for role dtos.
"""

from pydantic import Field, validator

from app.schemas.base_schema import BaseSchema
from app.schemas.user_and_role import UserAndRole


class Role(BaseSchema):
    """
    Schema for a role.
    """

    id: int = None
    name: str = None
    users: list[UserAndRole] = Field(None, exclude=True)
    user_ids: set[int] = None

    # pylint: disable=no-self-argument

    @validator("user_ids", pre=True, always=True)
    def set_user_ids(v, values):
        """
        Set the user ids.
        """

        users: list[UserAndRole] = values.get("users", [])
        return {user.user_id for user in users}

    # pylint: enable=no-self-argument


class RoleCreate(BaseSchema):
    """
    Schema for creating a new role.
    """

    name: str = Field(..., max_length=127)


class RoleUpdate(BaseSchema):
    """
    Schema for updating a role
    """

    name: str = Field(None, max_length=127)

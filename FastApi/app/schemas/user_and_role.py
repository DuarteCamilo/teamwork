"""
This module defines Pydantic models for user and role dtos.
"""

from app.schemas.base_schema import BaseSchema


class UserAndRole(BaseSchema):
    """
    Schema for a user and role.
    """

    id: int = None
    user_id: int = None
    role_id: int = None

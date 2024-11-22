from typing import Any

from app.controllers.role_controller import get_role_controller
from app.entities.role_entity import RoleEntity
from app.entities.user_and_role_entity import UserAndRoleEntity
from app.entities.user_entity import UserEntity
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.base_service import BaseService
from app.services.user_and_role_service import get_user_and_role_service
from app.helpers.hash_helper import HashHelper
from peewee import Model

from fastapi import HTTPException


class UserService(BaseService):
    """A service that provides CRUD operations for the User entity."""

    def __init__(self):
        super().__init__(entity_name="User", entity=UserEntity)

    def create(self, model: UserCreate) -> User:
        """Create a new user."""
        validate_model(self, model)
        model.password = HashHelper.hash_password(model.password)
        return super().create(model)

    def update(self, _id, model: UserUpdate) -> User:
        """Update a user by their ID."""
        validate_model(self, model)
        model.password = HashHelper.hash_password(model.password)
        return super().update(_id, model)


def validate_model(service: UserService, model: UserCreate | UserUpdate):
    """Validate the user model."""
    if UserEntity.get_or_none(UserEntity.email == model.email):
        raise HTTPException(
            status_code=400,
            detail=f"{service.name} with email '{model.email}' already exists",
        )


user_service = UserService()


def get_user_service():
    """Get an instance of the user service."""
    return user_service

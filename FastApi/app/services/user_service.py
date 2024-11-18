from typing import Any

from app.controllers.role_controller import get_role_controller
from app.entities.role_entity import RoleEntity
from app.entities.user_and_role_entity import UserAndRoleEntity
from app.entities.user_entity import UserEntity
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.base_service import BaseService
from app.services.user_and_role_service import get_user_and_role_service
from peewee import Model

from fastapi import HTTPException


class UserService(BaseService):
    def __init__(self):
        super().__init__(entity_name="User", entity=UserEntity)

    def create(self, model: UserCreate) -> User:
        validate_model(self, model)
        return super().create(model)

    def update(self, _id, model: UserUpdate) -> User:
        validate_model(self, model)
        return super().update(_id, model)


def validate_model(service: UserService, model: UserCreate | UserUpdate):
    if UserEntity.get_or_none(UserEntity.email == model.email):
        raise HTTPException(
            status_code=400,
            detail=f"{service.name} with email '{model.email}' already exists",
        )


user_service = UserService()


def get_user_service():
    return user_service

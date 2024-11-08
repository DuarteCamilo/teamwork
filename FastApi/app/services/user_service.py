from typing import Any

from fastapi import HTTPException
from peewee import Model

from app.controllers.role_controller import get_role_controller
from app.entities.role_entity import RoleEntity
from app.entities.user_and_role_entity import UserAndRoleEntity
from app.entities.user_entity import UserEntity
from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.user_and_role import UserAndRole
from app.services.base_service import BaseService
from app.services.user_and_role_service import get_user_and_role_service


class UserService(BaseService):
    def __init__(self):
        super().__init__(entity_name="User", entity=UserEntity)

    def create(self, model: UserCreate) -> User:
        validate_model(self, model)
        return update_role_ids(super().create(model))

    def update(self, _id, model: UserUpdate) -> User:
        validate_model(self, model)
        role_ids = model.role_ids

        updated_model: User = update_model(self, _id, model)
        updated_model.role_ids = role_ids

        return update_role_ids(updated_model)


def update_model(service: UserService, _id, model: UserUpdate) -> Model:
    allowed_fields = {
        field: value
        for field, value in model.model_dump(
            exclude_defaults=True, exclude_unset=True, exclude_none=True
        ).items()
        if field in service.entity._meta.fields
    }

    if len(allowed_fields) > 0:
        service.entity.update(**allowed_fields).where(
            service.entity.id == _id
        ).execute()

    return service.get_by_id(_id)


def validate_model(service: UserService, model: UserCreate | UserUpdate):
    if model.role_ids:
        for role_id in model.role_ids:
            if not RoleEntity.get_or_none(RoleEntity.id == role_id):
                raise HTTPException(
                    status_code=400,
                    detail=f"Role with id '{role_id}' does not exist",
                )

    if UserEntity.get_or_none(UserEntity.email == model.email):
        raise HTTPException(
            status_code=400,
            detail=f"{service.name} with email '{model.email}' already exists",
        )


def update_role_ids(model: User):
    if model.role_ids:
        existing_roles: list[UserAndRole] = list(
            UserAndRoleEntity.select().where(UserAndRoleEntity.user == model.id)
        )

        for user_and_role in existing_roles:
            if user_and_role.role_id not in model.role_ids:
                user_and_role.delete_instance()

        for role_id in model.role_ids:
            existing_role = (
                UserAndRoleEntity.select()
                .where(
                    (UserAndRoleEntity.user == model.id)
                    & (UserAndRoleEntity.role == role_id)
                )
                .first()
            )

            if not existing_role:
                UserAndRoleEntity.create(user_id=model.id, role_id=role_id)
    return model


user_service = UserService()


def get_user_service():
    return user_service
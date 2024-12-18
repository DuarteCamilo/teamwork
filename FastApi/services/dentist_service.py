from app.entities.dentist_entity import DentistEntity
from app.entities.user_entity import UserEntity
from app.schemas.dentist import DentistCreate, DentistUpdate
from app.services.base_service import BaseService

from fastapi import HTTPException


class DentistService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Dentist", entity=DentistEntity)

    def create(self, model: DentistCreate) -> DentistCreate:
        validate_model(model)
        return super().create(model)

    def update(self, _id, model: DentistUpdate) -> DentistUpdate:
        validate_model(model)
        return super().update(_id, model)


def validate_model(model: DentistCreate | DentistUpdate):
    if not UserEntity.get_or_none(UserEntity.id == model.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{model.user_id}' does not exist",
        )

    if DentistEntity.get_or_none(DentistEntity.user == model.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{model.user_id}' is already associated with a dentist",
        )


dentist_service = DentistService()


def get_dentist_service():
    return dentist_service

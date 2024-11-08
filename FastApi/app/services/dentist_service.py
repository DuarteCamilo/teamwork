""" 
This module contains the service layer for the Dentist entity.
"""

from fastapi import HTTPException

from app.entities.dentist_entity import DentistEntity
from app.entities.user_entity import UserEntity
from app.schemas.dentist import DentistCreate, DentistUpdate
from app.services.base_service import BaseService


class DentistService(BaseService):
    """
    Provides CRUD operations for the Dentist entity.
    """

    def __init__(self):
        super().__init__(entity_name="Dentist", entity=DentistEntity)

    def create(self, model: DentistCreate) -> DentistCreate:
        validate_model(model)
        return super().create(model)

    def update(self, _id, model: DentistUpdate) -> DentistUpdate:
        validate_model(model)
        return super().update(_id, model)


def validate_model(model: DentistCreate | DentistUpdate):
    """
    Validates the model before creating or updating a Dentist entity.
    """

    if not UserEntity.get_or_none(UserEntity.id == model.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{model.user_id}' does not exist",
        )


dentist_service = DentistService()


def get_dentist_service():
    """
    Returns the DentistService instance
    """

    return dentist_service

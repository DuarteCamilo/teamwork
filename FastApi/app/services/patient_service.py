from fastapi import HTTPException

from app.entities.patient_entity import PatientEntity
from app.entities.user_entity import UserEntity
from app.schemas.patient import PatientCreate, PatientUpdate
from app.services.base_service import BaseService


class PatientService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Patient", entity=PatientEntity)

    def create(self, model: PatientCreate) -> PatientCreate:
        validate_model(self, model)
        return super().create(model)

    def update(self, _id, model: PatientUpdate) -> PatientUpdate:
        validate_model(self, model)
        return super().update(_id, model)


def validate_model(service: PatientService, model: PatientCreate | PatientUpdate):
    if not UserEntity.get_or_none(UserEntity.id == model.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{model.user_id}' does not exist",
        )

    if PatientEntity.get_or_none(PatientEntity.user == model.user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{model.user_id}' is already associated with a patient",
        )

    if PatientEntity.get_or_none(PatientEntity.dni == model.dni):
        raise HTTPException(
            status_code=400,
            detail=f"{service.name} with dni '{model.dni}' already exists",
        )


patient_service = PatientService()


def get_patient_service():
    return patient_service

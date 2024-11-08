from datetime import date

from fastapi import HTTPException

from app.entities.appointment_entity import AppointmentEntity
from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.entities.dentist_entity import DentistEntity
from app.entities.patient_entity import PatientEntity
from app.schemas.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.services.base_service import BaseService


class AppointmentService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Appointment", entity=AppointmentEntity)

    def create(self, model: AppointmentCreate) -> Appointment:
        validate_model(model)
        return super().create(model)

    def update(self, _id, model: AppointmentCreate) -> Appointment:
        validate_model(model)
        return super().update(_id, model)


def validate_model(model: AppointmentCreate | AppointmentUpdate):
    if not AppointmentLabelEntity.get_or_none(model.label_id):
        raise HTTPException(
            status_code=400,
            detail=f"Label with id '{model.label_id}' does not exist",
        )

    if not PatientEntity.get_or_none(model.patient_id):
        raise HTTPException(
            status_code=400,
            detail=f"Patient with id '{model.patient_id}' does not exist",
        )

    if not DentistEntity.get_or_none(model.dentist_id):
        raise HTTPException(
            status_code=400,
            detail=f"Dentist with id '{model.dentist_id}' does not exist",
        )

    if model.date < date.today():
        raise HTTPException(
            status_code=400,
            detail="Date cannot be in the past",
        )


appointment_service = AppointmentService()


def get_appointment_service():
    return appointment_service

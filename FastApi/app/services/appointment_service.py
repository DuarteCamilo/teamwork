from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytz

from app.entities.appointment_entity import AppointmentEntity
from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.entities.dentist_entity import DentistEntity
from app.entities.patient_entity import PatientEntity
from app.schemas.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.services.base_service import BaseService
from app.helpers.format_helper import convert_to_local_time

from fastapi import HTTPException


class AppointmentService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Appointment", entity=AppointmentEntity)

    def create(self, model: AppointmentCreate) -> Appointment:
        validate_model(model)
        return super().create(model)

    def update(self, _id, model: AppointmentCreate) -> Appointment:
        validate_model(model)
        return super().update(_id, model)

def get_appointments_dentist(_id: int) -> list:
    appointments = AppointmentEntity.select().where(AppointmentEntity.dentist == _id)

    if not appointments:
        raise HTTPException(
            status_code=404,
            detail=f"No appointments found for dentist with id {_id}"
        )

    appointments_data = [Appointment.from_orm(appointment) for appointment in appointments]
    return appointments_data

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

    now = convert_to_local_time(datetime.now()) 
    appointments = get_appointments_dentist(model.dentist_id)

    if convert_to_local_time(model.date) < now:
        raise HTTPException(
            status_code=400,
            detail="Date cannot be in the past",
        )

    for appoint in appointments:
       appointment_label = AppointmentLabelEntity.get_or_none(appoint.label_id)
       if not appointment_label:
           continue

       duration_time = appointment_label.duration

       start_time = appoint.date.time()
       start_date = appoint.date.date()

       start_timedelta = timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
       duration_timedelta = timedelta(hours=duration_time.hour, minutes=duration_time.minute, seconds=duration_time.second)
       end_timedelta = start_timedelta + duration_timedelta

       end_time = (datetime.min + end_timedelta).time()

       if model.date.date() == start_date:
           if model.date.time() >= start_time and model.date.time() < end_time:
               raise HTTPException(
                   status_code=400,
                   detail="Appointment time conflicts with an existing appointment."
               )
    
appointment_service = AppointmentService()


def get_appointment_service():
    return appointment_service

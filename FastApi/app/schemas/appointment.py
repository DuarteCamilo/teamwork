"""
This module defines Pydantic models for appointment dtos.
"""

from datetime import date as dt_date

from app.schemas.base_schema import BaseSchema


class Appointment(BaseSchema):
    """
    Schema for an appointment.
    """

    id: int = None
    date: dt_date = None
    label_id: int = None
    patient_id: int = None
    dentist_id: int = None


class AppointmentCreate(BaseSchema):
    """
    Schema for creating a new appointment.
    """

    date: dt_date
    label_id: int
    patient_id: int
    dentist_id: int


class AppointmentUpdate(BaseSchema):
    """
    Schema for updating an appointment.
    """

    date: dt_date = None
    label_id: int = None
    patient_id: int = None
    dentist_id: int = None

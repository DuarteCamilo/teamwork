"""
This module defines Pydantic models for patient dtos.
"""

from datetime import datetime

from pydantic import Field, validator

from app.helpers.schemas_helper import get_appointment_ids
from app.schemas.appointment import Appointment
from app.schemas.base_schema import BaseSchema


class Patient(BaseSchema):
    """
    Schema for a patient.
    """

    id: int = None
    dni: int = None
    address: str = None
    admission_date: datetime = None
    user_id: int = None
    appointments: list[Appointment] = Field(None, exclude=True)
    appointment_ids: set[int] = None

    # pylint: disable=no-self-argument

    @validator("appointment_ids", pre=True, always=True)
    def set_appointment_ids(v, values):
        """
        Set the appointment ids.
        """

        return get_appointment_ids(values)

    # pylint: enable=no-self-argument


class PatientCreate(BaseSchema):
    """
    Schema for creating a new patient.
    """

    dni: int
    address: str = Field(..., max_length=255)
    admission_date: datetime = datetime.now()
    user_id: int


class PatientUpdate(BaseSchema):
    """
    Schema for updating a patient.
    """

    dni: int = None
    address: str = Field(None, max_length=255)
    admission_date: datetime = None
    user_id: int = None

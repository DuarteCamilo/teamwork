"""
This module defines Pydantic models for dentist dtos.
"""

from datetime import date, time

from pydantic import Field, validator

from app.helpers.schemas_helper import get_appointment_ids
from app.schemas.appointment import Appointment
from app.schemas.base_schema import BaseSchema


class Dentist(BaseSchema):
    """
    Schema for a dentist.
    """

    id: int = None
    license: str = None
    workday_start_time: time | None = None
    workday_end_time: time | None = None
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
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


class DentistCreate(BaseSchema):
    """
    Schema for creating a new dentist.
    """

    license: str = Field(..., max_length=255)
    workday_start_time: time
    workday_end_time: time
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
    user_id: int


class DentistUpdate(BaseSchema):
    """
    Schema for updating a dentist.
    """

    license: str = Field(None, max_length=255)
    workday_start_time: time = None
    workday_end_time: time = None
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
    user_id: int = None

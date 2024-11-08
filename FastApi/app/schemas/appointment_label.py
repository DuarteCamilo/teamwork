"""
This module defines Pydantic models for appointment label dtos.
"""

from datetime import time

from pydantic import Field, validator

from app.helpers.schemas_helper import get_appointment_ids
from app.schemas.appointment import Appointment
from app.schemas.base_schema import BaseSchema


class AppointmentLabel(BaseSchema):
    """
    Schema for an appointment label.
    """

    id: int = None
    name: str = None
    duration: time = None
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


class AppointmentLabelCreate(BaseSchema):
    """
    Schema for creating a new appointment label.
    """

    name: str = Field(..., max_length=127)
    duration: time


class AppointmentLabelUpdate(BaseSchema):
    """
    Schema for updating a appointment label
    """

    name: str = Field(None, max_length=127)
    duration: time = None

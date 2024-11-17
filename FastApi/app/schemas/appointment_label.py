from datetime import time

from app.schemas.base_schema import BaseSchema
from pydantic import Field


class AppointmentLabel(BaseSchema):
    """
    Schema for an appointment label.
    Attributes:
      id (int): The unique identifier for the appointment label.
      name (str): The name of the appointment label.
      duration (time): The duration of the appointment.
    """

    id: int = None
    name: str = None
    duration: time = None


class AppointmentLabelCreate(BaseSchema):
    """
    Schema for creating a new appointment label.
    Attributes:
      name (str): The name of the appointment label. Maximum length is 127 characters.
      duration (time): The duration of the appointment. Defaults to the current date and time.
    """

    name: str = Field(..., max_length=127)
    duration: time


class AppointmentLabelUpdate(BaseSchema):
    """
    Schema for updating a appointment label
    Attributes:
      name (str): The name of the appointment label. Maximum length is 127 characters.
      duration (time): The duration of the appointment.
    """

    name: str = Field(None, max_length=127)
    duration: time = None

from datetime import date, time

from fastapi import HTTPException
from pydantic import Field

from app.schemas.base_schema import BaseSchema


class Dentist(BaseSchema):
    """
    Schema for a dentist.
    Attributes:
      license (str): The license number of the dentist.
      workday_start_time (time): The start time of the dentist's workday.
      workday_end_time (time): The end time of the dentist's workday.
      inactivity_start_date (date): The start date of the dentist's inactivity.
      inactivity_end_date (date): The end date of the dentist's inactivity.
      user_id (int): The unique identifier of the user.
    """

    id: int = None
    license: str = None
    workday_start_time: time = None
    workday_end_time: time = None
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
    user_id: int = None


class DentistCreate(BaseSchema):
    """
    Schema for creating a new dentist.
    Attributes:
      license (str): The license number of the dentist, max length 255.
      workday_start_time (time): The start time of the dentist's workday.
      workday_end_time (time): The end time of the dentist's workday.
      inactivity_start_date (date): The start date of the dentist's inactivity.
      inactivity_end_date (date): The end date of the dentist's inactivity.
      user_id (int): The unique identifier
    """

    license: str = Field(..., max_length=255)
    workday_start_time: time = Field(...)
    workday_end_time: time = Field(...)
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
    user_id: int


class DentistUpdate(BaseSchema):
    """
    Schema for updating a dentist.
    Attributes:
      license (str): The license number of the dentist, max length 255.
      workday_start_time (time): The start time of the dentist's workday.
      workday_end_time (time): The end time of the dentist's workday.
      inactivity_start_date (date): The start date of the dentist's inactivity.
      inactivity_end_date (date): The end date of the dentist's inactivity.
      user_id (int): The unique identifier
    """

    license: str = Field(None, max_length=255)
    workday_start_time: time = None
    workday_end_time: time = None
    inactivity_start_date: date | None = None
    inactivity_end_date: date | None = None
    user_id: int = None

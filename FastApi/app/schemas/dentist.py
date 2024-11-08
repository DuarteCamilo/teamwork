from datetime import date, time

from fastapi import HTTPException
from pydantic import Field, model_validator

from app.entities.user_entity import UserEntity
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

    # pylint: disable=no-self-argument

    @model_validator(mode="before")
    def validate_model(cls, values):
        validate_model(values)
        return values

    # pylint: enable=no-self-argument


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

    # pylint: disable=no-self-argument

    @model_validator(mode="before")
    def validate_model(cls, values):
        validate_model(values)
        return values

    # pylint: enable=no-self-argument


def validate_model(values):
    user_id = values.get("user_id")

    if not UserEntity.get_or_none(UserEntity.id == user_id):
        raise HTTPException(
            status_code=400,
            detail=f"User with id '{user_id}' does not exist",
        )

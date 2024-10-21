"""
This module defines the Pydantic model for a dentist.
"""

from pydantic import BaseModel, Field


class Dentist(BaseModel):
    """
    Dentist schema for FastAPI application.
    Attributes:
      id_dentist (int): Unique identifier for the dentist.
      name (str): First name of the dentist, with a maximum length of 40 characters.
      lastname (str): Last name of the dentist, with a maximum length of 40 characters.
      license (str): License number of the dentist, with a maximum length of 40 characters.
      id_state (int): Identifier for the state where the dentist is licensed.
      inactive_days (int): Number of inactive days for the dentist.
      id_user (int): Identifier for the associated user.
      id_schedule (int): Identifier for the associated schedule.
    Config:
      orm_mode (bool): Enables ORM mode for compatibility with ORMs.
    """

    id_dentist: int
    name: str = Field(..., max_length=40)
    last_name: str = Field(..., max_length=40)
    license: str = Field(..., max_length=40)
    id_state: int
    inactive_days: int
    id_user: int
    id_schedule: int

    class Config:
        """
        Configuration class for Pydantic models.
        """

        orm_mode = True


class DentistCreate(BaseModel):
    """Dentist schema for creating a new dentist in the FastAPI application."""

    name: str = Field(..., max_length=40)
    last_name: str = Field(..., max_length=40)
    license: str = Field(..., max_length=40)
    id_state: int
    inactive_days: int
    id_user: int
    id_schedule: int


class DentistUpdate(BaseModel):
    """Dentist schema for updating an existing dentist in the FastAPI application."""

    name: str = Field(None, max_length=40)
    last_name: str = Field(None, max_length=40)
    license: str = Field(None, max_length=40)
    id_state: int
    inactive_days: int
    id_user: int
    id_schedule: int

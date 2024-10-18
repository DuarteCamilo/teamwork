from pydantic import BaseModel, Field
from datetime import date


class Patient(BaseModel):
    """
    Patient schema for FastAPI application.
    Attributes:
      id_patient (int): Unique identifier for the patient.
      name (str): First name of the patient, with a maximum length of 40 characters.
      last_name (str): Last name of the patient, with a maximum length of 40 characters.
      address (str): Address of the patient, with a maximum length of 100 characters.
      departure_date (date): Date when the patient departs from the system.
      id_user (int): Identifier for the associated user.
      dni (int): National identification number of the patient.
    Config:
      orm_mode (bool): Enables ORM mode for compatibility with ORMs.
    """

    id_patient: int
    name: str = Field(..., max_length=40)
    last_name: str = Field(..., max_length=40)
    address: str = Field(..., max_length=100)
    departure_date: date
    id_user: int
    dni: int

    class Config:
        """
        Configuration class for Pydantic models.
        """
        orm_mode = True

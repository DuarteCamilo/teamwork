from datetime import datetime

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class Patient(BaseSchema):
    """
    Schema for a patient.
    Attributes:
      dni (int): The DNI of the patient.
      address (str): The address of the patient.
      admission_date (date): The departure date of the patient.
      user_id (int): The unique identifier of the user.
    """

    id: int = None
    dni: int = None
    address: str = None
    admission_date: datetime = None
    user_id: int = None


class PatientCreate(BaseSchema):
    """
    Schema for creating a new patient.
    Attributes:
      dni (int): The DNI of the patient.
      address (str): The address of the patient, max length 255.
      admission_date (date): The departure date of the patient,defaults to the current date and time.
      user_id (int): The unique identifier of the user.
    """

    dni: int
    address: str = Field(..., max_length=255)
    admission_date: datetime = datetime.now()
    user_id: int


class PatientUpdate(BaseSchema):
    """
    Schema for updating a patient.
    Attributes:
      dni (int): The DNI of the patient.
      address (str): The address of the patient, max length 255.
      admission_date (date): The departure date of the patient.
      user_id (int): The unique identifier of the user.
    """

    dni: int = None
    address: str = Field(None, max_length=255)
    admission_date: datetime = None
    user_id: int = None

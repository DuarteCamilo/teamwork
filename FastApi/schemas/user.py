from app.schemas.base_schema import BaseSchema
from app.schemas.dentist import Dentist
from app.schemas.patient import Patient
from pydantic import Field, validator


class User(BaseSchema):
    """
    Schema for a user.
    Attributes:
      id (int): The unique identifier for the user.
      email (str): The email address of the user.
      password (str): The user's password.
      name (str): The first name of the user.
      lastname (str): The last name of the user.
      roles (list[Role]): The roles associated with the user.
      role_ids (list[int]): The role IDs associated with the user.
      appointments (list[Appointment]): The appointments associated with the user.
      appointment_ids (list[int]): The appointment IDs associated with the user.
    """

    id: int = None
    email: str = None
    password: str = None
    name: str = None
    lastname: str = None
    is_admin: bool = None
    patients: list[Patient] = Field(None, exclude=True)
    patient_id: int | None = None
    dentists: list[Dentist] = Field(None, exclude=True)
    dentist_id: int | None = None

    # pylint: disable=no-self-argument

    @validator("patient_id", pre=True, always=True)
    def set_patient_id(v, values):
        patients: list[Patient] = values.get("patients")
        return patients[0].id if patients else None

    @validator("dentist_id", pre=True, always=True)
    def set_dentist_id(v, values):
        dentists: list[Dentist] = values.get("dentists")
        print(bool(dentists))
        return dentists[0].id if dentists else None

    # pylint: enable=no-self-argument


class UserCreate(BaseSchema):
    """
    Schema for creating a new user.
    Attributes:
      email (str): The email address of the user. Max length is 320 characters.
      password (str): The user's password. Max length is 255 characters.
      name (str): The first name of the user.
      lastname (str): The last name of the user.
      role_ids (list[int]): The role IDs associated with the user.
    """

    email: str = Field(..., max_length=320)
    password: str = Field(..., max_length=255)
    name: str = Field(..., max_length=255)
    lastname: str = Field(..., max_length=255)
    is_admin: bool = Field(False)


class UserUpdate(BaseSchema):
    """
    Schema for updating a user.
    Attributes:
      email (str): The email address of the user. Max length is 320 characters.
      password (str): The user's password. Max length is 255 characters.
      name (str): The first name of the user.
      lastname (str): The last name of the user.
      role_ids (list[int]): The role IDs associated with the user.
    """

    email: str = Field(None, max_length=320)
    password: str = Field(None, max_length=255)
    name: str = Field(None, max_length=255)
    lastname: str = Field(None, max_length=255)
    is_admin: bool = None


class LoginUser(BaseSchema):
    email: str = Field(None, max_length=320)
    password: str = Field(None, max_length=255)

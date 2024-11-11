from pydantic import Field, validator

from app.schemas.base_schema import BaseSchema
from app.schemas.role import Role
from app.schemas.user_and_role import UserAndRole
from app.schemas.patient import Patient
from app.schemas.dentist import Dentist


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
    patient_id: int = None
    dentist_id: int = None
    
    
    # roles: list[UserAndRole] = Field(default_factory=None, exclude=True)
    # role_ids: list[int] = None
    # appointments: list[Appointment] = Field(default_factory=None, exclude=True)
    # appointment_ids: list[int] = None

    # pylint: disable=no-self-argument
    # @validator("role_ids", pre=True, always=True)
    # def set_role_ids(v, values):
    #     roles: list[UserAndRole] = values.get("roles", [])
    #     return {role.role_id for role in roles}

    # @validator("appointment_ids", pre=True, always=True)
    # def set_appointment_ids(v, values):
    #     return [appointment.id for appointment in values.get("appointments", [])]

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
    role_ids: list[int]


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
    role_ids: list[int] = None


class LoginUser(BaseSchema):
    email: str = Field(None, max_length=320)
    password: str = Field(None, max_length=255)

from app.schemas.base_schema import BaseSchema
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

    # roles: list[UserAndRole] = Field(default_factory=None, exclude=True)
    # role_ids: list[int] = None
    # appointments: list[Appointment] = Field(default_factory=None, exclude=True)
    # appointment_ids: list[int] = None

    # pylint: disable=no-self-argument
    # @validator("role_ids", pre=True, always=True)
    # def set_role_ids(v, values):
    #     roles: list[UserAndRole] = values.get("roles", [])
    #     return {role.role_id for role in roles}

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


class LoginUser(BaseSchema):
    email: str = Field(None, max_length=320)
    password: str = Field(None, max_length=255)
from pydantic import Field

from app.schemas.base_schema import BaseSchema


class Role(BaseSchema):
    """
    Schema for a role.
    Attributes:
      id (int): The unique identifier for the role.
      name (str): The name of the role.
    """

    id: int = None
    name: str = None


class RoleCreate(BaseSchema):
    """
    Schema for creating a new role.
    Attributes:
      name (str): The name of the role. Maximum length is 127 characters.
    """

    name: str = Field(..., max_length=127)


class RoleUpdate(BaseSchema):
    """
    Schema for updating a role
    Attributes:
      name (str): The name of the role. Maximum length is 127 characters.
    """

    name: str = Field(None, max_length=127)

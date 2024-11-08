from app.schemas.base_schema import BaseSchema


class UserAndRole(BaseSchema):
    """
    Schema for a user and role.
    Attributes:
      user_id (int): The unique identifier for the user.
      role_id (int): The unique identifier for the role.
    """

    id: int = None
    user_id: int = None
    role_id: int = None

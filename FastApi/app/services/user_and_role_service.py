"""
This module contains the service layer for the UserAndRole entity.
"""

from app.entities.user_and_role_entity import UserAndRoleEntity
from app.services.base_service import BaseService


class UserAndRoleService(BaseService):
    """
    Provides CRUD operations for the UserAndRole entity.
    """

    def __init__(self):
        super().__init__(entity_name="UserAndRole", entity=UserAndRoleEntity)


user_and_role_service = UserAndRoleService()


def get_user_and_role_service():
    """
    Returns the UserAndRoleService instance.
    """

    return user_and_role_service

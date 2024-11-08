"""
This module contains the service layer for the Role entity.
"""

from app.entities.role_entity import RoleEntity
from app.services.base_service import BaseService


class RoleService(BaseService):
    """
    Provides CRUD operations for the Role entity.
    """

    def __init__(self):
        super().__init__(entity_name="Role", entity=RoleEntity)


role_service = RoleService()


def get_role_service():
    """
    Returns the RoleService instance.
    """

    return role_service

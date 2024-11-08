"""
This module defines the Peewee model for the UserAndRole entity.
"""

from peewee import AutoField, ForeignKeyField

from app.entities.base_entity import BaseEntity
from app.entities.role_entity import RoleEntity
from app.entities.user_entity import UserEntity


class UserAndRoleEntity(BaseEntity):
    """
    UserAndRole represents a user and role entity in the database.
    """

    id = AutoField(primary_key=True)
    user = ForeignKeyField(UserEntity, backref="roles", on_delete="CASCADE")
    role = ForeignKeyField(RoleEntity, backref="users", on_delete="CASCADE")

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "users_roles"

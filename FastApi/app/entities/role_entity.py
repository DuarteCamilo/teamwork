"""
This module defines the Peewee model for the Role entity.
"""

from peewee import AutoField, CharField

from app.entities.base_entity import BaseEntity


class RoleEntity(BaseEntity):
    """
    Represents a role entity in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=127)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "roles"

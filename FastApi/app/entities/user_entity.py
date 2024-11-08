"""
This module defines the Peewee model for the User entity.
"""

from peewee import AutoField, CharField

from app.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    """
    Represents a user entity in the database.
    """

    id = AutoField(primary_key=True)
    email = CharField(max_length=320, unique=True)
    password = CharField(max_length=255)
    name = CharField(max_length=255)
    lastname = CharField(max_length=255)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "users"

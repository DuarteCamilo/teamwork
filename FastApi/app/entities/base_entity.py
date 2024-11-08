"""
This module defines the base entity for Peewee models.
"""

from peewee import Model

from app.db import get_db


class BaseEntity(Model):
    """
    Represents a base entity for Peewee models.
    """

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = get_db()

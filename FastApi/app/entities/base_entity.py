from peewee import Model

from app.db import get_db


class BaseEntity(Model):
    """
    BaseEntity represents a base entity in the database.
    """

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = get_db()

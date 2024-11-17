from app.entities.base_entity import BaseEntity
from peewee import AutoField, CharField


class RoleEntity(BaseEntity):
    """
    RoleEntity represents a role entity in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=127)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "roles"

from app.entities.base_entity import BaseEntity
from app.entities.user_entity import UserEntity
from peewee import AutoField, CharField, DateField, ForeignKeyField, TimeField


class DentistEntity(BaseEntity):
    """
    DentistModel represents a dentist entity in the database.
    """

    id = AutoField(primary_key=True)
    license = CharField(max_length=255)
    workday_start_time = TimeField()
    workday_end_time = TimeField()
    inactivity_start_date = DateField(null=True)
    inactivity_end_date = DateField(null=True)
    user = ForeignKeyField(
        UserEntity, backref="dentists", unique=True, on_delete="CASCADE"
    )

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "dentists"

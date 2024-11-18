from peewee import AutoField, CharField, DateTimeField, ForeignKeyField, IntegerField

from app.entities.base_entity import BaseEntity
from app.entities.user_entity import UserEntity


class PatientEntity(BaseEntity):
    """
    PatientModel represents a patient entity in the database.
    """

    id = AutoField(primary_key=True)
    dni = IntegerField()
    address = CharField(max_length=255)
    admission_date = DateTimeField()
    user = ForeignKeyField(
        UserEntity, backref="patients", unique=True, on_delete="CASCADE"
    )

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "patients"

from peewee import AutoField, CharField, ForeignKeyField, BooleanField

from app.entities.base_entity import BaseEntity
from app.entities.patient_entity import PatientEntity
from app.entities.dentist_entity import DentistEntity


class UserEntity(BaseEntity):
    """
    UserEntity represents a user entity in the database.
    """

    id = AutoField(primary_key=True)
    email = CharField(max_length=320, unique=True)
    password = CharField(max_length=255)
    name = CharField(max_length=255)
    lastname = CharField(max_length=255)
    is_admin = BooleanField()
    patient = ForeignKeyField(PatientEntity, backref="users", null = True)
    dentist = ForeignKeyField(DentistEntity, backref="users", null = True)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "users"

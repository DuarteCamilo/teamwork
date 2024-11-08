"""
This module defines the Peewee model for the Appointment entity.
"""

from peewee import AutoField, DateField, ForeignKeyField

from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.entities.base_entity import BaseEntity
from app.entities.dentist_entity import DentistEntity
from app.entities.patient_entity import PatientEntity


class AppointmentEntity(BaseEntity):
    """
    Represents an Appointment entity in the database.
    """

    id = AutoField(primary_key=True)
    date = DateField()
    label = ForeignKeyField(
        model=AppointmentLabelEntity,
        backref="appointments",
        null=True,
        on_delete="SET NULL",
    )
    patient = ForeignKeyField(
        model=PatientEntity, backref="appointments", on_delete="CASCADE"
    )
    dentist = ForeignKeyField(
        model=DentistEntity, backref="appointments", on_delete="CASCADE"
    )

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "appointments"

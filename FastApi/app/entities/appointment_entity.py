from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.entities.base_entity import BaseEntity
from app.entities.dentist_entity import DentistEntity
from app.entities.patient_entity import PatientEntity
from peewee import AutoField, DateTimeField, ForeignKeyField, IntegerField


class AppointmentEntity(BaseEntity):
    """
    Appointment represents an Appointment entity in the database.
    """

    id = AutoField(primary_key=True)
    date = DateTimeField()
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

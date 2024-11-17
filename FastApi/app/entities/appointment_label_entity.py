from app.entities.base_entity import BaseEntity
from peewee import AutoField, CharField, TimeField


class AppointmentLabelEntity(BaseEntity):
    """
    AppointmentLabel represents a Label Appointment entity in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=127)
    duration = TimeField()

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "appointment_labels"

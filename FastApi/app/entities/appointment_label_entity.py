"""
This module defines the Peewee model for the AppointmentLabel entity.
"""

from peewee import AutoField, CharField, TimeField

from app.entities.base_entity import BaseEntity


class AppointmentLabelEntity(BaseEntity):
    """
    Represents a Label Appointment entity in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=127)
    duration = TimeField()

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        table_name = "appointment_labels"

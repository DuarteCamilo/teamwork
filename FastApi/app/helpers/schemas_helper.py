"""
This module contains helper functions for the schemas.
"""

from app.schemas.appointment import Appointment


def get_appointment_ids(values):
    """
    Set the appointment ids.
    """

    appointments: list[Appointment] = values.get("appointments", {})
    return {appointment.id for appointment in appointments}

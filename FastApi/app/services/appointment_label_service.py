"""
This module contains the service layer for the Appointment Label entity.
"""

from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.services.base_service import BaseService


class AppointmentLabelService(BaseService):
    """
    Provides CRUD operations for the Appointment Label entity.
    """

    def __init__(self):
        super().__init__(entity_name="Appointment Label", entity=AppointmentLabelEntity)


appointment_label_service = AppointmentLabelService()


def get_appointment_label_service():
    """
    Returns the AppointmentLabelService instance.
    """

    return appointment_label_service

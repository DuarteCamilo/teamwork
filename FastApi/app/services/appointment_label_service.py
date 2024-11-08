from app.entities.appointment_label_entity import AppointmentLabelEntity
from app.services.base_service import BaseService


class AppointmentLabelService(BaseService):
    def __init__(self):
        super().__init__(entity_name="Appointment Label", entity=AppointmentLabelEntity)


appointment_label_service = AppointmentLabelService()


def get_appointment_label_service():
    return appointment_label_service

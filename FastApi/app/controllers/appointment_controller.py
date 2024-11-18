from fastapi import Body, Path

from app.controllers.base_controller import BaseController
from app.schemas.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.services.appointment_service import get_appointment_service


class AppointmentController(BaseController):
    def __init__(self):
        super().__init__(get_appointment_service())

    def get_all(self) -> list[Appointment]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> Appointment:
        return super().get_by_id(_id)

    def create(self, model: AppointmentCreate = Body(...)) -> Appointment:
        return super().create(model)

    def update(
        self, _id: int = Path(..., alias="id"), model: AppointmentUpdate = Body(...)
    ) -> Appointment:
        return super().update(_id, model)


appointment_controller = AppointmentController()


def get_appointment_controller():
    return appointment_controller

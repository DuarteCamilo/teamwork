from app.controllers.base_controller import BaseController
from app.schemas.appointment_label import (
    AppointmentLabel,
    AppointmentLabelCreate,
    AppointmentLabelUpdate,
)
from app.services.appointment_label_service import get_appointment_label_service

from fastapi import Body, Path


class AppointmentLabelController(BaseController):
    def __init__(self):
        super().__init__(get_appointment_label_service())

    def get_all(self) -> list[AppointmentLabel]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> AppointmentLabel:
        return super().get_by_id(_id)

    def create(self, model: AppointmentLabelCreate = Body(...)) -> AppointmentLabel:
        return super().create(model)

    def update(
        self,
        _id: int = Path(..., alias="id"),
        model: AppointmentLabelUpdate = Body(...),
    ) -> AppointmentLabel:
        return super().update(_id, model)


appointment_label_controller = AppointmentLabelController()


def get_appointment_label_controller():
    return appointment_label_controller

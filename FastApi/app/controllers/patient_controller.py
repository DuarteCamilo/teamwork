from app.controllers.base_controller import BaseController
from app.schemas.patient import Patient, PatientCreate, PatientUpdate
from app.services.patient_service import get_patient_service

from fastapi import Body, Path


class PatientController(BaseController):
    def __init__(self):
        super().__init__(get_patient_service())

    def get_all(self) -> list[Patient]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> Patient:
        return super().get_by_id(_id)

    def create(self, model: PatientCreate = Body(...)) -> Patient:
        return super().create(model)

    def update(
        self, _id: int = Path(..., alias="id"), model: PatientUpdate = Body(...)
    ) -> Patient:
        return super().update(_id, model)


patient_controller = PatientController()


def get_patient_controller():
    return patient_controller

from fastapi import Body, Path

from app.controllers.base_controller import BaseController
from app.schemas.dentist import Dentist, DentistCreate, DentistUpdate
from app.services.dentist_service import get_dentist_service


class DentistController(BaseController):
    def __init__(self):
        super().__init__(get_dentist_service())

    def get_all(self) -> list[Dentist]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> Dentist:
        return super().get_by_id(_id)

    def create(self, model: DentistCreate = Body(...)) -> Dentist:
        return super().create(model)

    def update(
        self, _id: int = Path(..., alias="id"), model: DentistUpdate = Body(...)
    ) -> Dentist:
        return super().update(_id, model)


dentist_controller = DentistController()


def get_dentist_controller():
    return dentist_controller

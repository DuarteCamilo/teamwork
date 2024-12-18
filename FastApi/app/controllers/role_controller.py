from app.controllers.base_controller import BaseController
from app.schemas.role import Role, RoleCreate, RoleUpdate
from app.services.role_service import get_role_service

from fastapi import Body, Path


class RoleController(BaseController):
    def __init__(self):
        super().__init__(get_role_service())

    def get_all(self) -> list[Role]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> Role:
        return super().get_by_id(_id)

    def create(self, model: RoleCreate = Body(...)) -> Role:
        return super().create(model)

    def update(
        self,
        _id: int = Path(..., alias="id"),
        model: RoleUpdate = Body(...),
    ) -> Role:
        return super().update(_id, model)


role_controller = RoleController()


def get_role_controller():
    return role_controller

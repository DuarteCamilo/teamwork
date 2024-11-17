from app.controllers.base_controller import BaseController
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import get_user_service

from fastapi import Body, Path


class UserController(BaseController):
    def __init__(self):
        super().__init__(get_user_service())

    def get_all(self) -> list[User]:
        return super().get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> User:
        return super().get_by_id(_id)

    def create(self, model: UserCreate = Body(...)) -> User:
        return super().create(model)

    def update(
        self, _id: int = Path(..., alias="id"), model: UserUpdate = Body(...)
    ) -> User:
        return super().update(_id, model)


user_controller = UserController()


def get_user_controller():
    return user_controller

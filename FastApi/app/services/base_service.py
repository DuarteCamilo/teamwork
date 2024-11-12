from app.models.message import MessageResponse
from peewee import Model
from pydantic import BaseModel

from fastapi import HTTPException


class BaseService:
    """
    A generic service that provides standard CRUD operations for a database entity.
    Args:
        entity (Model): A Peewee model that represents the database entity.
    """

    def __init__(self, entity_name: str, entity: Model):
        self.name = entity_name
        self.entity = entity

    def get_all(self) -> list[Model]:
        return list(self.entity.select())

    def get_by_id(self, _id: int) -> Model:
        existing_entity = self.entity.get_or_none(self.entity.id == _id)

        if existing_entity is None:
            raise HTTPException(
                status_code=404, detail=f"{self.name} with id {_id} not found"
            )

        return existing_entity

    def create(self, model: BaseModel) -> Model:
        return self.entity.create(**model.model_dump())

    def update(self, _id, model: BaseModel) -> Model:
        self.entity.update(
            **model.model_dump(
                exclude_defaults=True, exclude_unset=True, exclude_none=True
            )
        ).where(self.entity.id == _id).execute()

        return self.get_by_id(_id)

    def delete(self, id: int) -> MessageResponse:
        self.get_by_id(id).delete_instance()

        return MessageResponse(message=f"{self.name} successfully deleted")

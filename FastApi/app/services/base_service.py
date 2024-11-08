"""
This module contains a generic service that provides standard CRUD operations for a database entity.
"""

from fastapi import HTTPException
from peewee import Model
from pydantic import BaseModel

from app.models.message import MessageResponse


class BaseService:
    """
    A generic service that provides standard CRUD operations for a database entity.
    """

    def __init__(self, entity_name: str, entity: Model):
        self.name = entity_name
        self.entity = entity

    def get_all(self) -> list[Model]:
        """
        Returns all entities.
        """

        return list(self.entity.select())

    def get_by_id(self, _id: int) -> Model:
        """
        Returns an entity by its id.
        """

        existing_entity = self.entity.get_or_none(self.entity.id == _id)

        if existing_entity is None:
            raise HTTPException(
                status_code=404, detail=f"{self.name} with id {_id} not found"
            )

        return existing_entity

    def create(self, model: BaseModel) -> Model:
        """
        Creates a new entity.
        """

        return self.entity.create(**model.model_dump())

    def update(self, _id, model: BaseModel) -> Model:
        """
        Updates an existing entity by its id ignoring default, unset, and None values.
        """

        self.entity.update(
            **model.model_dump(
                exclude_defaults=True, exclude_unset=True, exclude_none=True
            )
        ).where(self.entity.id == _id).execute()

        return self.get_by_id(_id)

    def delete(self, _id: int) -> MessageResponse:
        """
        Deletes an entity by its id.
        """

        self.get_by_id(_id).delete_instance()
        return MessageResponse(message=f"{self.name} successfully deleted")

"""
This module contains a generic controller that provides standard CRUD routes for a FastAPI application.
"""

from typing import List

from fastapi import APIRouter, Body, Path
from pydantic import BaseModel

from app.services.base_service import BaseService


class BaseController:
    """
    A generic controller that provides standard CRUD routes for a FastAPI application.

    Args:
        service (BaseService): A service that provides CRUD operations for the entity.
    """

    def __init__(self, service: BaseService):
        self.router = APIRouter()
        self.service = service

        self.router.add_api_route("/", self.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_by_id, methods=["GET"])
        self.router.add_api_route("/", self.create, methods=["POST"])
        self.router.add_api_route("/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete, methods=["DELETE"])

    def get_router(self) -> APIRouter:
        """
        Returns the router for the controller.
        """

        return self.router

    def get_all(self) -> List[BaseModel]:
        """
        Returns all entities.
        """

        return self.service.get_all()

    def get_by_id(self, _id: int = Path(..., alias="id")) -> BaseModel:
        """
        Returns an entity by its ID.
        """

        return self.service.get_by_id(_id)

    def create(self, model: BaseModel = Body(...)) -> BaseModel:
        """
        Creates a new entity.
        """

        return self.service.create(model)

    def update(
        self, _id: int = Path(..., alias="id"), model: BaseModel = Body(...)
    ) -> BaseModel:
        """
        Updates an entity by its ID
        """

        return self.service.update(_id, model)

    def delete(self, _id: int = Path(..., alias="id")):
        """
        Deletes an entity by its ID.
        """

        return self.service.delete(_id)

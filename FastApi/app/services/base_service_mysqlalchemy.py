# from fastapi import HTTPException
# from pydantic import BaseModel
# from sqlalchemy.orm import Session

# from app.models.message import MessageResponse


# class BaseService:
#     """
#     A generic service that provides standard CRUD operations for a database entity.

#     Args:
#         entity (Base): An SQLAlchemy model that represents the database entity.
#         db_session (Session): An active SQLAlchemy session.
#     """

#     def __init__(self, name: str, entity, db_session: Session):
#         self.name = name
#         self.entity = entity
#         self.db_session = db_session

#     def get_all(self) -> list:
#         """Retrieve all records of the entity."""
#         return self.db_session.query(self.entity).all()

#     def get_by_id(self, _id: int):
#         """Retrieve a single record by its ID."""
#         existing_entity = self.db_session.query(self.entity).get(_id)

#         if existing_entity is None:
#             raise HTTPException(
#                 status_code=404, detail=f"{self.name} with id {_id} not found"
#             )

#         return existing_entity

#     def create(self, model: BaseModel):
#         """Create a new record using the data from the provided Pydantic model."""
#         new_entity = self.entity(**model.model_dump())
#         self.db_session.add(new_entity)
#         self.db_session.commit()
#         self.db_session.refresh(new_entity)
#         return new_entity

#     def update(self, _id: int, model: BaseModel):
#         """Update an existing record by its ID with the provided data."""
#         existing_entity = self.get_by_id(_id)

#         for key, value in model.model_dump(
#             exclude_unset=True, exclude_defaults=True
#         ).items():
#             setattr(existing_entity, key, value)

#         self.db_session.commit()
#         return existing_entity

#     def delete(self, _id: int) -> MessageResponse:
#         """Delete a record by its ID."""
#         existing_entity = self.get_by_id(_id)
#         self.db_session.delete(existing_entity)
#         self.db_session.commit()

#         return MessageResponse(message=f"{self.name} successfully deleted")

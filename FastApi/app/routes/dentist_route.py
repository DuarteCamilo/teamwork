"""
This module defines the API routes for managing dentists in the application.
Routes:
    - POST /dentists/: Create a new dentist.
    - GET /dentists: Retrieve a list of dentists.
    - GET /dentists/{dentist_id}: Retrieve a dentist by their ID.
    - PUT /dentists/{dentist_id}: Update a dentist by their ID.
    - DELETE /dentists/{dentist_id}: Delete a dentist by their ID.
Dependencies:
    - config.database.DentistModel: The database model for dentists.
    - schemas.dentist.DentistCreate: Schema for creating a dentist.
    - schemas.dentist.DentistUpdate: Schema for updating a dentist.
    - peewee.IntegrityError: Exception raised for database integrity errors.
    - fastapi.APIRouter: FastAPI router for defining routes.
    - fastapi.Body: FastAPI dependency for request body parameters.
"""

# pylint: disable=import-error
from schemas.dentist import DentistCreate, DentistUpdate
from services import dentist_service

# pylint: enable=import-error

from peewee import IntegrityError
from fastapi import APIRouter, Body

dentist_route = APIRouter()


@dentist_route.post("/dentists/")
def create_dentists(dentist: DentistCreate = Body(...)):
    """
    Create a new dentist.
    Args:
        dentist (Dentist): The dentist object containing the dentistname, color, and age.
    Returns:
        None
    """
    return dentist_service.create_dentists(dentist)

@dentist_route.get("/dentists")
def get_dentists():
    """
    Retrieve a list of dentists from the database.

    This function queries the DentistModel to select all dentists with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a dentist.
    """
    return dentist_service.get_dentists()

@dentist_route.get("/dentists/{dentist_id}")
def get_dentist(dentist_id: int):
    """
    Retrieve a dentist by their ID.
    Args:
        dentist_id (int): The ID of the dentist to retrieve.
    Returns:
        DentistModel: The dentist object if found.
        dict: An error message if the dentist is not found.
    """
    return dentist_service.get_dentist(dentist_id)


@dentist_route.put("/dentists/{dentist_id}")
def update_dentist(dentist_id: int, dentist: DentistUpdate = Body(...)):
    """
    Update a dentist by their ID.
    Args:
        dentist_id (int): The ID of the dentist to update.
        dentist (Dentist): The updated dentist object containing the dentistname, color, and age.
    Returns:
        None
    """
    return dentist_service.update_dentist(dentist_id, dentist)
    
@dentist_route.delete("/dentists/{dentist_id}")
def delete_dentist(dentist_id: int):
    """
    Delete a dentist by their ID.
    Args:
        dentist_id (int): The ID of the dentist to delete.
    Returns:
        None
    """
    return dentist_service.delete_dentist(dentist_id)

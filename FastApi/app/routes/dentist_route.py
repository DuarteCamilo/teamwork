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
from config.database import DentistModel
from schemas.dentist import DentistCreate, DentistUpdate

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
    try:
        DentistModel.create(
            name=dentist.name,
            last_name=dentist.last_name,
            license=dentist.license,
            id_state=dentist.id_state,
            inactive_days=dentist.inactive_days,
            id_user=dentist.id_user,
            id_schedule=dentist.id_schedule,
        )
        return {"message": "Dentist created successfully"}
    except IntegrityError:
        return {"error": "Dentist already exists"}


@dentist_route.get("/dentists")
def get_dentists():
    """
    Retrieve a list of dentists from the database.

    This function queries the DentistModel to select all dentists with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a dentist.
    """
    dentist = DentistModel.select().where(DentistModel.id_dentist > 0).dicts()
    return list(dentist)


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
    print(dentist_id)
    try:
        dentist = DentistModel.get(DentistModel.id_dentist == dentist_id)
        return dentist
    except DentistModel.DoesNotExist:
        return {"error": "Dentist not found"}


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
    try:
        DentistModel.update(
            name=dentist.name,
            last_name=dentist.last_name,
            license=dentist.license,
            id_state=dentist.id_state,
            inactive_days=dentist.inactive_days,
            id_user=dentist.id_user,
            id_schedule=dentist.id_schedule,
        ).where(DentistModel.id_dentist == dentist_id).execute()
        return {"message": "Dentist updated successfully"}
    except DentistModel.DoesNotExist:
        return {"error": "Dentist not found"}


@dentist_route.delete("/dentists/{dentist_id}")
def delete_dentist(dentist_id: int):
    """
    Delete a dentist by their ID.

    Args:
        dentist_id (int): The ID of the dentist to delete.

    Returns:
        None
    """
    try:
        DentistModel.delete().where(DentistModel.id_dentist == dentist_id).execute()
        return {"message": "Dentist deleted successfully"}
    except DentistModel.DoesNotExist:
        return {"error": "Dentist not found"}

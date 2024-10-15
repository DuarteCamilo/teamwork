"""
This module defines the routes for dentist-related operations in the FastAPI applidentistion.
Routes:
    - POST /dentists/: Create a new dentist.
    - GET /dentists: Retrieve a list of all dentists.
    - GET /dentists/{dentist_id}: Retrieve a specific dentist by their ID.
    - PUT /dentists/{dentist_id}: Update a specific dentist by their ID.
    - DELETE /dentists/{dentist_id}: Delete a specific dentist by their ID.
Functions:
    - create_dentists(dentist: Dentist): Creates a new dentist with the provided details.
    - get_dentists(): Retrieves a list of all dentists from the database.
    - get_dentist(dentist_id: int): Retrieves a specific dentist by their ID. 
      Returns an error message if the dentist is not found.
    - update_dentist(dentist_id: int, dentist: Dentist): Updates a specific dentist by their ID.
    - delete_dentist(dentist_id: int): Deletes a specific dentist by their ID.
Dependencies:
    - DentistModel: The database model for dentists.
    - Dentist: The Pydantic model for dentist data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

# pylint: disable=import-error
from config.database import DentistModel
from schemas.dentist import Dentist

# pylint: enable=import-error

from peewee import IntegrityError
from fastapi import APIRouter, Body

dentist_route = APIRouter()


@dentist_route.post("/dentists/")
def create_dentists(dentist: Dentist = Body(...)):
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
            license=dentist.licence,
            id_status=dentist.id_status,
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
def update_dentist(dentist_id: int, dentist: Dentist = Body(...)):
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
            license=dentist.licence,
            id_status=dentist.id_status,
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

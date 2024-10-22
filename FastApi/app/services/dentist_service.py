from config.database import DentistModel
from schemas.dentist import DentistCreate, DentistUpdate 

from peewee import IntegrityError
from fastapi import Body

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

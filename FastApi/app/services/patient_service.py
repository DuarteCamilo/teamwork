"""
This module provides services for managing patients in the FastAPI application.
Functions:
  create_patient(patient: PatientCreate = Body(...)):
  get_patients():
  get_patient(patient_id: int):
  update_patient(patient_id: int, patient: PatientUpdate = Body(...)):
  delete_patient(patient_id: int):
"""

from config.database import PatientModel
from schemas.patient import PatientCreate, PatientUpdate

from peewee import IntegrityError
from fastapi import Body


def create_patient(patient: PatientCreate = Body(...)):
    """
    Create a new patient.

    Args:
        patient (Patient): The patient object containing the necessary details.

    Returns:
        dict: Success or error message.
    """
    try:
        PatientModel.create(
            name=patient.name,
            last_name=patient.last_name,
            address=patient.address,
            departure_date=patient.departure_date,
            id_user=patient.id_user,
            dni=patient.dni,
        )
        return {"message": "Patient created successfully"}
    except IntegrityError:
        return {"error": "Patient already exists"}


def get_patients():
    """
    Retrieve a list of patients from the database.

    This function queries the PatientModel to select all patients with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a patient.
    """
    patients = PatientModel.select().where(PatientModel.id_patient > 0).dicts()
    return list(patients)


def get_patient(patient_id: int):
    """
    Retrieve a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to retrieve.

    Returns:
        PatientModel: The patient object if found.
        dict: An error message if the patient is not found.
    """
    try:
        patient = PatientModel.get(PatientModel.id_patient == patient_id)
        return patient
    except PatientModel.DoesNotExist:
        return {"error": "Patient not found"}


def update_patient(patient_id: int, patient: PatientUpdate = Body(...)):
    """
    Update a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to update.
        patient (Patient): The updated patient object with new details.

    Returns:
        dict: Success or error message.
    """
    try:
        PatientModel.update(
            name=patient.name,
            last_name=patient.last_name,
            address=patient.address,
            departure_date=patient.departure_date,
            dni=patient.dni,
        ).where(PatientModel.id_patient == patient_id).execute()
        return {"message": "Patient updated successfully"}
    except PatientModel.DoesNotExist:
        return {"error": "Patient not found"}


def delete_patient(patient_id: int):
    """
    Delete a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to delete.

    Returns:
        dict: Success or error message.
    """
    try:
        PatientModel.delete().where(PatientModel.id_patient == patient_id).execute()
        return {"message": "Patient deleted successfully"}
    except PatientModel.DoesNotExist:
        return {"error": "Patient not found"}
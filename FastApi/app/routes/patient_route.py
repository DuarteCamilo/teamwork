"""
This module defines the routes for patient-related operations in the FastAPI application.
Routes:
    - POST /patients/: Create a new patient.
    - GET /patients/: Retrieve a list of patients.
    - GET /patients/{patient_id}: Retrieve a patient by their ID.
    - PUT /patients/{patient_id}: Update a patient by their ID.
    - DELETE /patients/{patient_id}: Delete a patient by their ID.
Each route corresponds to a function in the patient_service module that handles the actual
logic for creating, retrieving, updating, and deleting patients.
Modules:
    - schemas.patient: Contains the PatientCreate and PatientUpdate schemas.
    - services.patient_service: Contains the service functions for patient operations.
    - fastapi: FastAPI framework for building APIs.
Attributes:
    patient_route (APIRouter): The router object for patient-related routes.
"""

# pylint: disable=import-error
from schemas.patient import PatientCreate, PatientUpdate
from services import patient_service

# pylint: enable=import-error

from fastapi import APIRouter, Body

patient_route = APIRouter()


@patient_route.post("/patients/")
def create_patient(patient: PatientCreate = Body(...)):
    """
    Create a new patient.

    Args:
        patient (Patient): The patient object containing the necessary details.

    Returns:
        dict: Success or error message.
    """
    return patient_service.create_patient(patient)


@patient_route.get("/patients/")
def get_patients():
    """
    Retrieve a list of patients from the database.

    This function queries the PatientModel to select all patients with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a patient.
    """
    return patient_service.get_patients()


@patient_route.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    """
    Retrieve a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to retrieve.

    Returns:
        PatientModel: The patient object if found.
        dict: An error message if the patient is not found.
    """
    return patient_service.get_patient(patient_id)


@patient_route.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient: PatientUpdate = Body(...)):
    """
    Update a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to update.
        patient (Patient): The updated patient object with new details.

    Returns:
        dict: Success or error message.
    """
    return patient_service.update_patient(patient_id, patient)


@patient_route.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    """
    Delete a patient by their ID.

    Args:
        patient_id (int): The ID of the patient to delete.

    Returns:
        dict: Success or error message.
    """
    return patient_service.delete_patient(patient_id)

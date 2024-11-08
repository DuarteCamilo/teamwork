"""
This module defines the routes for label appointments in the FastAPI application.
Routes:
    POST /: Create a new label appointment.
    GET /: Retrieve all label appointments.
    GET /{_id}: Retrieve a label appointment by its ID.
    PUT /{_id}: Update a label appointment by its ID.
    DELETE /{_id}: Delete a label appointment by its ID.
"""

from fastapi import APIRouter, Body

from app.schemas.label_appointment import (
    LabelAppointment,
    LabelAppointmentCreate,
    LabelAppointmentUpdate,
)
from app.services import label_appointment_service

label_appointment_route = APIRouter()


def get_label_appointment_route():
    """
    Retrieves the label appointment route.
    Returns:
        The label appointment route.
    """

    return label_appointment_route


@label_appointment_route.get("/")
def get_label_appointments() -> list[LabelAppointment]:
    """
    Retrieve all label appointments.
    Returns:
        list: A list of label appointments.
    """

    return label_appointment_service.get_label_appointments()


@label_appointment_route.get("/{_id}")
def get_label_appointment(_id: int) -> LabelAppointment:
    """
    Retrieve a label appointment by its ID.
    Args:
        _id (int): The ID of the label appointment to retrieve.
    Returns:
        The label appointment object corresponding to the given ID.
    """

    return label_appointment_service.get_label_appointment(_id)


@label_appointment_route.post("/")
def create_label_appointment(
    label_apoointment: LabelAppointmentCreate = Body(...),
) -> LabelAppointment:
    """
    Create a new label appointment.
    Args:
        label_appointment (LabelAppointmentCreate): The label appointment data to be created.
    Returns:
        The created label appointment.
    """

    return label_appointment_service.create_label_appointment(label_apoointment)


@label_appointment_route.put("/{_id}")
def update_label_appointment(
    _id: int, label: LabelAppointmentUpdate = Body(...)
) -> LabelAppointment:
    """
    Update an existing label appointment by its ID.
    Args:
        _id (int): The unique identifier of the label appointment to be updated.
        label (LabelAppointmentUpdate): The new data for the label appointment.
    Returns:
        The updated label appointment.
    """

    return label_appointment_service.update_label_appointment(_id, label)


@label_appointment_route.delete("/{_id}")
def delete_label_appointment(_id: int):
    """
    Delete a label appointment by its ID.
    Args:
        _id (int): The ID of the label appointment to delete.
    Returns:
        The result of the delete operation from the label_appointment_service.
    """

    return label_appointment_service.delete_label_appointment(_id)

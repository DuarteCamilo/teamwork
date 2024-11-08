# """
# This module provides services for managing label appointments in the FastAPI application.
# """

# from fastapi import HTTPException

# from app.entities.label_appointment_entity import LabelAppointmentEntity
# from app.models.message import MessageResponse
# from app.schemas.label_appointment import LabelAppointmentCreate, LabelAppointmentUpdate


# def get_label_appointments() -> list[LabelAppointmentEntity]:
#     """
#     Retrieve all label appointment entities.
#     Returns:
#         list[LabelAppointmentEntity]: A list of label appointment entities.
#     """

#     return list(LabelAppointmentEntity.select())


# def get_label_appointment(_id: int) -> LabelAppointmentEntity:
#     """
#     Retrieve a label appointment by its ID.
#     Args:
#         _id (int): The ID of the label appointment to retrieve.
#     Returns:
#         LabelAppointmentEntity: The label appointment corresponding to the given ID.
#     """

#     label_appointment = LabelAppointmentEntity.get_or_none(
#         LabelAppointmentEntity.id == _id
#     )

#     if label_appointment is None:
#         raise HTTPException(status_code=404, detail="label appointment not found")

#     return label_appointment


# def create_label_appointment(
#     label_appointment: LabelAppointmentCreate,
# ) -> LabelAppointmentEntity:
#     """
#     Creates a new label appointment.
#     Args:
#         label_appointment (LabelAppointmentCreate): The label appointment data to be created.
#     Returns:
#         LabelAppointmentEntity: The newly created label appointment.
#     Raises:
#         ValueError: If there is an integrity error while creating the label appointment.
#     """

#     new_label = LabelAppointmentEntity.create(**label_appointment.model_dump())
#     return new_label


# def update_label_appointment(
#     _id: int, label_appointment: LabelAppointmentUpdate
# ) -> LabelAppointmentEntity:
#     """
#     Updates a label appointment with the given ID using the provided label_appointment data.
#     Args:
#         _id (int): The ID of the label appointment to update.
#         label_appointment (LabelAppointmentUpdate): An instance containing the updated label_appointment data.
#     Returns:
#         LabelAppointmentEntity: The updated label appointment.
#     """

#     LabelAppointmentEntity.update(
#         **label_appointment.model_dump(exclude_unset=True)
#     ).where(LabelAppointmentEntity.id == _id).execute()

#     return get_label_appointment(_id)


# def delete_label_appointment(_id: int) -> MessageResponse:
#     """
#     Deletes a label appointment from the database based on the provided label_appointment ID.
#     Args:
#         _id (int): The ID of the label appointment to be deleted.
#     Returns:
#         None
#     """

#     get_label_appointment(_id).delete_instance()

#     return MessageResponse(message="label appointment deleted")

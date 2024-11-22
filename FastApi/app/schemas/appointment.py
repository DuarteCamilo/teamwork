from datetime import datetime

from app.schemas.base_schema import BaseSchema


class Appointment(BaseSchema):
    """
    Schema for an appointment.
    Attributes:
      id (int): The unique identifier for the appointment.
      date (date): The date of the appointment.
      label_id (int): The label ID associated with the appointment
      patient_id (int): The patient ID associated with the appointment.
      dentist_id (int): The dentist ID associated with the appointment.
    """

    id: int = None
    date: datetime = None
    label_id: int = None
    patient_id: int = None
    dentist_id: int = None


class AppointmentCreate(BaseSchema):
    """
    Schema for creating a new appointment.
    Attributes:
      date (str): The date of the appointment.
      label_id (int): The label ID associated with the appointment
      patient_id (int): The patient ID associated with the appointment.
      dentist_id (int): The dentist ID associated with the appointment.
    """

    date: datetime
    label_id: int
    patient_id: int
    dentist_id: int

    # @field_validator('date')
    # def check_date(self, v):
    #     if v < dt_date.today():
    #         raise ValueError('Date cannot be in the past')
    #     return v


class AppointmentUpdate(BaseSchema):
    """
    Schema for updating an appointment.
    Attributes:
      date (date): The date of the appointment.
      label_id (int): The label ID associated with the appointment
      patient_id (int): The patient ID associated with the appointment.
      dentist_id (int): The dentist ID associated with the appointment.
    """

    date: datetime = None
    label_id: int = None
    patient_id: int = None
    dentist_id: int = None

"""
This module sets up the database connection and defines the DentistModel.
"""

from peewee import Model, MySQLDatabase, AutoField, CharField, IntegerField, DateField,ForeignKeyField, TimeField, DateTimeField
from config.settings import DATABASE

from datetime import datetime 
import pytz

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

Colombian = pytz.timezone('America/Bogota')

class RoleModel(Model):
    """
    RoleModel represents a role entity in the database.
    """
    id_role = IntegerField()
    name = CharField(max_length=40)
    description = CharField(max_length=100)

    class Meta:
        """
        Meta class for configuring the database settings.
        """
        database = database
        table_name = "roles"

class UserModel(Model):
    """
    UserModel represents a user entity in the database.
    """
    
    id_user = AutoField(primary_key=True)
    email = CharField(max_length=200, unique=True)
    password = CharField(max_length=200)
    id_role = ForeignKeyField(RoleModel, backref='user')

    class Meta:
        """
        Meta class for configuring the database settings.
        """
        database = database
        table_name = "users"

class ScheduleDentistModel(Model):
    """
    ScheduleDentistModel represents a schedule entity in the database.
    """
    
    id_schedule = AutoField(primary_key=True)
    day_start_time = DateTimeField(
        default=lambda: datetime.now(pytz.timezone(Colombian)))
    end_time_day = DateTimeField(
        default=lambda: datetime.now(pytz.timezone(Colombian)))

    class Meta:
        """
        Meta class for configuring the database settings.
        """
        database = database
        table_name = "Schedule"

class StateDentistModel(Model):
    id_state = AutoField(primary_key=True)
    name = CharField(max_length=40)
    description = CharField(max_length=100)

    class Meta:
        """
        Meta class for configuring the database settings.
        """       
        database = database
        table_name = "states"

class DentistModel(Model):
    """
    DentistModel represents a dentist entity in the database.
    """

    id_dentist = AutoField(primary_key=True)
    name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    license = CharField(max_length=40)
    id_state = ForeignKeyField(StateDentistModel, backref='dentist')
    inactive_days = IntegerField(null=True)
    id_user = ForeignKeyField(UserModel, backref='dentist')
    id_schedule = ForeignKeyField(ScheduleDentistModel, backref='dentist')

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = database
        table_name = "dentists"


class PatientModel(Model):
    """
    PatientModel represents a patient entity in the database.
    """

    id_patient = AutoField(primary_key=True)
    name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    address = CharField(max_length=100)
    departure_date = DateField(null=True)
    id_user = ForeignKeyField(UserModel, backref='patient')
    dni = IntegerField(null=True)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = database
        table_name = "patients"



class labelAppointmentModel(Model):
    """
    labelAppointment represents a labelAppointment entity in the database.
    """
    id_label = AutoField(primary_key=True)
    name = CharField(max_length=100)
    hour = IntegerField(null=True)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = database
        table_name = "labelAppointment"


class AppointmentModel(Model):
    """
    Appointment represents a Appointment entity in the database.
    """
    id_appointment = AutoField(primary_key=True)
    date = DateField(null=True)
    hour = IntegerField(null=True)
    id_label = ForeignKeyField(labelAppointmentModel, backref='appoinment')
    id_patient = ForeignKeyField(PatientModel, backref='appoinment')
    id_dentist = ForeignKeyField(DentistModel, backref='appoinment')

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = database
        table_name = "appoinments"
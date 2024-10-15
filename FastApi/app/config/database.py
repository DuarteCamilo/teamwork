"""
This module sets up the database connection and defines the DentistModel.
"""

from peewee import Model, MySQLDatabase, AutoField, CharField, IntegerField
from config.settings import DATABASE

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class DentistModel(Model):
    """
    DentistModel represents a dentist entity in the database.
    """

    id_dentist = AutoField(primary_key=True)
    name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    licence = CharField(max_length=40)
    id_state = IntegerField(null=True)
    inactive_days = IntegerField(null=True)
    id_user = IntegerField(null=True)
    id_schedule = IntegerField(null=True)

    class Meta:
        """
        Meta class for configuring the database settings.
        """

        database = database
        table_name = "dentists"

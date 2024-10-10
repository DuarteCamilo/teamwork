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
    id_odontologo = AutoField(primary_key=True)
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    matricula = CharField(max_length=40)
    id_estado = IntegerField(null=True)
    dias_inactividad = IntegerField(null=True)
    id_usuario = IntegerField(null=True)
    id_horario = IntegerField(null=True)
    
    class Meta:
        database = database
        table_name = "dentists"
"""
This module defines the Pydantic model for a dentist.
"""

from pydantic import BaseModel, Field


class Dentist(BaseModel):
    """
    Dentist schema for FastAPI application.
    Attributes:
      id_odontologo (int): Unique identifier for the dentist, aliased as "Id_odontologo".
      nombre (str): First name of the dentist, with a maximum length of 40 characters.
      apellido (str): Last name of the dentist, with a maximum length of 40 characters.
      matricula (str): Registration number of the dentist, with a maximum length of 40 characters.
      id_estado (int): Identifier for the state, aliased as "id_estado".
      dias_inactividad (int): Number of inactive days, aliased as "dias_inactividad".
      id_usuario (int): User identifier, aliased as "id_usuario".
      id_horario (int): Schedule identifier, aliased as "id_horario".
    Config:
      orm_mode (bool): Enables ORM mode for compatibility with ORMs.
    """

    id_odontologo: int = Field(..., alias="Id_odontologo")
    nombre: str = Field(..., max_length=40)
    apellido: str = Field(..., max_length=40)
    matricula: str = Field(..., max_length=40)
    id_estado: int = Field(..., alias="id_estado")
    dias_inactividad: int = Field(..., alias="dias_inactividad")
    id_usuario: int = Field(..., alias="id_usuario")
    id_horario: int = Field(..., alias="id_horario")

    class Config:
        orm_mode = True

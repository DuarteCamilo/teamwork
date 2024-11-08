"""
This module defines the base schema for Pydantic models.
"""

from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base model for Pydantic models in the FastAPI application.
    """

    class Config:
        """
        Configuration class for Pydantic models.
        """

        orm_mode = True

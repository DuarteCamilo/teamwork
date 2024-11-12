from datetime import date, datetime, time

from app.helpers.format_helper import date_to_str, datetime_to_str, time_to_str
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

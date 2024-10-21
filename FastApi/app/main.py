"""
This module defines the main entry point for the FastAPI application and manages its lifespan.
"""

from contextlib import asynccontextmanager
from starlette.responses import RedirectResponse
from config.database import database as connection

from routes.dentist_route import dentist_route
from routes.patient_route import patient_route

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.
    This function ensures that the database connection is open when the application starts
    and closes it when the application shuts down.
    """

    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan, title="Microservice for Adios Caries")


@app.get("/", include_in_schema=False)
def read_root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """
    return RedirectResponse(url="/docs")


# ------------- Dentist Routes -------------
app.include_router(
    dentist_route,
    prefix="/api",
    tags=["Dentists"],
)

# ------------- Patient Routes -------------
app.include_router(
    patient_route,
    prefix="/api",
    tags=["Patients"],
)

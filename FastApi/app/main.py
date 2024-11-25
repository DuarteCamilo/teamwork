# Don't remove peeweedbevolve import, it's necessary for migrations to work!

from contextlib import asynccontextmanager

import peeweedbevolve
from app.controllers.appointment_controller import get_appointment_controller
from app.controllers.appointment_label_controller import (
    get_appointment_label_controller,
)
from app.controllers.dentist_controller import get_dentist_controller
from app.controllers.patient_controller import get_patient_controller
from app.controllers.role_controller import get_role_controller
from app.controllers.user_controller import get_user_controller
from app.db import get_db
from app.entities.base_entity import BaseEntity
from app.helpers.migration_helper import get_entity_modules, get_entity_table_names
from app.routes.login_route import get_login_router
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

from fastapi import FastAPI, Request

db = get_db()
app = FastAPI(title="Adios Caries API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(_: Request, exc: RequestValidationError):
    messages = [f'{error["loc"][1]}: {error["msg"]}' for error in exc.errors()]
    response_content = messages[0] if len(messages) == 1 else messages
    return JSONResponse(status_code=422, content={"detail": response_content})


@asynccontextmanager
async def lifespan_wrapper(_: FastAPI):
    ignored_entities = {BaseEntity}
    ignored_entity_table_names = get_entity_table_names(ignored_entities)

    get_entity_modules()
    db.evolve(interactive=False, ignore_tables=ignored_entity_table_names)

    yield

    db.close()


app.router.lifespan_context = lifespan_wrapper


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


app.include_router(
    get_login_router(),
    prefix="/login",
    tags=["Login"],
)

app.include_router(
    get_user_controller().get_router(),
    prefix="/users",
    tags=["Users"],
)

app.include_router(
    get_patient_controller().get_router(),
    prefix="/patients",
    tags=["Patients"],
)

app.include_router(
    get_dentist_controller().get_router(),
    prefix="/dentists",
    tags=["Dentists"],
)

app.include_router(
    get_appointment_controller().get_router(),
    prefix="/appointments",
    tags=["Appointments"],
)

app.include_router(
    get_appointment_label_controller().get_router(),
    prefix="/appointment_labels",
    tags=["Appointment Labels"],
)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8080)

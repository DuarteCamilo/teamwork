# Adios Caries

This project is a **Management system for a dental clinic** built with FastAPI and Peewee as the ORM.

## Requirements

Make sure you have installed:

- **Docker**
- **Docker Compose**

## Running the Project Locally

To build and start the project locally, follow these steps.

**Build and Start the Containers**

Run the following command from the project root directory:

```bash
docker compose up --build
```

> [!NOTE]
>
> alternatively you can run the project with this command
>
> ```bash
> docker-compose up --build
> ```

This command will build Docker images (if running for the first time) and start the application and database services defined in `docker-compose.yaml`.

## Main Endpoints

These are the main endpoints of the API and their functionalities:

- **Users** (`/users`): User management.
- **Patients** (`/patients`): Patient profile management.
- **Dentists** (`/dentists`): Dentist information management.
- **Appointments** (`/appointments`): Appointment scheduling and management.
- **Appointment Labels** (`/appointment_labels`): Appointment categorization by label.


Each of these endpoints allows CRUD operations (Create, Read, Update, Delete).

## Contributions

To contribute to the project:

1. Fork the repository.
2. Create a branch for your feature.
3. Commit your changes.
4. Open a pull request to dev branch.

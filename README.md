# Django Event Project

This is a simple Django project that allows users to create and manage events.

## Installation

To install the project, run the following command:

```bash
docker-compose build
docker-compose up
```

## Usage

You should create a superuser and login to the admin panel to create and manage events.

You can do this with the following command:

```bash
docker compose exec api python manage.py createsuperuser
```

And you will need to run migrations:

```bash
docker compose exec api python manage.py migrate
```

The admin panel is available at http://localhost:8080/admin/

The API is available at http://localhost:8080/api

The docs are available at http://localhost:8080/docs

## License

This project is licensed under the MIT License.

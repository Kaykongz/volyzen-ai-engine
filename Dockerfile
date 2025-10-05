Use the official Python slim image as a parent image
FROM python:3.11-slim-bookworm
Set the working directory in the container
WORKDIR /app
Set environment variables to prevent Python from writing .pyc files
and to buffer output
ENV PYTHONDONTWRITEBYTECODE 1 ENV PYTHONUNBUFFERED 1
Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends 
build-essential 
&& rm -rf /var/lib/apt/lists/*
Install poetry
RUN pip install --no-cache-dir poetry
Copy only the dependency definition files
COPY poetry.lock pyproject.toml /app/
Install project dependencies using poetry
--no-root: Don't install the project itself, only dependencies
--no-dev: Exclude development dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev
Copy the rest of the application's code
COPY ./app /app/app COPY ./alembic /app/alembic COPY alembic.ini /app/
Expose the port the app runs on
EXPOSE 8000
Command to run the application using Gunicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_conf.py", "app.main:app"]

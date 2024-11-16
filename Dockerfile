# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy project files
COPY app/ /code/app/

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock /code/app/

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install Python dependencies
RUN poetry install --only main

# Create staticfiles directory
RUN mkdir -p /code/app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
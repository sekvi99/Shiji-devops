FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    python3-dev

# Upgrading pip
RUN pip install --no-cache-dir --upgrade pip setuptools

# Copy and install application dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project structure
COPY ./shiji_app /app

# Set working dir
WORKDIR /app

# Run migrations
RUN python manage.py migrate

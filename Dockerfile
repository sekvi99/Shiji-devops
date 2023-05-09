FROM python:3.8.0-alpine

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./shiji_app /app

WORKDIR /app

RUN python manage.py migrate

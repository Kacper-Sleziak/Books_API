FROM python:3.10.4-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /django
COPY . .
RUN apt-get update
RUN apt-get -y install python3-dev libpq-dev gcc

RUN pip install -r requirements.txt

FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --mo-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

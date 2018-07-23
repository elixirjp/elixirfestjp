FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

VOLUME /code
WORKDIR /code

ADD . /code

RUN pip install --upgrade pip
RUN pip install -r requirements/base.txt

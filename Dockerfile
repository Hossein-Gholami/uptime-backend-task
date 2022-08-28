FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /uptime_backend_task

WORKDIR /uptime_backend_task

ADD . /uptime_backend_task/

RUN pip install -r requirements.txt
FROM python:3.6

LABEL maintainer="koriond98@gmail.com"

ENV BIND_PORT=8000

# netcat is required for wait_for function
RUN apt-get update && \
    apt-get install -y \
      gettext-base \
      netcat && \
    apt-get clean && \
    mkdir -p /var/www/django_api

WORKDIR /var/www/django_api

COPY django_api/requirements.txt ./

RUN pip install -r requirements.txt && \
    pip install gevent

COPY ./django_api /var/www/django_api
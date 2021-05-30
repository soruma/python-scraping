FROM python:3.9.5-buster

RUN apt update \
  && apt install -y build-essential libssl-dev libffi-dev python3-dev libpq-dev \
  && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile .
RUN pipenv install

EXPOSE 8050

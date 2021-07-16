FROM python:3.9-slim

RUN set -ex \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl

ENV PATH $PATH:/root/.poetry/bin
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

RUN mkdir -p /app
WORKDIR /app

COPY poetry.lock /app
COPY pyproject.toml /app
RUN poetry install

COPY . /app

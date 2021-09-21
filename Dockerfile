FROM python:3.9.7-slim

WORKDIR /app

RUN set -ex \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl

ENV PATH $PATH:/root/.poetry/bin
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY poetry.lock /app
COPY pyproject.toml /app

RUN poetry config virtualenvs.create false
RUN poetry update

COPY . /app

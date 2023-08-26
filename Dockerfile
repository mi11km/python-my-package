FROM python:3.10-slim

WORKDIR /app

RUN set -ex \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl

ENV PATH /root/.local/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock /app
COPY pyproject.toml /app

RUN poetry config virtualenvs.create false
RUN poetry update

COPY . /app
CMD ["python", "-m", "src"]

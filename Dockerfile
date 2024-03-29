ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

RUN set -ex \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get update \
  && apt-get install -y --no-install-recommends curl

ENV PATH /root/.local/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --only-root

COPY . .
CMD ["python", "-m", "src"]

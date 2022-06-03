FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
 PYTHONUNBUFFERED=1 \
 PYTHONHASHSEED=random \
 PIP_NO_CACHE_DIR=off \
 PIP_DISABLE_PIP_VERSION_CHECK=on \
 PIP_DEFAULT_TIMEOUT=100 \
 POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

RUN apt-get update -y && apt-get install -y gcc libmariadb-dev

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

EXPOSE 8000

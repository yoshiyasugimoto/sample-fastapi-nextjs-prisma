FROM python:3.13

WORKDIR /app

ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

COPY . /app/
RUN poetry install --without dev --no-root
# COPY prisma/ /work/prisma/

# RUN prisma generate

CMD ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.server:app", "--bind", "0.0.0.0:8000", "--access-logfile", "-"]

FROM python:3.10-slim

WORKDIR /app

# Instalar pipenv
RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

# Instalar dependências do pipenv
RUN pipenv install --deploy --system

COPY . .

CMD ["pipenv", "run", "airflow", "scheduler"]

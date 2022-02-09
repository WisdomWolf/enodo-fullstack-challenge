FROM tiangolo/meinheld-gunicorn-flask:python3.9
COPY ./src /app/
COPY ./Pipfile* /setup/
WORKDIR /setup
RUN pip install -U pip && pip install pipenv && pipenv install --system && pip install greenlet==0.4.17

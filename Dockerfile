FROM python:3.9

WORKDIR /app

COPY ./app /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


FROM python:latest

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["gunicorn", "core.wsgi", "0.0.0.0:8000"]

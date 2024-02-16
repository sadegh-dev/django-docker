FROM python:latest

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "A.wsgi", ":8000"]


## Directory structure ##

# + core/
#       - manage.py
#       - core/
# - Dockerfile
# - docker-compose.yml



## Create image od django ##

# > dockr build -t {image_name} .



## Run djnago image ##

# > docker run -p 8000:8000 {image_name}:{version}  


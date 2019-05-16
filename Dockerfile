FROM python:3.5.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /farmer_app

WORKDIR /farmer_app

ADD . /farmer_app/

RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install django-rest-swagger
RUN pip3 install django-cors-headers

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py migrate --database=usa
RUN python3 manage.py migrate --database=china
RUN python3 manage.py migrate --database=india

EXPOSE 8000

ENTRYPOINT ["python3","manage.py","runserver","0.0.0.0:8000"]
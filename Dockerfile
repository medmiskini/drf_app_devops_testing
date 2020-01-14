FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn api_crud.wsgi:application --bind=0.0.0.0:8000 --workers=3
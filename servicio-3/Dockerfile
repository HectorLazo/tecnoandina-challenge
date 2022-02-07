# Dockerfile con la imagen y pasos para dejar funcionando el servicio
# puede ser igual al del servicio-1 y servicio-2

FROM python:3.9.10-alpine3.15
WORKDIR /app

COPY . .

RUN pip3 install django==3.2
RUN pip3 install djangorestframework==3.13.1
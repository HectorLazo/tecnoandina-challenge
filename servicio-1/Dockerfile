# Dockerfile con la imagen y pasos para dejar funcionando el servicio
# puede ser igual al del servicio-2 y servicio-3

FROM python:3.9.10-alpine3.15
WORKDIR /app

RUN pip3 install --user paho-mqtt

COPY . .

CMD ["python", "-u", "main.py"]
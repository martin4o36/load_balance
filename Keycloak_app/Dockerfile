FROM python:3.10-alpine
EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache \
        musl-dev \
        mariadb-dev \
        gcc \
        mariadb-client

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app/

CMD ["sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:5000"]
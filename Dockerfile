FROM python:2.7-slim

COPY . /app

WORKDIR /app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["bash", "/app/entrypoint.sh"]

FROM python:3.10-slim

WORKDIR /app

COPY . /app

EXPOSE 4499

CMD ["python3", "-m", "http.server", "4499"]
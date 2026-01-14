FROM python:3.11-alpine
WORKDIR /app
COPY ej1.py .
CMD ["python", "-u", "ej1.py"]

FROM python:3.12-slim
WORKDIR /app
COPY notas.py .
CMD ["python","notas.py"]
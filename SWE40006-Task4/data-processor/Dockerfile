FROM python:3.12-slim

WORKDIR /app

COPY processor.py .

RUN useradd --create-home appuser

USER appuser

CMD ["python", "processor.py"]
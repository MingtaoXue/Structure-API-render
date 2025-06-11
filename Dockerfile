FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY logo.png .

COPY .well-known /app/.well-known

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 6000

CMD ["python", "app.py"]

# requirements.txt (save this in a separate file)
# ---
# flask==2.3.3
# gunicorn==21.2.0

# docker-compose.yml (save this in a separate file)
# ---
# version: '3'
# services:
#   ticket-service:
#     build: .
#     ports:
#       - "5000:5000"
#     volumes:
#       - .:/app
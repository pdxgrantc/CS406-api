# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Cloud Run expects $PORT environment variable
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]

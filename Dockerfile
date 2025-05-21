FROM python:3.10-slim

# Create non-root user
RUN adduser --disabled-password --gecos '' celeryuser

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# First copy only requirements to cache them
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Verify Django installed
RUN python -c "import django; print(f'Django version: {django.__version__}')"

# Copy the rest
COPY . .

# Switch to non-root user
USER celeryuser

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecomproject.wsgi:application"]?
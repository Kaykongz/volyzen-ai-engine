# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
  && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

# Install everything in requirements.txt first
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
 # then install pandas-ta from a tarball (no git needed)
 && pip install --no-cache-dir https://github.com/twopirllc/pandas-ta/archive/refs/tags/v0.3.14b0.tar.gz

# Copy app
COPY . /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.14.7-slim

WORKDIR /app

COPY requirements-docker.txt .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --prefer-binary -r requirements-docker.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
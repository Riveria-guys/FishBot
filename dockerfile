FROM python:3.13.2-slim

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
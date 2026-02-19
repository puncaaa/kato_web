FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

RUN python manage.py collectstatic --noinput

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

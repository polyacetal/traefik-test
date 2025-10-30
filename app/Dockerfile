FROM python:3.12-slim

WORKDIR /app
COPY src/app.py /app/

RUN pip install --no-cache-dir Flask==3.0.3 gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

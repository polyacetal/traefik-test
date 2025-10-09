FROM python:3.12-slim

WORKDIR /app
COPY app.py /app/

RUN pip install --no-cache-dir Flask==3.0.3

EXPOSE 5000
CMD ["python", "app.py"]

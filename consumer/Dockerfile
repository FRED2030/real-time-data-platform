FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install kafka-python prometheus-client

ENV PYTHONUNBUFFERED=1

CMD ["python", "consumer.py"]

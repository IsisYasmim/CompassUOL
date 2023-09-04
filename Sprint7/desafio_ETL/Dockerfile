FROM python:3

WORKDIR /app

COPY movies.csv .

COPY series.csv .

RUN pip install boto3

COPY . .

CMD ["python", "script.py"]

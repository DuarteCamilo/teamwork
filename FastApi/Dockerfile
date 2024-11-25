FROM python:3.12

COPY ./app /app
COPY ./requirements.txt /

WORKDIR /

RUN apt-get update && apt-get install -y mariadb-client && pip install mysqlclient

ENV TZ=America/Bogota

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]

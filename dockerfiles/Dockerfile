FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 app.py

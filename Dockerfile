FROM python:3.11

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY . /opt/app

RUN pip install -r reqs/requirements.txt


CMD python3 start.py
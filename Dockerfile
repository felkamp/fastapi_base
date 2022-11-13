FROM python:3.11

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY ./requirements.txt /opt/app

RUN pip install -r requirements.txt

ADD . /opt/app

CMD python3 start.py
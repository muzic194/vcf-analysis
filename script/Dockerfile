FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install python3 python3-pip -y

COPY . /script

WORKDIR /script

RUN pip3 install -r requirements.txt

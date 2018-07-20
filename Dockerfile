FROM ubuntu:18.04

VOLUME /home/root/.ssh
ADD . /personal_website
VOLUME /personal_website

RUN apt-get update \
    && apt-get -y install python3 \
       make \
       git

RUN git config --global user.name "Tanay PrabhuDesai" \
    && git config --global user.email "tanayseven@gmail.com"


FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y python3-pip python3-setuptools python3-dev libcurl4-openssl-dev libssl-dev xvfb
RUN apt-get install curl
RUN apt-get install apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
RUN apt-get update
ENV ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . /app/
WORKDIR /app
COPY requirement.txt /app/
RUN pip install -r requirement.txt
EXPOSE 9001
ENTRYPOINT python3 manage.py runserver 0.0.0.0:9001

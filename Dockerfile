# pull official base image
FROM python:3.7.4

# set work directory
WORKDIR /usr/src/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apt-get clean && apt-get update
RUN apt-get install -y gcc python3-dev python-dev build-essential default-libmysqlclient-dev musl-dev python-mysqldb

COPY code /usr/src/code/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
# run entrypoint.prod.sh





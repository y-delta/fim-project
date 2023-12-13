# Using official Python runtime as parent image
FROM python:3.8-slim

WORKDIR /usr/src/app

RUN useradd -m docker-user
USER docker-user

COPY ./server/src/* /usr/src/app/
COPY ./shared/ /usr/src/app/shared
COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD [ "python", "./main.py"]
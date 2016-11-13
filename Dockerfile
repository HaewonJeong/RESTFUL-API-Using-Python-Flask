# Set the base image
FROM python:2.7

# File Author / Maintainer
MAINTAINER bjg

# Update the sources list
RUN apt-get update

# Update the sources list
RUN apt-get -y upgrade

# Copy the application folder inside the container
ADD /todo-api /todo-api

# Get pip to download and install requirements:
RUN pip install -r /todo-api/requirements.txt

# Expose listener port
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /todo-api
RUN mkdir /data
# Set the default command to execute
# when creating a new container
CMD python restful.py

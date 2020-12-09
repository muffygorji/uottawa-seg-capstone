FROM python:3.7-slim
COPY . /app
WORKDIR /app

# Run should only be used when altering the state of the VM, but use CMD when executing system commands for which one is trying to run this application.
# TODO: Find a way to not deploy every time? 
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends gcc build-essential
RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python3 common-utils.py

RUN python3 build.py
RUN ls -al

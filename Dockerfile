FROM ubuntu:18.04

WORKDIR /opt
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Install Development Environment
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip

# Install Python Dependencies
COPY requirements.txt .
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/src/core/mediapipe/

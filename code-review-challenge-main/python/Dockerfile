FROM ubuntu:22.04 as base

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
RUN apt update  \
    && apt install -y python3-pip gdal-bin libgdal-dev cmake make gcc libtool ninja-build

RUN pip install wheel cython
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . .
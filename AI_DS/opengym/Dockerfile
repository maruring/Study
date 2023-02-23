FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y unzip \
    libglu1-mesa-dev \
    libgl1-mesa-dev \
    libosmesa6-dev \
    xvfb \
    patchelf \
    ffmpeg cmake g++

WORKDIR /root/src

RUN python -m pip install --upgrade pip
RUN python -m pip install 'gym[all]' 'gym[accept-rom-license]' jupyterlab ipywidgets matplotlib tensorflow keras-rl2
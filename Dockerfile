FROM nvcr.io/nvidia/tritonserver:24.01-py3

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    python3.10 \
    python3.10-dev \
    python3.10-venv \
    python3.10-distutils \
    python-is-python3 \
    ffmpeg \
    libsndfile1

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN python -m pip install --upgrade wheel
RUN python -m pip install --upgrade -r requirements.txt
FROM python:3.11

WORKDIR /opt/cinema_api

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && \
     pip install -r requirements.txt --no-cache-dir

COPY . .
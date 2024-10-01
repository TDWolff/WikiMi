FROM docker.io/python:3.11
WORKDIR /
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
COPY . /
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn gevent gevent-websocket flask-sockets
ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8877"
EXPOSE 8877
ENV FLASK_ENV=production
CMD [ "gunicorn", "main:app" ]
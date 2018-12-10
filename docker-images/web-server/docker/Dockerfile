FROM alpine:3.8

#
#
#

ENV WEBSERVER_PORT="80" \
    WEBSERVER_ADDRESS="0.0.0.0"

COPY ./app/ /app/

RUN apk add --no-cache \
        python2 \
        py-pip && \
    pip install --no-cache-dir -r /app/requirements.txt

LABEL name="web-server" \
      description="An image that provides a simple web server written in Python." \
      os="Alpine Linux" \
      os.version="3.8" \
      component.name="web-server"

WORKDIR /app

EXPOSE ${WEBSERVER_PORT}/tcp

ENTRYPOINT []

CMD ["python", "-u", "/app/web-server.py"]

Pyton web-server docker image
=============================

## Overview

An Docker image that contains a simple web server application written in Python to serve incoming HTTP queries for specific endpoints on an arbitrary TCP port and responds with code 200. It also provides simple Prometheus metrics for total amount of HTTP requests for every endpoint supported. In case an IP address and/or TCP port are not defined explicitly, the values 0.0.0.0 and 80 will be used as default respectively.

## Requirements

The image to be built and run requires `Docker` containerization platform.
Check [upstream documentation](https://docs.docker.com/install) for how to install `Docker` on your system.

## Building and running

To build the image run the following command in application root path:

```bash
docker build --pull --tag web-server -f docker/Dockerfile .
```

To run a container with the image use:

```bash
docker run \
    --name web-server \
    -e WEBSERVER_PORT="80" \
    -e WEBSERVER_ADDRESS="0.0.0.0" \
    -p 80:80 \
    -it web-server
```

## Environment variables

| Variable | Default value | Description |
| ------------------- | --------------- | ----------- |
| WEBSERVER_ADDRESS | 0.0.0.0 | An IPv4 address to listen HTTP requests on |
| WEBSERVER_PORT | 80 | A TCP port for HTTP server |

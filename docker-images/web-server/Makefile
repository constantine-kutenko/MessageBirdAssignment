
#
#
#

APP_NAME="web-server"

all: build run

build:
	@docker build --tag ${APP_NAME} -f docker/Dockerfile .

run:
	@docker run \
		--rm \
		--name ${APP_NAME} \
		-e WEBSERVER_PORT="80" \
		-e WEBSERVER_ADDRESS="0.0.0.0" \
		-p 80:80 \
		-it ${APP_NAME}

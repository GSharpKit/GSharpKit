FEDORA_VERSION = 27
VERSION = 27.18

all: pull build tag push

pull:
	sudo docker pull fedora:${FEDORA_VERSION}

build:
	sudo docker build --no-cache -t gsharpkit-linux .

tag:
	sudo docker tag gsharpkit-linux gsharpkit/gsharpkit-linux:${VERSION}

push:
	sudo docker push gsharpkit/gsharpkit-linux:${VERSION}


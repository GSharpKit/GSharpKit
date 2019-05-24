include ../config

all: pull build tag push

pull:
	sudo docker pull fedora:${FEDORA_VERSION}

build:
	cp Dockerfile.in Dockerfile
	sed -i -e 's!@VERSION@!${VERSION}!g' Dockerfile
	sed -i -e 's!@RELEASE@!${RELEASE}!g' Dockerfile
	sed -i -e 's!@FEDORA_VERSION@!${FEDORA_VERSION}!g' Dockerfile
	sudo docker build --no-cache -t gsharpkit-linux .

tag:
	sudo docker tag gsharpkit-linux gsharpkit/gsharpkit-linux:${VERSION}

push:
	sudo docker push gsharpkit/gsharpkit-linux:${VERSION}


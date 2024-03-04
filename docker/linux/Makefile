include ../../config

all: pull build tag

release: all push

pull:
	podman pull fedora:${FEDORA_VERSION}

build:
	cp Dockerfile.in Dockerfile
	sed -i -e 's!@VERSION@!${VERSION}!g' Dockerfile
	sed -i -e 's!@RELEASE@!${RELEASE}!g' Dockerfile
	sed -i -e 's!@FRAMEWORK@!${FRAMEWORK}!g' Dockerfile
	sed -i -e 's!@FEDORA_VERSION@!${FEDORA_VERSION}!g' Dockerfile
	podman build --no-cache -t gsharpkit-linux .

tag:
	podman tag gsharpkit-linux gsharpkit/gsharpkit-linux:${VERSION}

push:
	podman push gsharpkit/gsharpkit-linux:${VERSION}


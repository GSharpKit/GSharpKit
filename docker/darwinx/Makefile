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
	podman build --no-cache -t gsharpkit-darwinx .

tag:
	podman tag gsharpkit-darwinx gsharpkit/gsharpkit-darwinx:${VERSION}

push:
	podman push gsharpkit/gsharpkit-darwinx:${VERSION}


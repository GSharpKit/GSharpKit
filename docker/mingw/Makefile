include ../../config

all: pull build tag

release: all push

pull:
	podman pull fedora:${FEDORA_VERSION}

build:
	cp Dockerfile.in Dockerfile
	sed -i -e 's!@VERSION@!${VERSION}!g' Dockerfile
	sed -i -e 's!@RELEASE@!${RELEASE}!g' Dockerfile
	sed -i -e 's!@FEDORA_VERSION@!${FEDORA_VERSION}!g' Dockerfile
	podman build --no-cache -t gsharpkit-mingw .

tag:
	podman tag gsharpkit-mingw gsharpkit/gsharpkit-mingw:${VERSION}

push:
	podman push gsharpkit/gsharpkit-mingw:${VERSION}


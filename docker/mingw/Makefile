include ../../config

all: pull build tag

release: all push

pull:
	podman pull fedora:${FEDORA_VERSION}

build:
	cp Dockerfile.in Dockerfile
	cp ../../dictionary/da_DK-${DIC_VERSION}.aff da_DK.aff
	cp ../../dictionary/da_DK-${DIC_VERSION}.dic da_DK.dic
	sed -i -e 's!@VERSION@!${VERSION}!g' Dockerfile
	sed -i -e 's!@RELEASE@!${RELEASE}!g' Dockerfile
	sed -i -e 's!@FRAMEWORK@!${FRAMEWORK}!g' Dockerfile
	sed -i -e 's!@FEDORA_VERSION@!${FEDORA_VERSION}!g' Dockerfile
	podman build --no-cache -t gsharpkit-mingw .

tag:
	podman tag gsharpkit-mingw gsharpkit/gsharpkit-mingw:${VERSION}

push:
	podman push gsharpkit/gsharpkit-mingw:${VERSION}


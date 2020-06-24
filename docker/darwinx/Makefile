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
	podman build --no-cache -t gsharpkit-darwinx .

tag:
	podman tag gsharpkit-darwinx gsharpkit/gsharpkit-darwinx:${VERSION}

push:
	podman push gsharpkit/gsharpkit-darwinx:${VERSION}

download:
	-mkdir packages
	rm -rf packages/*
	scp gsharpkit@gimli.xmedicus.com:/home/gsharpkit/GSharpKit/Fedora32-x86_64/framework/darwinx-*.noarch.rpm packages/
	rm -f packages/darwinx-filesystem-base-*

update:
	sudo rpm -Fvh --ignoreos packages/*.rpm

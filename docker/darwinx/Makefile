include ../../config

all: pull build tag push

pull:
	sudo docker pull fedora:${FEDORA_VERSION}

build:
	cp Dockerfile.in Dockerfile
	sed -i -e 's!@VERSION@!${VERSION}!g' Dockerfile
	sed -i -e 's!@RELEASE@!${RELEASE}!g' Dockerfile
	sed -i -e 's!@FEDORA_VERSION@!${FEDORA_VERSION}!g' Dockerfile
	sudo docker build --no-cache -t gsharpkit-darwinx .

tag:
	sudo docker tag gsharpkit-darwinx gsharpkit/gsharpkit-darwinx:${VERSION}

push:
	sudo docker push gsharpkit/gsharpkit-darwinx:${VERSION}

download:
	rm -rf packages/*
	cd packages/
	scp gsharpkit@gimli.xmedicus.com:/home/gsharpkit/GSharpKit/Fedora30-x86_64/framework/darwinx-*.noarch.rpm .


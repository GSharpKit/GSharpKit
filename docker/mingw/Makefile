FEDORA_VERSION = 28
VERSION = 28.1

all: pull build tag push

pull:
	sudo docker pull fedora:${FEDORA_VERSION}

build:
	sudo docker build --no-cache -t gsharpkit-mingw .

tag:
	sudo docker tag gsharpkit-mingw gsharpkit/gsharpkit-mingw:latest
	sudo docker tag gsharpkit-mingw gsharpkit/gsharpkit-mingw:${VERSION}

push:
	sudo docker push gsharpkit/gsharpkit-mingw:latest
	sudo docker push gsharpkit/gsharpkit-mingw:${VERSION}


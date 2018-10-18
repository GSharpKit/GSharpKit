#!/bin/bash
BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

URL=http://pkgconfig.freedesktop.org/releases/

cd $BUILD_ROOT
curl -OL $URL/pkg-config-0.28.tar.gz
tar xfz pkg-config-0.28.tar.gz
cd pkg-config-0.28
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX --with-internal-glib
make
sudo make install
sudo ln -sf $SYMLINK/bin/pkg-config /usr/local/bin/pkg-config


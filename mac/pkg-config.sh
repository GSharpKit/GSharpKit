#!/bin/bash
BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

URL=http://pkgconfig.freedesktop.org/releases/

cd $BUILD_ROOT
curl -OL $URL/pkg-config-0.28.tar.gz
tar xfz pkg-config-0.28.tar.gz
cd pkg-config-0.28
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX --with-internal-glib
make
sudo make install
sudo ln -s $SYMLINK/bin/pkg-config /usr/local/bin/pkg-config


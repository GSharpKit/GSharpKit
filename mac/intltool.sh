#!/bin/bash
BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

URL=https://launchpad.net/intltool/trunk/0.50.2/+download

cd $BUILD_ROOT
curl -OL $URL/intltool-0.50.2.tar.gz
tar xfz intltool-0.50.2.tar.gz
cd intltool-0.50.2
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/intltoolize /usr/local/bin/intltoolize
sudo ln -sf $SYMLINK/bin/intltool-update /usr/local/bin/intltool-update
sudo ln -sf $SYMLINK/bin/intltool-extract /usr/local/bin/intltool-extract
sudo ln -sf $SYMLINK/bin/intltool-merge /usr/local/bin/intltool-merge
sudo ln -sf $SYMLINK/bin/intltool-prepare /usr/local/bin/intltool-prepare


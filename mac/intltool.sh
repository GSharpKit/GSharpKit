#!/bin/bash
BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

URL=https://launchpad.net/intltool/trunk/0.50.2/+download

cd $BUILD_ROOT
curl -OL $URL/intltool-0.50.2.tar.gz
tar xfz intltool-0.50.2.tar.gz
cd intltool-0.50.2
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -s $SYMLINK/bin/intltoolize /usr/local/bin/intltoolize
sudo ln -s $SYMLINK/bin/intltool-update /usr/local/bin/intltool-update
sudo ln -s $SYMLINK/bin/intltool-extract /usr/local/bin/intltool-extract
sudo ln -s $SYMLINK/bin/intltool-merge /usr/local/bin/intltool-merge
sudo ln -s $SYMLINK/bin/intltool-prepare /usr/local/bin/intltool-prepare


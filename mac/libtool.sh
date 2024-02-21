#!/bin/bash
SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

VERSION=2.4.7
URL=https://ftpmirror.gnu.org/libtool/libtool-$VERSION.tar.gz

cd $BUILD_ROOT

if [[ ! -f "libtool-$VERSION.tar.gz" ]]; then
        curl -OL $URL
fi

tar xfz libtool-$VERSION.tar.gz
cd libtool-$VERSION
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/intltoolize /usr/local/bin/intltoolize
sudo ln -sf $SYMLINK/bin/intltool-update /usr/local/bin/intltool-update
sudo ln -sf $SYMLINK/bin/intltool-extract /usr/local/bin/intltool-extract
sudo ln -sf $SYMLINK/bin/intltool-merge /usr/local/bin/intltool-merge
sudo ln -sf $SYMLINK/bin/intltool-prepare /usr/local/bin/intltool-prepare


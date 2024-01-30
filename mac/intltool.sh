#!/bin/bash
SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

VERSION=0.51.0
URL=https://launchpad.net/intltool/trunk/$VERSION/+download

cd $BUILD_ROOT

if [[ ! -f "intltool-$VERSION.tar.gz" ]]; then
        curl -OL $URL/intltool-$VERSION.tar.gz
fi

tar xfz intltool-$VERSION.tar.gz
cd intltool-$VERSION
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/intltoolize /usr/local/bin/intltoolize
sudo ln -sf $SYMLINK/bin/intltool-update /usr/local/bin/intltool-update
sudo ln -sf $SYMLINK/bin/intltool-extract /usr/local/bin/intltool-extract
sudo ln -sf $SYMLINK/bin/intltool-merge /usr/local/bin/intltool-merge
sudo ln -sf $SYMLINK/bin/intltool-prepare /usr/local/bin/intltool-prepare


#!/bin/bash

SCRIPT_ROOT=`pwd`
BUILD_ROOT=~/GSharpKitBuild

NAME=gettext
VERSION=0.18.3.1
URL=http://ftp.gnu.org/pub/gnu/gettext

cd $BUILD_ROOT
curl -o $NAME-$VERSION.tar.gz $URL/$NAME-$VERSION.tar.gz

cd $BUILD_ROOT
tar xfz $NAME-$VERSION.tar.gz
cd $NAME-$VERSION
darwinx-configure
make
sudo make install

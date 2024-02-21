#!/bin/bash

ARCH=`arch`
TARGET=aarch64-apple-darwin23.3.0
if [[ $ARCH == "i386" ]]; then
	TARGET=x86_64-apple-darwin23.3.0
fi

SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

sudo mkdir -p $PREFIX

cd $SCRIPT_ROOT

cd $BUILD_ROOT
if [[ ! -f nspr-4.35.tar.gz ]]; then
curl -o nspr-4.35.tar.gz http://ftp.mozilla.org/pub/nspr/releases/v4.35/src/nspr-4.35.tar.gz
fi
if [[ ! -f nss-3.96.1.tar.gz  ]]; then
curl -o nss-3.96.1.tar.gz https://archive.mozilla.org/pub/security/nss/releases/NSS_3_96_1_RTM/src/nss-3.96.1.tar.gz
fi
if [[ ! -f file-5.16.tar.gz ]]; then
curl -o file-5.16.tar.gz ftp://ftp.astron.com/pub/file/file-5.16.tar.gz
fi
if [[ ! -f popt-1.19.tar.gz ]]; then
curl -o popt-1.19.tar.gz http://ftp.rpm.org/popt/releases/popt-1.x/popt-1.19.tar.gz
fi
if [[ ! -f db-4.5.20.tar.gz ]]; then
curl -o db-4.5.20.tar.gz https://ftpmirror.your.org/pub/misc/Berkeley-DB/db-4.5.20.tar.gz
fi

if [[ -d nspr-4.35 ]]; then
	rm -rf nspr-4.35
fi

if [[ -d nss-3.96.1  ]]; then
        rm -rf nss-3.96.1
fi

if [[ -d file-5.16 ]]; then
        rm -rf file-5.16
fi

if [[ -d popt-1.19 ]]; then
        rm -rf popt-1.19
fi

if [[ -d db-4.5.20 ]]; then
        rm -rf db-4.5.20
fi

tar xfz nspr-4.35.tar.gz
tar xfz nss-3.96.1.tar.gz
tar xfz file-5.16.tar.gz 
tar xfz popt-1.19.tar.gz
tar xfz db-4.5.20.tar.gz

cd $BUILD_ROOT/nspr-4.35/nspr
./configure --target=$TARGET --prefix=$PREFIX --exec-prefix=$PREFIX --enable-64bit
make
sudo make install


cd $BUILD_ROOT/nss-3.96.1
patch -p1 < $SCRIPT_ROOT/sources/nss-crypto.patch
cd $BUILD_ROOT/nss-3.96.1/nss
make BUILD_OPT=1 NSPR_INCLUDE_DIR=$PREFIX/include/nspr NSPR_LIB_DIR=$PREFIX/lib USE_SYSTEM_ZLIB=1 ZLIB_LIBS=-lz USE_64=1
cd ../dist
sudo install -v -m755 Darwin*/lib/*.dylib           $PREFIX/lib
sudo install -v -m644 Darwin*/lib/{*.chk,libcrmf.a} $PREFIX/lib
sudo install -v -m755 -d                            $PREFIX/include/nss
sudo cp -v -RL {public,private}/nss/*               $PREFIX/include/nss
sudo chmod -v 644                                   $PREFIX/include/nss/*
sudo install -v -m755 Darwin*/bin/{certutil,nss-config,pk12util} $PREFIX/bin
sudo install -v -m644 Darwin*/lib/pkgconfig/nss.pc  $PREFIX/lib/pkgconfig

cd $BUILD_ROOT/file-5.16
./configure --target=$TARGET --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/popt-1.19
./configure --target=$TARGET --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/db-4.5.20/build_unix
../dist/configure --target=$TARGET --prefix=$PREFIX --exec-prefix=$PREFIX --disable-replication
make
sudo make install


#!/bin/bash

SCRIPT_ROOT=`pwd`
BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

RPM_VERSION=4.11.2

sudo mkdir -p $PREFIX
cd $PREFIX/..
sudo ln -s $PREFIX Current
cd ../
sudo ln -s $SYMLINK/bin Commands
sudo ln -s $SYMLINK/include Headers
sudo ln -s $SYMLINK/ Home
sudo ln -s $SYMLINK/lib Libraries
sudo mkdir External

cd $SCRIPT_ROOT
cp sources/rpm-${RPM_VERSION}.tar.bz2 $BUILD_ROOT/

cd $BUILD_ROOT
curl -o nspr-4.10.2.tar.gz http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v4.10.2/src/nspr-4.10.2.tar.gz
curl -o nss-3.15.3.tar.gz https://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_15_3_RTM/src/nss-3.15.3.tar.gz
curl -o file-5.16.tar.gz ftp://ftp.astron.com/pub/file/file-5.16.tar.gz
curl -o popt-1.16.tar.gz ftp://anduin.linuxfromscratch.org/BLFS/svn/p/popt-1.16.tar.gz
curl -o db-4.5.20.tar.gz http://download.oracle.com/berkeley-db/db-4.5.20.tar.gz
#curl -o rpm-${RPM_VERSION}.tar.bz2 http://rpm.org/releases/rpm-4.11.x/rpm-${RPM_VERSION}.tar.bz2

tar xfz nspr-4.10.2.tar.gz
tar xfz nss-3.15.3.tar.gz
tar xfz file-5.16.tar.gz 
tar xfz popt-1.16.tar.gz
tar xfz db-4.5.20.tar.gz
tar xfj rpm-${RPM_VERSION}.tar.bz2

cd $BUILD_ROOT/nspr-4.10.2/nspr
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/nss-3.15.3/nss
make BUILD_OPT=1 NSPR_INCLUDE_DIR=$PREFIX/include/nspr NSPR_LIB_DIR=$PREFIX/lib USE_SYSTEM_ZLIB=1 ZLIB_LIBS=-lz $([ $(uname -m) = x86_64 ] && echo USE_64=1)
cd ../dist
sudo install -v -m755 Darwin*/lib/*.dylib           $PREFIX/lib
sudo install -v -m644 Darwin*/lib/{*.chk,libcrmf.a} $PREFIX/lib
sudo install -v -m755 -d                            $PREFIX/include/nss
sudo cp -v -RL {public,private}/nss/*               $PREFIX/include/nss
sudo chmod -v 644                                   $PREFIX/include/nss/*
sudo install -v -m755 Darwin*/bin/{certutil,nss-config,pk12util} $PREFIX/bin
sudo install -v -m644 Darwin*/lib/pkgconfig/nss.pc  $PREFIX/lib/pkgconfig

cd $BUILD_ROOT/file-5.16
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/popt-1.16
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/db-4.5.20/build_unix
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ../dist/configure --prefix=$PREFIX --exec-prefix=$PREFIX --disable-replication
make
sudo make install

cd $BUILD_ROOT/rpm-${RPM_VERSION}
patch -p1 < $SCRIPT_ROOT/rpm-4.11.2-mac.patch
PATH=$PREFIX/bin:$PATH CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" CPPFLAGS="-I$PREFIX/include -I$PREFIX/include/nspr -I$PREFIX/include/nss" LDFLAGS="-arch x86_64 -L$PREFIX/lib" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX --with-external-db --without-lua --disable-optimized --disable-aio --with-glob --enable-broken-chown --disable-rpath
make
sudo make install
sudo install_name_tool -change @executable_path/libssl3.dylib $PREFIX/lib/libssl3.dylib $PREFIX/lib/libssl3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/libssl3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libssl3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libssl3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libssl3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libssl3.dylib

sudo install_name_tool -change @executable_path/libsqlite3.dylib $PREFIX/lib/libsqlite3.dylib $PREFIX/lib/libsqlite3.dylib

sudo install_name_tool -change @executable_path/libsoftokn3.dylib $PREFIX/lib/libsoftokn3.dylib $PREFIX/lib/libsoftokn3.dylib
sudo install_name_tool -change @executable_path/libsqlite3.dylib $PREFIX/lib/libsqlite3.dylib $PREFIX/lib/libsoftokn3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libsoftokn3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libsoftokn3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libsoftokn3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libsoftokn3.dylib

sudo install_name_tool -change @executable_path/libsmime3.dylib $PREFIX/lib/libsmime3.dylib $PREFIX/lib/libsmime3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/libsmime3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libsmime3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libsmime3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libsmime3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libsmime3.dylib

sudo install_name_tool -change @executable_path/libfreebl3.dylib $PREFIX/lib/libfreebl3.dylib $PREFIX/lib/libfreebl3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libfreebl3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libfreebl3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/libnss3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libnss3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libnss3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libnss3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libnss3.dylib
sudo install_name_tool -change @executable_path/libnssckbi.dylib $PREFIX/lib/libnssckbi.dylib $PREFIX/lib/libnssckbi.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libnssckbi.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libnssckbi.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libnssckbi.dylib
sudo install_name_tool -change @executable_path/libnssdbm3.dylib $PREFIX/lib/libnssdbm3.dylib $PREFIX/lib/libnssdbm3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libnssdbm3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libnssdbm3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libnssdbm3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libnssdbm3.dylib
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libnssutil3.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libnssutil3.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libnssutil3.dylib
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/lib/libplc4.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libplc4.dylib
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/lib/libplds4.dylib
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/lib/libplds4.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpm
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpm2cpio
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmbuild
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmdb
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmgraph
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmkeys
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmsign
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/rpmspec 
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpm.3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmbuild.3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmio.3.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmsign.1.dylib

sudo install_name_tool -change @executable_path/libssl3.dylib $PREFIX/lib/libssl3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libsmime3.dylib $PREFIX/lib/libsmime3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/bin/certutil

sudo mkdir -p $PREFIX/var/lib/rpm
sudo mkdir -p $PREFIX/etc/rpm
sudo cp $SCRIPT_ROOT/rpm/SOURCES/macros.darwinx $PREFIX/etc/rpm/
sudo cp $SCRIPT_ROOT/rpm/SOURCES/macros.dist $PREFIX/etc/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-lang.sh $PREFIX/lib/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-provides.sh $PREFIX/lib/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-requires.sh $PREFIX/lib/rpm/
sudo chmod 777 $PREFIX/var/tmp
sudo chmod 777 $PREFIX/var/lib
sudo chmod 777 $PREFIX/var/lib/rpm

export PATH="/Library/Frameworks/AppBox.framework/Versions/Current/bin:$PATH"
export DYLD_LIBRARY_PATH="/Library/Frameworks/AppBox.framework/Versions/Current/lib:$DYLD_LIBRARY_PATH"
export DYLD_FALLBACK_LIBRARY_PATH="/Library/Frameworks/AppBox.framework/Versions/Current/lib:$DYLD_FALLBACK_LIBRARY_PATH"

rpm --initdb

sudo ln -s $SYMLINK/bin/rpm /usr/local/bin/rpm
sudo ln -s $SYMLINK/bin/rpm2cpio /usr/local/bin/rpm2cpio
sudo ln -s $SYMLINK/bin/rpmbuild /usr/local/bin/rpmbuild
sudo ln -s $SYMLINK/bin/rpmdb /usr/local/bin/rpmdb
sudo ln -s $SYMLINK/bin/rpmgraph /usr/local/bin/rpmgraph
sudo ln -s $SYMLINK/bin/rpmkeys /usr/local/bin/rpmkeys
sudo ln -s $SYMLINK/bin/rpmsign /usr/local/bin/rpmsign
sudo ln -s $SYMLINK/bin/rpmspec /usr/local/bin/rpmspec


#!/bin/bash

SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

RPM_VERSION=4.18.2

sudo mkdir -p $PREFIX

cd $SCRIPT_ROOT
cp -f sources/rpm-${RPM_VERSION}.tar.bz2 $BUILD_ROOT/

cd $BUILD_ROOT
#if [[ ! -f rpm-${RPM_VERSION}.tar.bz2 ]]; then
#curl -o rpm-${RPM_VERSION}.tar.bz2 http://ftp.rpm.org/releases/rpm-4.19.x/rpm-${RPM_VERSION}.tar.bz2
#fi

if [[ -d rpm-${RPM_VERSION} ]]; then
        rm -rf rpm-${RPM_VERSION}
fi

tar xfj rpm-${RPM_VERSION}.tar.bz2

cd $BUILD_ROOT/rpm-${RPM_VERSION}
#patch -p1 < $SCRIPT_ROOT/rpm-4.11.2-mac.patch
PATH=$PREFIX/bin:$PATH CPPFLAGS="-I$PREFIX/include -I$PREFIX/include/nspr -I$PREFIX/include/nss" LDFLAGS="-L$PREFIX/lib" ./configure --target=aarch64-apple-darwin23.2.0 --prefix=$PREFIX --exec-prefix=$PREFIX --with-external-db --without-lua --disable-optimized --disable-aio --with-glob --enable-broken-chown --disable-rpath --without-archive
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
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpm.9.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmbuild.9.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmio.9.dylib
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/lib/librpmsign.9.dylib

sudo install_name_tool -change @executable_path/libssl3.dylib $PREFIX/lib/libssl3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libsmime3.dylib $PREFIX/lib/libsmime3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnss3.dylib $PREFIX/lib/libnss3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnssutil3.dylib $PREFIX/lib/libnssutil3.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libplc4.dylib $PREFIX/lib/libplc4.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libplds4.dylib $PREFIX/lib/libplds4.dylib $PREFIX/bin/certutil
sudo install_name_tool -change @executable_path/libnspr4.dylib $PREFIX/lib/libnspr4.dylib $PREFIX/bin/certutil

sudo mkdir -p $PREFIX/var/lib/rpm
sudo mkdir -p $PREFIX/etc/rpm
sudo cp $SCRIPT_ROOT/../rpm/SOURCES/macros.darwinx $PREFIX/etc/rpm/
sudo cp $SCRIPT_ROOT/../rpm/SOURCES/macros.dist $PREFIX/etc/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-lang.sh $PREFIX/lib/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-provides.sh $PREFIX/lib/rpm/
#sudo cp $SCRIPT_ROOT/darwinx-find-requires.sh $PREFIX/lib/rpm/
sudo chmod 777 $PREFIX/var/tmp
sudo chmod 777 $PREFIX/var/lib
sudo chmod 777 $PREFIX/var/lib/rpm

sudo ln -sf $SYMLINK/bin/rpm /usr/local/bin/rpm
sudo ln -sf $SYMLINK/bin/rpm2cpio /usr/local/bin/rpm2cpio
sudo ln -sf $SYMLINK/bin/rpmbuild /usr/local/bin/rpmbuild
sudo ln -sf $SYMLINK/bin/rpmdb /usr/local/bin/rpmdb
sudo ln -sf $SYMLINK/bin/rpmgraph /usr/local/bin/rpmgraph
sudo ln -sf $SYMLINK/bin/rpmkeys /usr/local/bin/rpmkeys
sudo ln -sf $SYMLINK/bin/rpmsign /usr/local/bin/rpmsign
sudo ln -sf $SYMLINK/bin/rpmspec /usr/local/bin/rpmspec

rpm --initdb

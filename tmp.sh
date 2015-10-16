#!/bin/bash
NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION

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



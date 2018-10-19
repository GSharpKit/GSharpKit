#!/bin/bash

sudo cp darwinx-configure.sh /usr/local/bin/darwinx-configure

sudo chmod 755 /usr/local/bin/darwinx-configure

cd /usr/local/lib
sudo ln -sf ../../lib/libSystem.B.dylib libgcc_s.10.4.dylib
sudo ln -sf ../../lib/libSystem.B.dylib libgcc_s.10.5.dylib
cd -

sh rpm.sh
sh pkg-config.sh
sh automake.sh
sh bison.sh
sh xz.sh
sh cmake.sh


#!/bin/bash

sudo cp darwinx-configure.sh /usr/local/bin/darwinx-configure

sudo chmod 755 /usr/local/bin/darwinx-configure

sh rpm.sh
sh pkg-config.sh
sh automake.sh
sh bison.sh
sh xz.sh
sh cmake.sh


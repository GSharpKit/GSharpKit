#!/bin/bash

sudo cp darwinx-configure.sh /usr/local/bin/darwinx-configure
sudo chmod 755 /usr/local/bin/darwinx-configure

sudo cp darwinx-make.sh /usr/local/bin/darwinx-make
sudo chmod 755 /usr/local/bin/darwinx-make

sh rpm.sh
sh pkg-config.sh
sh automake.sh
sh bison.sh
sh xz.sh
sh cmake.sh
sh ninja.sh
sh meson.sh


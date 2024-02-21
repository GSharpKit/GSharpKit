#!/bin/bash

sh rpm-pre1.sh
sh pkg-config.sh
sh xz.sh
sh libgcrypt.sh
sh sqlite.sh
sh lua.sh
sh rpm.sh

sudo cp darwinx-env.sh /usr/local/bin/darwinx-env
sudo chmod 755 /usr/local/bin/darwinx-env

sudo cp darwinx-run.sh /usr/local/bin/darwinx-run
sudo chmod 755 /usr/local/bin/darwinx-run

sudo cp darwinx-configure.sh /usr/local/bin/darwinx-configure
sudo chmod 755 /usr/local/bin/darwinx-configure

sudo cp darwinx-make.sh /usr/local/bin/darwinx-make
sudo chmod 755 /usr/local/bin/darwinx-make

sh automake.sh
sh bison.sh
sh cmake.sh
sh ninja.sh
sh meson.sh
sh rust.sh
#sh gettext.sh
sh intltool.sh
sh libtool.sh

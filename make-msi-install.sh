#!/bin/bash

#shopt -s extglob

FROM=$1
TO=$2
ARCH=$3

echo "Install Framework $FROM"

# BIN directory
mkdir $TO/bin
cp $FROM/bin/mono.exe $TO/bin/
cp $FROM/lib/mono/4.5/cert-sync.exe $TO/bin/
cp /etc/pki/tls/certs/ca-bundle.crt $TO/bin/

cp $FROM/bin/VC_redist.${ARCH}.exe $TO/bin/

cp $FROM/bin/dbus-daemon.exe $TO/bin/
cp $FROM/bin/dbus-launch.exe $TO/bin/
cp $FROM/bin/dbus-send.exe $TO/bin/
cp $FROM/bin/gdk-pixbuf-query-loaders.exe $TO/bin/
cp $FROM/bin/gtk-query-immodules-3.0.exe $TO/bin/

cp $FROM/bin/*.dll $TO/bin/
cp $FROM/lib/*.dll $TO/bin/
cp $TO/bin/libsqlite3-0.dll $TO/bin/libsqlite3.dll

# ETC directory
mkdir $TO/etc
cp -r $FROM/etc/dbus-1 $TO/etc/
touch $TO/etc/dbus-1/session.d/empty
cp -r $FROM/etc/fonts $TO/etc/
cp -r $FROM/etc/gtk-2.0 $TO/etc/
cp -r $FROM/etc/gtk-3.0 $TO/etc/
cp -r $FROM/etc/mono $TO/etc/
cp -r $FROM/etc/pki $TO/etc/

# LIB directory
mkdir $TO/lib
cp -r $FROM/lib/enchant $TO/lib/
cp -r $FROM/lib/engines $TO/lib/
cp -r $FROM/lib/gdk-pixbuf-2.0 $TO/lib/
cp -r $FROM/lib/gio $TO/lib/
cp -r $FROM/lib/gstreamer-1.0 $TO/lib/
cp -r $FROM/lib/gtk-3.0 $TO/lib/

mkdir -p $TO/lib/mono/4.5
cp -r $FROM/lib/mono/4.5/mscorlib.dll $TO/lib/mono/4.5/
cp -r $FROM/lib/mono/4.5/Facades $TO/lib/mono/4.5/
rm -f $TO/lib/mono/4.5/Facades/*.pdb
cp -r $FROM/lib/mono/gac $TO/lib/mono/
rm -f $TO/lib/mono/gac/*/*/*.pdb
rm -f $TO/lib/mono/gac/*/*/*.mdb

# SHARE directory
mkdir -p $TO/share/glib-2.0
cp -r $FROM/share/glib-2.0/schemas $TO/share/glib-2.0/

mkdir -p $TO/share/icons/Adwaita
cp -r $FROM/share/icons/Adwaita/16x16 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/24x24 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/32x32 $TO/share/icons/Adwaita/
cp -r $FROM/share/icons/Adwaita/48x48 $TO/share/icons/Adwaita/
cp $FROM/share/icons/Adwaita/index.theme $TO/share/icons/Adwaita/

mkdir -p $TO/share/locale
cp -r $FROM/share/locale/da $TO/share/locale/
cp -r $FROM/share/locale/sv $TO/share/locale/

cp -r $FROM/share/myspell $TO/share/

#!/bin/bash

#shopt -s extglob

FROM=$1
TO=$2

echo "Install Framework $FROM into $TO"

# ETC directory
mkdir -p $TO/etc
cp -r $FROM/etc/dbus-1 $TO/etc/
cp -r $FROM/etc/fonts $TO/etc/
cp -r $FROM/etc/gtk-3.0 $TO/etc/
cp -r $FROM/etc/mono $TO/etc/
cp -r $FROM/etc/pki $TO/etc/
cp ca-bundle.crt $TO/etc/pki/
#cp -r $FROM/etc/sane.d $TO/etc/

# BIN directory
mkdir -p $TO/bin
cp $FROM/bin/mono $TO/bin/
cp $FROM/lib/mono/4.5/cert-sync.exe $TO/bin/

cp $FROM/bin/dbus-daemon $TO/bin/
cp $FROM/bin/dbus-launch $TO/bin/
cp $FROM/bin/dbus-send $TO/bin/

cp $FROM/bin/glib-compile-schemas $TO/bin/
cp $FROM/bin/gdk-pixbuf-query-loaders $TO/bin/
cp $FROM/bin/gtk-query-immodules-3.0 $TO/bin/

cp $FROM/bin/fc-cache $TO/bin/

# LIB directory
mkdir -p $TO/lib
cp $FROM/lib/*.dll $TO/lib/
cp $FROM/lib/*.dll.config $TO/lib/

# Hack to make gphoto work.
#cp $TO/lib/libgphoto2-sharp.dll $TO/lib/libgphoto2.dll

cp -a $FROM/lib/*.dylib $TO/lib/
 
mkdir -p $TO/lib/mono/4.5
cp -r $FROM/lib/mono/4.5/mscorlib.dll $TO/lib/mono/4.5/
cp -r $FROM/lib/mono/4.5/Facades $TO/lib/mono/4.5/
rm -f $TO/lib/mono/4.5/Facades/*.pdb
cp -r $FROM/lib/mono/gac $TO/lib/mono/
rm -f $TO/lib/mono/gac/*/*/*.pdb
rm -f $TO/lib/mono/gac/*/*/*.mdb

mkdir -p $TO/lib/enchant
cp -r $FROM/lib/enchant/*.so $TO/lib/enchant/

#cp -r $FROM/lib/engines-1_1 $TO/lib/

cp -r $FROM/lib/gdk-pixbuf-2.0 $TO/lib/
rm -f $TO/lib/gdk-pixbuf-2.0/2.10.0/loaders/*.a
rm -f $TO/lib/gdk-pixbuf-2.0/2.10.0/loaders/*.la

cp -r $FROM/lib/gio $TO/lib/
rm -f $TO/lib/gio/modules/*.la

cp -r $FROM/lib/gstreamer-1.0 $TO/lib/
rm -f $TO/lib/gstreamer-1.0/*.la

cp -r $FROM/lib/gtk-3.0 $TO/lib/
rm -f $TO/lib/gtk-3.0/3.0.0/immodules/*.a
rm -f $TO/lib/gtk-3.0/3.0.0/immodules/*.la
rm -f $TO/lib/gtk-3.0/3.0.0/printbackends/*.a
rm -f $TO/lib/gtk-3.0/3.0.0/printbackends/*.la

#cp -r $FROM/lib/libgphoto2 $TO/lib/
#cp -r $FROM/lib/libgphoto2_port $TO/lib/

# SHARE directory
mkdir -p $TO/share
cp -r $FROM/share/dbus-1 $TO/share/

mkdir $TO/share/glib-2.0
cp -r $FROM/share/glib-2.0/schemas $TO/share/glib-2.0/

mkdir -p $TO/share/icons
cp -r $FROM/share/icons/Adwaita $TO/share/icons/
cp -r $FROM/share/icons/hicolor $TO/share/icons/

mkdir -p $TO/share/locale
cp -r $FROM/share/locale/da $TO/share/locale/
cp -r $FROM/share/locale/sv $TO/share/locale/

#cp -r $FROM/share/myspell $TO/share/

#!/bin/bash

NAMES=(
filesystem
binutils
crt
headers
cpp
gcc
gcc-c++
gcc-objc
pkg-config
winpthreads
termcap
zlib
win-iconv
gettext
libffi
pcre
glib2
pixman
bzip2
freetype
expat
fontconfig
libpng
libjpeg-turbo
libtiff
cairo
icu
harfbuzz
pango
atk
jasper
libxml2
libcroco
libepoxy
librsvg2
gdk-pixbuf
gtk3
libgdl
adwaita-icon-theme
nsis
ige-mac-bundler
gtk-mac-integration
libgpg-error
libgcrypt
gmp
nettle
libtasn1
p11-kit
readline
gnutls
openssl
glib-networking
libxslt
sqlite
libsoup
libidn
hunspell
enchant
libogg
libvorbis
orc
libwebp
speex
gsm
ilmbase
OpenEXR
wavpack
opus
gstreamer1
gstreamer1-plugins-base
gstreamer1-plugins-good
gstreamer1-plugins-bad
webkitgtk3
dbus
dbus-glib
mono-core
Npgsql
GtkSharp
GdlSharp
gtk-mac-integration-sharp
mono-zeroconf
mono-addins
webkitgtk3-sharp
dbus-sharp
dbus-sharp-glib
gstreamer1-sharp
Newtonsoft.Json
BouncyCastle
MimeKit
MailKit
ServiceStack
RestSharp
SealApi
PDFsharp-MigraDoc
)

declare -A RPMS
CRPMS=(`rpm -qa --qf '%{NAME} %{VERSION} '`)
IDX=0
KEY=""
for i in ${CRPMS[@]}; do
	if [[ $((IDX % 2)) == 0 ]]; then
		KEY=$i;
	else
		RPMS[$KEY]=$i;
	fi
	IDX=$((IDX + 1))
done

#for k in "${!RPMS[@]}"
#do
#	echo "$k ${RPMS[$k]}"
#done
#exit;

echo "Package, Linux 64bit, Windows 32/64bit, Mac OS X 64bit "

for i in ${NAMES[@]}; do
	STR="$i"
	FOUND=0
	for k in "${!RPMS[@]}"
	do
		if [[ $i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
		fi
	done
	if [[ $FOUND == 0 ]]; then
		STR="$STR, "
	fi
	FOUND=0
        for k in "${!RPMS[@]}"
        do
               	if [[ mingw32-$i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
		fi
        done
        if [[ $FOUND == 0 ]]; then
                STR="$STR, "
        fi
        FOUND=0
        for k in "${!RPMS[@]}"
        do
                if [[ darwinx-$i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
                fi
        done
        if [[ $FOUND == 0 ]]; then
                STR="$STR, "
        fi
	echo $STR
done


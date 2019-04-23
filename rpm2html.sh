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
fribidi
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
libunistring
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
libusbx
libexif
libgphoto2
sane-backends
twaindsm
webkitgtk3
dbus
dbus-glib
mono-core
Npgsql
GtkSharp
GdlSharp
gtk-mac-integration-sharp
Mono.Addins
webkitgtk3-sharp
dbus-sharp
dbus-sharp-glib
GstSharp
libgphoto2-sharp
SharpCamera
Newtonsoft.Json
BouncyCastle
MimeKit
MailKit
ServiceStack
RestSharp
Seal.net
PDFsharp-MigraDoc
SharpZipLib
)

LIN_BUILD_IN=(
crt
headers
pkg-config
gdk-pixbuf
termcap
jasper
)

LIN_NA=(
gtk-mac-integration
winpthreads
win-iconv
nsis
gtk-mac-integration-sharp
)

WIN_BUILD_IN=(
mono-core
)

WIN_NA=(
ige-mac-bundler
gtk-mac-integration
libunistring
gtk-mac-integration-sharp
)

MAC_BUILD_IN=(
binutils
crt
headers
cpp
gcc
gcc-c++
gcc-objc
pkg-config
termcap
zlib
bzip2
expat
readline
openssl
sqlite
libidn
hunspell
twaindsm
)

MAC_NA=(
winpthreads
win-iconv
nsis
gtk-mac-integration-sharp
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

echo "Package, Linux 64bit, Windows 32/64bit, Mac OS X 64bit "

for i in ${NAMES[@]}; do
	STR="$i"
	FOUND=0
	for k in "${!RPMS[@]}"
	do
		if [[ $i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
			break
		fi
	done
	if [[ $FOUND == 0 ]]; then
		for lb in ${LIN_BUILD_IN[@]};
		do
		        if [[ $i == $lb ]]; then
				STR="$STR, Build-in"
				FOUND=1
				break
		        fi	
		done
		for lna in ${LIN_NA[@]};
		do
		        if [[ $i == $lna ]]; then
				STR="$STR, N/A"
				FOUND=1
				break
		        fi	
		done
		if [[ $FOUND == 0 ]]; then
                	STR="$STR, "
		fi
	fi
	FOUND=0
        for k in "${!RPMS[@]}"
        do
               	if [[ mingw32-$i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
			break
		fi
        done
        if [[ $FOUND == 0 ]]; then
		for wb in ${WIN_BUILD_IN[@]};
		do
		        if [[ $i == $wb ]]; then
				STR="$STR, Build-in"
				FOUND=1
				break
		        fi	
		done
		for wna in ${WIN_NA[@]};
		do
		        if [[ $i == $wna ]]; then
				STR="$STR, N/A"
				FOUND=1
				break
		        fi	
		done
		if [[ $FOUND == 0 ]]; then
                	STR="$STR, "
		fi
        fi
        FOUND=0
        for k in "${!RPMS[@]}"
        do
                if [[ darwinx-$i == $k ]]; then
			STR="$STR, ${RPMS[$k]}"
			FOUND=1
			break
                fi
        done
        if [[ $FOUND == 0 ]]; then
		for mb in ${MAC_BUILD_IN[@]};
		do
		        if [[ $i == $mb ]]; then
				STR="$STR, Build-in"
				FOUND=1
				break
		        fi	
		done
		for mna in ${MAC_NA[@]};
		do
		        if [[ $i == $mna ]]; then
				STR="$STR, N/A"
				FOUND=1
				break
		        fi	
		done
		if [[ $FOUND == 0 ]]; then
                	STR="$STR, "
		fi
        fi
	echo $STR
done


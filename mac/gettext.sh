SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

VERSION=0.26

cd $BUILD_ROOT

if [[ ! -f "gettext-$VERSION.tar.gz" ]]; then
	curl -OL https://ftp.gnu.org/pub/gnu/gettext/gettext-$VERSION.tar.gz
fi

tar xfz gettext-$VERSION.tar.gz
cd gettext-$VERSION
./configure --prefix=$PREFIX --exec-prefix=$PREFIX \
        --disable-dependency-tracking \
        --disable-static \
        --without-git \
        --disable-java \
        --disable-c++ \
        --disable-libasprintf \
        --with-included-libxml

make
sudo make install
sudo ln -sf $SYMLINK/bin/autopoint /usr/local/bin/autopoint

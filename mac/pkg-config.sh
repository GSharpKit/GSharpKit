SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT

URL=http://pkgconfig.freedesktop.org/releases/

curl -OL $URL/pkg-config-0.28.tar.gz
tar xfz pkg-config-0.28.tar.gz
cd pkg-config-0.28
./configure --prefix=$PREFIX --exec-prefix=$PREFIX --with-internal-glib
make
sudo make install
sudo ln -sf $SYMLINK/bin/pkg-config /usr/local/bin/pkg-config


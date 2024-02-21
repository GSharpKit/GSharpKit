SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
if [[ ! -f sqlite-autoconf-3450100.tar.gz ]]; then
curl -OL https://www.sqlite.org/2024/sqlite-autoconf-3450100.tar.gz
fi

if [[ -d sqlite-autoconf-3450100 ]]; then
        rm -rf sqlite-autoconf-3450100
fi

tar xzf sqlite-autoconf-3450100.tar.gz

cd sqlite-autoconf-3450100
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

VERSION=3.28.1

cd $BUILD_ROOT
curl -OL https://cmake.org/files/v3.28/cmake-$VERSION.tar.gz
tar xzf cmake-$VERSION.tar.gz
cd cmake-$VERSION
./configure --prefix=$PREFIX
make
sudo make install
cd ..
sudo ln -sf $SYMLINK/bin/cmake /usr/local/bin/cmake
sudo mkdir -p $PREFIX/share/cross
sudo cp toolchain-darwinx.cmake $PREFIX/share/cross/

BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -OL https://cmake.org/files/v3.17/cmake-3.17.3.tar.gz
tar xzf cmake-3.17.3.tar.gz
cd cmake-3.17.3
./configure --prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/cmake /usr/local/bin/cmake
sudo mkdir -p $PREFIX/share/cross
sudo cp toolchain-darwinx.cmake $PREFIX/share/cross/

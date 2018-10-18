BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -OL https://cmake.org/files/v3.7/cmake-3.7.0.tar.gz
tar xzf cmake-3.7.0.tar.gz
cd cmake-3.7.0
./configure --prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/cmake /usr/local/bin/cmake

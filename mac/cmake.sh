BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

cd $BUILD_ROOT
curl -OL https://cmake.org/files/v3.7/cmake-3.7.0.tar.gz
tar xzf cmake-3.7.0.tar.gz
cd cmake-3.7.0
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -s $SYMLINK/bin/cmake /usr/local/bin/cmake

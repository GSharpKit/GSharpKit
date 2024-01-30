SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -OL https://ftp.gnu.org/gnu/bison/bison-3.8.2.tar.xz
tar xfj bison-3.8.2.tar.xz
cd bison-3.8.2
#patch -p0 < $MAIN_ROOT/sources/secure_snprintf.patch
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

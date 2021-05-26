MAIN_ROOT=`pwd`
BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -OL http://ftp.gnu.org/gnu/bison/bison-3.7.6.tar.gz 
tar xzf bison-3.7.6.tar.gz
cd bison-3.7.6
patch -p0 < $MAIN_ROOT/sources/secure_snprintf.patch
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

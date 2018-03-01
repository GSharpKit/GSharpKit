MAIN_ROOT=`pwd`
BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

cd $BUILD_ROOT
curl -OL http://ftp.gnu.org/gnu/bison/bison-2.7.tar.gz 
tar xzf bison-2.7.tar.gz
cd bison-2.7
patch -p0 < $MAIN_ROOT/sources/secure_snprintf.patch
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

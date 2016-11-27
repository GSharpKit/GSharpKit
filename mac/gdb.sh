BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

cd $BUILD_ROOT
#curl -OL http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz
tar xzf gdb-7.6.tar.gz
cd gdb-7.6
./configure --prefix=$PREFIX --exec-prefix=$PREFIX --enable-targets=x86_64-apple-darwin13.0.0 --enable-64-bit-bfd --disable-werror --build=x86_64-apple-darwin13.0.0 --host=x86_64-apple-darwin13.0.0 --target=x86_64-apple-darwin13.0.0
make
sudo make install
sudo ln -s $SYMLINK/bin/gdb /usr/bin/gdb

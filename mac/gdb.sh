BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/Frameworks/$NAME
SYMLINK=/Library/Frameworks/$NAME

cd $BUILD_ROOT
#curl -OL http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz
tar xzf gdb-7.6.tar.gz
cd gdb-7.6
./configure --prefix=$PREFIX --exec-prefix=$PREFIX --enable-targets=x86_64-apple-darwin13.0.0 --enable-64-bit-bfd --disable-werror --build=x86_64-apple-darwin13.0.0 --host=x86_64-apple-darwin13.0.0 --target=x86_64-apple-darwin13.0.0
make
sudo make install
sudo ln -sf $SYMLINK/bin/gdb /usr/local/bin/gdb

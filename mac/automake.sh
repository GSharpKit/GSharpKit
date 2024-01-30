SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

curl -OL http://ftpmirror.gnu.org/m4/m4-1.4.17.tar.gz
tar xzf m4-1.4.17.tar.gz
cd m4-1.4.17
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-2.69.tar.gz
tar xzf autoconf-2.69.tar.gz
cd autoconf-2.69
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
export PATH=$PATH:$PREFIX/bin

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.11.6.tar.gz
tar xzf automake-1.11.6.tar.gz
cd automake-1.11.6
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.13.tar.gz
tar xzf automake-1.13.tar.gz
cd automake-1.13
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.14.1.tar.gz
tar xzf automake-1.14.1.tar.gz
cd automake-1.14.1
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.15.tar.gz
tar xzf automake-1.15.tar.gz
cd automake-1.15
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.16.5.tar.gz
tar xzf automake-1.16.5.tar.gz
cd automake-1.16.5
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/libtool/libtool-2.4.7.tar.xz
tar xzj libtool-2.4.7.tar.xz
cd libtool-2.4.7
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://mirrors.dotsrc.org/gnu/autoconf-archive/autoconf-archive-2019.01.06.tar.xz
tar xzf autoconf-archive-2019.01.06.tar.xz
cd autoconf-archive-2019.01.06
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

sudo ln -sf $SYMLINK/bin/autoconf /usr/local/bin/autoconf
sudo ln -sf $SYMLINK/bin/automake-1.16 /usr/local/bin/automake
sudo ln -sf $SYMLINK/bin/automake-1.16 /usr/local/bin/automake-1.16
sudo ln -sf $SYMLINK/bin/automake-1.15 /usr/local/bin/automake-1.15
sudo ln -sf $SYMLINK/bin/automake-1.14 /usr/local/bin/automake-1.14
sudo ln -sf $SYMLINK/bin/automake-1.13 /usr/local/bin/automake-1.13
sudo ln -sf $SYMLINK/bin/automake-1.11 /usr/local/bin/automake-1.11
sudo ln -sf $SYMLINK/bin/aclocal-1.16 /usr/local/bin/aclocal
sudo ln -sf $SYMLINK/bin/aclocal-1.16 /usr/local/bin/aclocal-1.16
sudo ln -sf $SYMLINK/bin/aclocal-1.15 /usr/local/bin/aclocal-1.15
sudo ln -sf $SYMLINK/bin/aclocal-1.14 /usr/local/bin/aclocal-1.14
sudo ln -sf $SYMLINK/bin/aclocal-1.13 /usr/local/bin/aclocal-1.13
sudo ln -sf $SYMLINK/bin/aclocal-1.11 /usr/local/bin/aclocal-1.11
sudo ln -sf $SYMLINK/bin/autom4te /usr/local/bin/autom4te
sudo ln -sf $SYMLINK/bin/autoreconf /usr/local/bin/autoreconf
sudo ln -sf $SYMLINK/bin/autoheader /usr/local/bin/autoheader

sudo ln -sf $SYMLINK/bin/libtoolize /usr/local/bin/libtoolize

sudo ln -sf /usr/local/bin/gcc /usr/local/bin/darwinx-gcc

BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-2.69.tar.gz
tar xzf autoconf-2.69.tar.gz
cd autoconf-2.69
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
export PATH=$PATH:$PREFIX/bin

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.11.6.tar.gz
tar xzf automake-1.11.6.tar.gz
cd automake-1.11.6
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.13.tar.gz
tar xzf automake-1.13.tar.gz
cd automake-1.13
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/automake/automake-1.14.1.tar.gz
tar xzf automake-1.14.1.tar.gz
cd automake-1.14.1
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT
curl -OL http://ftpmirror.gnu.org/libtool/libtool-2.4.tar.gz
tar xzf libtool-2.4.tar.gz
cd libtool-2.4
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

sudo ln -s $SYMLINK/bin/autoconf /usr/local/bin/autoconf
sudo ln -s $SYMLINK/bin/automake-1.14 /usr/local/bin/automake
sudo ln -s $SYMLINK/bin/automake-1.14 /usr/local/bin/automake-1.14
sudo ln -s $SYMLINK/bin/automake-1.13 /usr/local/bin/automake-1.13
sudo ln -s $SYMLINK/bin/automake-1.11 /usr/local/bin/automake-1.11
sudo ln -s $SYMLINK/bin/aclocal-1.14 /usr/local/bin/aclocal
sudo ln -s $SYMLINK/bin/aclocal-1.13 /usr/local/bin/aclocal-1.14
sudo ln -s $SYMLINK/bin/aclocal-1.13 /usr/local/bin/aclocal-1.13
sudo ln -s $SYMLINK/bin/aclocal-1.11 /usr/local/bin/aclocal-1.11
sudo ln -s $SYMLINK/bin/autom4te /usr/local/bin/autom4te
sudo ln -s $SYMLINK/bin/autoreconf /usr/local/bin/autoreconf
sudo ln -s $SYMLINK/bin/autoheader /usr/local/bin/autoheader
sudo ln -s $SYMLINK/bin/libtoolize /usr/local/bin/libtoolize

sudo ln -s /usr/local/bin/gcc /usr/local/bin/darwinx-gcc

BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -OL http://tukaani.org/xz/xz-5.0.5.tar.gz
tar xzf xz-5.0.5.tar.gz
cd xz-5.0.5
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/xz /usr/local/bin/xz

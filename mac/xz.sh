BUILD_ROOT=~/AppboxBuild

NAME=AppBox
VERSION=1.0.0
PREFIX=/Library/Frameworks/$NAME.framework/Versions/$VERSION
SYMLINK=/Library/Frameworks/$NAME.framework/Versions/Current

cd $BUILD_ROOT
curl -OL http://tukaani.org/xz/xz-5.0.5.tar.gz
tar xzf xz-5.0.5.tar.gz
cd xz-5.0.5
CFLAGS="-m64 -arch x86_64" CXXFLAGS="-m64 -arch x86_64" LDFLAGS="-arch x86_64" ./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -s $SYMLINK/bin/xz /usr/local/bin/xz

SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
if [[ ! -f xz-5.0.5.tar.gz ]]; then
curl -OL http://tukaani.org/xz/xz-5.0.5.tar.gz
fi

if [[ -d xz-5.0.5 ]]; then
        rm -rf xz-5.0.5
fi

tar xzf xz-5.0.5.tar.gz

cd xz-5.0.5
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install
sudo ln -sf $SYMLINK/bin/xz /usr/local/bin/xz

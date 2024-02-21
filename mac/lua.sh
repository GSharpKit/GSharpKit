SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
if [[ ! -f lua-5.4.6.tar.gz ]]; then
curl -OL https://www.lua.org/ftp/lua-5.4.6.tar.gz
fi

if [[ -d lua-5.4.6 ]]; then
        rm -rf lua-5.4.6
fi

tar xzf lua-5.4.6.tar.gz

cd lua-5.4.6
INSTALL_TOP=$PREFIX make
sudo make install INSTALL_TOP=$PREFIX
sudo cp $SCRIPT_ROOT/lua.pc $PREFIX/lib/pkgconfig/

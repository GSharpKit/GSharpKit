SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
if [[ ! -f libgpg-error-1.47.tar.bz2 ]]; then
curl -OL https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.47.tar.bz2
fi
if [[ ! -f libgcrypt-1.10.3.tar.bz2 ]]; then
curl -OL https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.10.3.tar.bz2
fi

if [[ -d libgpg-error-1.47 ]]; then
        rm -rf libgpg-error-1.47
fi
if [[ -d libgcrypt-1.10.3 ]]; then
        rm -rf libgcrypt-1.10.3
fi

tar xfz libgpg-error-1.47.tar.bz2
tar xfz libgcrypt-1.10.3.tar.bz2

cd $BUILD_ROOT/libgpg-error-1.47
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

cd $BUILD_ROOT/libgcrypt-1.10.3
./configure --prefix=$PREFIX --exec-prefix=$PREFIX
make
sudo make install

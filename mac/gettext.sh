BUILD_ROOT=~/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
curl -o gettext-0.18.3.1.tar.gz http://ftp.gnu.org/pub/gnu/gettext/gettext-0.18.3.1.tar.gz

cd $BUILD_ROOT
tar xfz gettext-0.18.3.1.tar.gz
cd gettext-0.18.3.1
./configure --prefix=$PREFIX
make
sudo make install

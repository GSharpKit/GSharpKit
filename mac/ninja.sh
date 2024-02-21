SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

cd $BUILD_ROOT
git clone https://github.com/ninja-build/ninja.git
cd ninja
git checkout release

./configure.py --bootstrap
cmake -Bbuild-cmake -H.
cmake --build build-cmake

sudo cp build-cmake/ninja $SYMLINK/bin/

sudo ln -sf $SYMLINK/bin/ninja /usr/local/bin/ninja

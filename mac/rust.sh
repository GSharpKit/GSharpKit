SCRIPT_ROOT=`pwd`
BUILD_ROOT=$SCRIPT_ROOT/GSharpKitBuild

NAME=GSharpKit
PREFIX=/Library/$NAME
SYMLINK=/Library/$NAME

VERSION=1.75.0

cd $BUILD_ROOT

if [[ ! -f "rust-$VERSION.tar.gz" ]]; then
	curl -OL https://github.com/rust-lang/rust/archive/refs/tags/$VERSION.tar.gz
fi
rm -rf rust-$VERSION
tar xzf rust-$VERSION.tar.gz
cd rust-$VERSION
./configure --prefix=$PREFIX --enable-cargo-native-static --enable-clang --enable-full-bootstrap --enable-missing-tools
cp Cargo.* src/tools/cargo/
make
sudo make install
cd ..
#sudo ln -sf $SYMLINK/bin/cmake /usr/local/bin/cmake
#sudo mkdir -p $PREFIX/share/cross
#sudo cp toolchain-darwinx.cmake $PREFIX/share/cross/

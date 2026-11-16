%{?ucrt_package_header}

Name:           ucrt-webkit2gtk3
Version:        2.54.2
Release:        1%{?dist}
Summary:        MinGW Windows GTK+ Web content engine library

Group:          Development/Libraries
License:        LGPLv2+ and BSD
URL:            http://webkit.org/

Source0:        http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz

Patch:          0001-MinGW-platform-port-foundation.patch
Patch:          0002-MinGW-toolchain-and-thirdparty.patch
Patch:          0003-MinGW-webkit-source-portability-guards.patch
Patch:          0004-MinGW-linkage-and-symbol-visibility.patch
Patch:          0005-MinGW-gobject-introspection-and-dump-program.patch  
Patch:          0006-MinGW-UCRT.patch          

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  perl-Math-BigInt

BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-fontconfig
BuildRequires:  ucrt64-freetype
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-egl-headers
BuildRequires:  ucrt64-gstreamer1
BuildRequires:  ucrt64-gstreamer1-plugins-base
BuildRequires:  ucrt64-gtk3
BuildRequires:  ucrt64-libidn
BuildRequires:  ucrt64-libsoup3
BuildRequires:  ucrt64-libnghttp2
BuildRequires:  ucrt64-libwebp
BuildRequires:  ucrt64-libxml2
BuildRequires:  ucrt64-libxslt
BuildRequires:  ucrt64-winpthreads
BuildRequires:  ucrt64-sqlite

%description
WebKitGTK+ is an open-source Web content engine library.
This package contains the shared libraries for the WebKit GTK+ port
as well as the sample GtkLauncher tool.

This is the MinGW port of WebKitGTK+ for GTK+ 3.

%package -n ucrt64-webkit2gtk3
Summary:        MinGW Windows web content engine library

%description -n ucrt64-webkit2gtk3
WebKitGTK+ is an open-source Web content engine library.
This package contains the shared libraries for the WebKit GTK+ port
as well as the sample GtkLauncher tool.

This is the MinGW port of WebKitGTK+ for GTK+ 3.

%{?ucrt_debug_package}

%prep
%autosetup -p1 -n "webkitgtk-%{version}"

%build
mkdir build_ucrt
pushd build_ucrt
%global ucrt64_cflags %(echo %{ucrt64_cflags} | sed 's/-g /-g1 /') -Wl,--strip-debug
ucrt64-cmake \
	-GNinja \
	-DPORT=GTK \
	-DUSE_GTK4=OFF \
	-DENABLE_TOUCH_EVENTS=OFF \
	-DENABLE_TOOLS=OFF \
	-DENABLE_API_TESTS=OFF \
	-DUSE_SYSTEM_SYSPROF_CAPTURE=OFF \
	-DUSE_SYSPROF_CAPTURE=OFF \
	-DENABLE_GAMEPAD=OFF \
	-DUSE_LIBSECRET=OFF \
	-DENABLE_DOCUMENTATION=OFF \
	-DUSE_LIBDRM=OFF \
	-DENABLE_SPEECH_SYNTHESIS=OFF \
	-DENABLE_SPELLCHECK=OFF \
	-DUSE_GSTREAMER_WEBRTC=ON \
	-DUSE_GSTREAMER_GL=OFF \
	-DUSE_LIBHYPHEN=OFF \
	-DUSE_WOFF2=OFF \
	-DENABLE_JOURNALD_LOG=OFF \
	-DUSE_LIBBACKTRACE=OFF \
	-DUSE_JPEGXL=OFF \
	-DUSE_AVIF=OFF \
	-DUSE_LCMS=OFF \
	-DUNIFDEF_EXECUTABLE=/usr/bin/unifdef ..
ninja
popd


%install
pushd build_ucrt
DESTDIR=%{buildroot} ninja install
popd

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n ucrt64-webkit2gtk3
%{_docdir}/ucrt64-webkitgtk3/
%{ucrt64_bindir}/jsc-3.exe
%{ucrt64_bindir}/GtkLauncher-3.exe
%{ucrt64_bindir}/libjavascriptcoregtk-3.0-0.dll
%{ucrt64_bindir}/libwebkitgtk-3.0-0.dll
%{ucrt64_includedir}/webkitgtk-3.0/
%{ucrt64_libdir}/libjavascriptcoregtk-3.0.dll.a
%{ucrt64_libdir}/libwebkitgtk-3.0.dll.a
%{ucrt64_libdir}/pkgconfig/javascriptcoregtk-3.0.pc
%{ucrt64_libdir}/pkgconfig/webkitgtk-3.0.pc
%{ucrt64_datadir}/webkitgtk-3.0/
%{ucrt64_datadir}/locale/
%{ucrt64_datadir}/gtk-doc/

%changelog
* Mon Nov 16 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.54.2-1
- Initial ucrt-webkit2gtk3 packaging.

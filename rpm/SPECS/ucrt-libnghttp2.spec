%global debug_package %{nil}
%global with_http3 0

%{?ucrt_package_header}

Summary: Experimental HTTP/2 client, server and proxy
Name: ucrt-libnghttp2
Version: 1.68.0
Release: 4%{?dist}

# Parts of ruby bindings are additionally under GPL-2.0-or-later, MIT and
# HPND-Kevlin-Henney but they are NOT shipped.
License: MIT

URL: https://nghttp2.org/
Source0: https://github.com/tatsuhiro-t/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz

BuildRequires: ucrt64-filesystem >= 107
BuildRequires: ucrt64-gcc-c++
BuildRequires: ucrt64-binutils
#BuildRequires: ucrt64-c-ares
BuildRequires: ucrt64-libxml2
BuildRequires: ucrt64-openssl
#BuildRequires: ucrt64-python3
BuildRequires: ucrt64-zlib

%description
This package contains the HTTP/2 client, server and proxy programs.

%package -n ucrt64-libnghttp2
Summary: A library implementing the HTTP/2 protocol

%description -n ucrt64-libnghttp2
libnghttp2 is a library implementing the Hypertext Transfer Protocol
version 2 (HTTP/2) protocol in C.

This is the MinGW cross-compiled Windows library.

%{?ucrt_debug_package}

%prep
%autosetup -p1 -n nghttp2-%{version}


%build
%ucrt64_configure --disable-hpack-tools --disable-static
%ucrt64_make

%install
%ucrt64_make install DESTDIR=%{buildroot}

rm -f "${buildroot}%{ucrt64_libdir}/libnghttp2.la"
rm -f "%{buildroot}%{ucrt64_datadir}/doc/nghttp2/README.rst"
rm -r "%{buildroot}%{ucrt64_mandir}/man1"

%files -n ucrt64-libnghttp2
%license COPYING
%doc README.rst
%{ucrt64_bindir}/libnghttp2-14.dll
%{ucrt64_libdir}/libnghttp2.dll.a
%{ucrt64_libdir}/pkgconfig/libnghttp2.pc
%{ucrt64_includedir}/nghttp2/

%changelog
* Thu Oct 15 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.6.6-1
- Initial import.

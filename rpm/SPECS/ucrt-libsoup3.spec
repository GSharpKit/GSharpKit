%global debug_package %{nil}
%global glib2_version 2.70.0

%{?ucrt_package_header}

Name:    ucrt-libsoup3
Version: 3.6.6
Release: %autorelease
Summary: Soup, an HTTP library implementation

License: LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://wiki.gnome.org/Projects/libsoup
Source0: https://download.gnome.org/sources/libsoup/3.6/libsoup-%{version}.tar.xz

# Downstream patch, needed due to glib2 gnutls-hmac.patch
Patch:   no-ntlm-in-fips-mode.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2433867
Patch:   0001-CVE-2026-1539-Also-remove-Proxy-Authorization-header-on-cross-origin-redirect.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2452935
Patch:   0002-CVE-2026-5119-cookies-do-not-send-cookies-to-HTTP-proxy-for-HTTPS-request.patch

BuildRequires: ucrt64-filesystem >= 107
BuildRequires: ucrt64-gcc
BuildRequires: ucrt64-binutils
BuildRequires: ucrt64-glib2
BuildRequires: ucrt64-brotli
BuildRequires: ucrt64-libpsl
BuildRequires: ucrt64-sqlite
BuildRequires: ucrt64-libnghttp2

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it), but the SOAP parts were removed
long ago.

%package -n ucrt64-libsoup3
Summary: MinGW library for HTTP functionality
Recommends: ucrt64-glib-networking

%description -n ucrt64-libsoup3
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of libsoup3

%{?ucrt_debug_package}

%prep
%autosetup -p1 -n libsoup-%{version}


%build
mkdir build_ucrt
pushd build_ucrt
%ucrt64_meson \
    -Ddocs=disabled \
    -Dintrospection=disabled \
    -Dtests=false \
    -Dtls_check=false \
    -Dvapi=disabled
ninja
popd


%install
pushd build_ucrt
DESTDIR=%{buildroot} ninja install
popd
install -m 644 -D tests/libsoup.supp %{buildroot}%{ucrt64_datadir}/libsoup-3.0/libsoup.supp

%files -n ucrt64-libsoup3
%license COPYING
%doc README NEWS AUTHORS
%{ucrt64_bindir}/libsoup-3.0-0.dll
%{ucrt64_includedir}/libsoup-3.0
%{ucrt64_libdir}/libsoup-3.0.dll.a
%{ucrt64_libdir}/pkgconfig/libsoup-3.0.pc
%{ucrt64_datadir}/libsoup-3.0/libsoup.supp
%{ucrt64_datadir}/locale

%changelog
* Thu Oct 15 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.6.6-1
- Initial import.

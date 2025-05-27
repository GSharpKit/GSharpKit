Name:           darwinx-gnutls
Version:        3.8.9
Release:        1%{?dist}
Summary:        GnuTLS TLS/SSL encryption library

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnutls.org/
Source0:        gnutls-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-zlib
BuildRequires:  darwinx-libgcrypt
BuildRequires:  darwinx-libtasn1
BuildRequires:  darwinx-p11-kit
BuildRequires:  darwinx-gmp
BuildRequires:  darwinx-nettle
BuildRequires:  darwinx-libunistring
BuildRequires:  pkgconfig

Requires:  darwinx-libgcrypt
Requires:  darwinx-libtasn1
Requires:  darwinx-p11-kit
Requires:  darwinx-gmp
Requires:  darwinx-nettle
Requires:  darwinx-libunistring


%description
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for Darwin.


%prep
%setup -q -n gnutls-%{version}

%build
%{_darwinx_configure} \
  --disable-static \
  --disable-cxx \
  --disable-libdane \
  --disable-guile \
  --with-libgcrypt \
  --disable-srp-authentication \
  --disable-hardware-acceleration

%{_darwinx_make}
# %{?_smp_mflags} doesn't build correctly.


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# Remove info and man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_infodir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/certtool
%{_darwinx_bindir}/gnutls-cli
%{_darwinx_bindir}/gnutls-cli-debug
%{_darwinx_bindir}/gnutls-serv
%{_darwinx_bindir}/ocsptool
%{_darwinx_bindir}/p11tool
%{_darwinx_bindir}/psktool
%{_darwinx_libdir}/libgnutls.*.dylib
%{_darwinx_libdir}/libgnutls.dylib
#%{_darwinx_libdir}/libgnutls-openssl.*.dylib
#%{_darwinx_libdir}/libgnutls-openssl.dylib
#%{_darwinx_libdir}/libgnutlsxx.*.dylib
#%{_darwinx_libdir}/libgnutlsxx.dylib
#%{_darwinx_libdir}/gnutls/libpkcs11mock1.so
%{_darwinx_libdir}/pkgconfig/gnutls.pc
%{_darwinx_includedir}/gnutls/
%{_darwinx_datadir}/locale

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.3.1-1
- Initial RPM release.


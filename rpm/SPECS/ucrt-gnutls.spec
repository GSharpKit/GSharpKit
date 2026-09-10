%global debug_package %{nil}

%{?ucrt_package_header}

Name:           ucrt-gnutls
Version:        3.8.13
Release:        1%{?dist}
Summary:        GnuTLS TLS/SSL encryption library

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnutls.org/
Source0:        gnutls-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ucrt64-filesystem >= 7
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-zlib
BuildRequires:  ucrt64-libgcrypt
BuildRequires:  ucrt64-libtasn1
BuildRequires:  ucrt64-p11-kit
BuildRequires:  ucrt64-gmp
BuildRequires:  ucrt64-nettle
BuildRequires:  ucrt64-libunistring
BuildRequires:  pkgconfig

Requires:  ucrt64-libgcrypt
Requires:  ucrt64-libtasn1
Requires:  ucrt64-p11-kit
Requires:  ucrt64-gmp
Requires:  ucrt64-nettle
Requires:  ucrt64-libunistring


%description
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for Darwin.

%package -n ucrt64-gnutls
Summary: %{summary}
Requires: publicsuffix-list

%description -n ucrt64-gnutls
GnuTLS TLS/SSL encryption library.  This library is cross-compiled
for Darwin.

%{?ucrt_debug_package}

%prep
%setup -q -n gnutls-%{version}

%build
export UCRT64_CFLAGS="-O2 -g -fno-optimize-strlen"
%{ucrt64_configure} \
  --disable-static \
  --disable-cxx \
  --disable-libdane \
  --disable-guile \
  --with-libgcrypt \
  --disable-srp-authentication \
  --disable-hardware-acceleration \
  --disable-tests \
  --disable-tools \
  --disable-doc

%{ucrt64_make}
# %{?_smp_mflags} doesn't build correctly.


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# Remove info and man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{ucrt64_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{ucrt64_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{ucrt64_infodir}
rm -rf $RPM_BUILD_ROOT%{ucrt64_mandir}

rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/libgnutls*.dll.a
mv $RPM_BUILD_ROOT%{ucrt64_libdir}/libgnutls* $RPM_BUILD_ROOT%{ucrt64_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files -n ucrt64-gnutls
%defattr(-,root,wheel)
%{ucrt64_bindir}/libgnutls*.dll
%{ucrt64_bindir}/libgnutls*.def
%{ucrt64_libdir}/pkgconfig/gnutls.pc
%{ucrt64_includedir}/gnutls/

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.3.1-1
- Initial RPM release.


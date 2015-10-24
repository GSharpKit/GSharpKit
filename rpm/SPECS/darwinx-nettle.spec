Name:           darwinx-nettle
Version:        2.7.1
Release:        1%{?dist}
Summary:        A low-level cryptographic library
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://ftp.gnu.org/gnu/nettle/
Source0:        nettle-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libgpg-error
BuildRequires:  darwinx-libgcrypt >= 1.5.2
BuildRequires:  darwinx-gmp
BuildRequires:  darwinx-gettext

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig


%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package static
Summary:        A low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.


%prep
%setup -q -n nettle-%{version}

%build
%{_darwinx_configure} --disable-assembler
%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING.LIB
%{_darwinx_bindir}/nettle-hash
%{_darwinx_bindir}/nettle-lfib-stream
%{_darwinx_bindir}/pkcs1-conv
%{_darwinx_bindir}/sexp-conv
%{_darwinx_includedir}/nettle
%{_darwinx_libdir}/libhogweed.2.5.dylib
%{_darwinx_libdir}/libhogweed.2.dylib
%{_darwinx_libdir}/libhogweed.dylib
%{_darwinx_libdir}/libnettle.4.7.dylib
%{_darwinx_libdir}/libnettle.4.dylib
%{_darwinx_libdir}/libnettle.dylib
%{_darwinx_libdir}/pkgconfig/hogweed.pc
%{_darwinx_libdir}/pkgconfig/nettle.pc

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libhogweed.a
%{_darwinx_libdir}/libnettle.a


%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.6-1
- Initial RPM release.


Name:           darwinx-libxml2
Version:        2.10.4
Release:        1%{?dist}
Summary:        libxml2 is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://xmlsoft.org/
Source0:        ftp://xmlsoft.org/libxml2/libxml2-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext

Requires:       darwinx-filesystem >= 18

%description
libxml2 is the official PNG reference library.

%prep
%setup -q -n libxml2-v%{version}

%build
NOCONFIGURE=yes sh autogen.sh 
%{_darwinx_configure} \
	--without-iconv \
	--without-python \
	--without-lzma \
	--without-zlib

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/xml2-config
%{_darwinx_bindir}/xmlcatalog
%{_darwinx_bindir}/xmllint
%{_darwinx_libdir}/cmake/libxml2/libxml2-config.cmake
%{_darwinx_libdir}/libxml2.dylib
%{_darwinx_libdir}/libxml2.2.dylib
%{_darwinx_libdir}/pkgconfig/libxml-2.0.pc
%{_darwinx_includedir}/libxml2
%{_darwinx_datadir}/aclocal/libxml.m4

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release

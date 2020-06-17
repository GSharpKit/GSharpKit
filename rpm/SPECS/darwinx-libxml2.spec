Name:           darwinx-libxml2
Version:        2.9.10
Release:        1%{?dist}
Summary:        libxml2 is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://xmlsoft.org/
Source0:        ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext

Requires:       darwinx-filesystem >= 18

%description
libxml2 is the official PNG reference library.

%package static
Summary:        libxml2 is the official PNG reference library.
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the libxml2 library.

%prep
%setup -q -n libxml2-%{version}


%build
%{_darwinx_configure} --without-lzma
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}
rm -rf $RPM_BUILD_ROOT/Library/Python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/xml2-config
%{_darwinx_bindir}/xmlcatalog
%{_darwinx_bindir}/xmllint
%{_darwinx_libdir}/libxml2.dylib
%{_darwinx_libdir}/libxml2.la
%{_darwinx_libdir}/libxml2.*.dylib
%{_darwinx_libdir}/xml2Conf.sh
%{_darwinx_libdir}/pkgconfig/libxml-2.0.pc
%{_darwinx_libdir}/cmake/libxml2/libxml2-config.cmake
%{_darwinx_includedir}/libxml2

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libxml2.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.9.2-1
- Initial RPM release

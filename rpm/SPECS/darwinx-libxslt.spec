Name:           darwinx-libxslt
Version:        1.1.39
Release:        1%{?dist}
Summary:        libxslt is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            ftp://xmlsoft.org/libxslt/
Source0:        libxslt-v%{version}.tar.gz
Patch0:		libxslt-v1.1.39-static.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext

Requires:  	darwinx-filesystem >= 18

%description
libxslt is the official PNG reference library.

%prep
%setup -q -n libxslt-v%{version}
%patch 0 -p1

%build
NOCONFIGURE=yes sh autogen.sh
%{_darwinx_configure} \
	--disable-static \
	--without-python
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/python*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/xslt-config
%{_darwinx_bindir}/xsltproc
%{_darwinx_libdir}/libxslt.dylib
%{_darwinx_libdir}/libxslt.*.dylib
%{_darwinx_libdir}/libexslt.dylib
%{_darwinx_libdir}/libexslt.*.dylib
%{_darwinx_libdir}/xsltConf.sh
%{_darwinx_libdir}/pkgconfig/libxslt.pc
%{_darwinx_libdir}/pkgconfig/libexslt.pc
%{_darwinx_includedir}/libxslt
%{_darwinx_includedir}/libexslt
%dir %{_darwinx_libdir}/cmake/libxslt
%{_darwinx_libdir}/cmake/libxslt/*

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.1.28-1
- Initial RPM release

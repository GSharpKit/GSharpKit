Name:           darwinx-libxslt
Version:        1.1.28
Release:        1%{?dist}
Summary:        libxslt is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://prdownloads.sourceforge.net/libxslt/
Source0:        libxslt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
libxslt is the official PNG reference library.

%package static
Summary:        libxslt is the official PNG reference library.
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the libxslt library.

%prep
%setup -q -n libxslt-%{version}


%build
%{_darwinx_configure}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/python*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/xslt-config
%{_darwinx_bindir}/xsltproc
%{_darwinx_libdir}/libxslt.dylib
%{_darwinx_libdir}/libxslt.la
%{_darwinx_libdir}/libxslt.*.dylib
%{_darwinx_libdir}/libexslt.la
%{_darwinx_libdir}/libexslt.dylib
%{_darwinx_libdir}/libexslt.*.dylib
%{_darwinx_libdir}/xsltConf.sh
%{_darwinx_libdir}/pkgconfig/libxslt.pc
%{_darwinx_libdir}/pkgconfig/libexslt.pc
%{_darwinx_includedir}/libxslt
%{_darwinx_includedir}/libexslt

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libxslt.a
%{_darwinx_libdir}/libexslt.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.0.13-1
- Initial RPM release

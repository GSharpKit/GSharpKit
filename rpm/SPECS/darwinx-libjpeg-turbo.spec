Name:           darwinx-libjpeg-turbo
Version:        1.3.1
Release:        1%{?dist}
Summary:        libjpeg-turbo is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://libjpeg-turbo.virtualgl.org/
Source0:        libjpeg-turbo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
libjpeg-turbo is the official PNG reference library.

%package static
Summary:        libjpeg-turbo is the official PNG reference library.
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the libjpeg-turbo library.

%prep
%setup -q -n libjpeg-turbo-%{version}


%build
%{_darwinx_configure} --without-simd
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/cjpeg
%{_darwinx_bindir}/djpeg
%{_darwinx_bindir}/jpegtran
%{_darwinx_bindir}/rdjpgcom
%{_darwinx_bindir}/tjbench
%{_darwinx_bindir}/wrjpgcom
%{_darwinx_libdir}/libturbojpeg.dylib
%{_darwinx_libdir}/libjpeg.dylib
%{_darwinx_libdir}/libturbojpeg.*.dylib
%{_darwinx_libdir}/libjpeg.*.dylib
%{_darwinx_libdir}/libturbojpeg.la
%{_darwinx_libdir}/libjpeg.la
%{_darwinx_includedir}/jconfig.h
%{_darwinx_includedir}/jerror.h
%{_darwinx_includedir}/jmorecfg.h
%{_darwinx_includedir}/jpeglib.h
%{_darwinx_includedir}/turbojpeg.h

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libturbojpeg.a
%{_darwinx_libdir}/libjpeg.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.0.13-1
- Initial RPM release

Name:           darwinx-libjpeg-turbo
Version:        3.1.0
Release:        1%{?dist}
Summary:        libjpeg-turbo is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://libjpeg-turbo.virtualgl.org/
Source0:        libjpeg-turbo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
libjpeg-turbo is the official PNG reference library.

%prep
%setup -q -n libjpeg-turbo-%{version}

%build
%darwinx_cmake
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/*.a
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/cmake
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
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
%{_darwinx_includedir}/jconfig.h
%{_darwinx_includedir}/jerror.h
%{_darwinx_includedir}/jmorecfg.h
%{_darwinx_includedir}/jpeglib.h
%{_darwinx_includedir}/turbojpeg.h
%{_darwinx_libdir}/pkgconfig/libjpeg.pc
%{_darwinx_libdir}/pkgconfig/libturbojpeg.pc

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.13-1
- Initial RPM release

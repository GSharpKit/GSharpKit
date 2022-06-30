Name:           darwinx-jasper
Version:        2.0.33
Release:        1%{?dist}
Summary:        The JasPer Project is an JPEG-2000 Part-1 standard

License:        See LICENSE
Group:          Development/Libraries
URL:            https://github.com/jasper-software/jasper/releases
Source0:        jasper-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libjpeg-turbo


%description
The JasPer Project is an JPEG-2000 Part-1 standard

%package static
Summary:        The JasPer Project is an JPEG-2000 Part-1 standard
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
The JasPer Project is an JPEG-2000 Part-1 standard

%prep
%setup -q -n jasper-%{version}


%build
mkdir build_static
cd build_static
%{_darwinx_cmake} -DJAS_ENABLE_SHARED=OFF -DJAS_ENABLE_DOC=OFF
make %{?_smp_mflags}

cd ..
mkdir build_shared
cd build_shared
%{_darwinx_cmake} -DJAS_ENABLE_SHARED=ON -DJAS_ENABLE_DOC=OFF
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd build_static
make DESTDIR=$RPM_BUILD_ROOT install
cd ../build_shared
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_bindir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_libdir}/libjasper.dylib
%{_darwinx_libdir}/libjasper.*.dylib
%{_darwinx_includedir}/jasper/jasper.h
%{_darwinx_includedir}/jasper/jas_*
%{_darwinx_libdir}/pkgconfig/jasper.pc

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libjasper.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.900.1-1
- Initial RPM release

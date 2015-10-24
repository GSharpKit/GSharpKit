Name:           darwinx-jasper
Version:        1.900.1
Release:        1%{?dist}
Summary:        The JasPer Project is an JPEG-2000 Part-1 standard

License:        See LICENSE
Group:          Development/Libraries
URL:            http://www.ece.uvic.ca/~frodo/jasper/
Source0:        jasper-%{version}.zip
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
%{_darwinx_configure} \
	--enable-shared \
	--enable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_bindir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_libdir}/libjasper.dylib
%{_darwinx_libdir}/libjasper.*.dylib
%{_darwinx_libdir}/libjasper.la
%{_darwinx_includedir}/jasper/jasper.h
%{_darwinx_includedir}/jasper/jas_*

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libjasper.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.0.13-1
- Initial RPM release

Name:           darwinx-zlib
Version:        1.2.13
Release:        1%{?dist}
Summary:        A Massively Spiffy Yet Delicately Unobtrusive Compression Library

License:        As-is
Group:          Development/Libraries
URL:            https://zlib.net
Source0:        https://zlib.net/fossils/zlib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
A Massively Spiffy Yet Delicately Unobtrusive Compression Library

%prep
%setup -q -n zlib-%{version}

%build
%{_darwinx_env}
./configure --prefix=%{_darwinx_prefix}

%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_darwinx_includedir}/*
%{_darwinx_libdir}/libz.*.dylib
%{_darwinx_libdir}/libz.dylib
%{_darwinx_libdir}/pkgconfig/*

%changelog
* Sat Jan  6 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.8-1
- Initial RPM release.


Name:           darwinx-expat
Version:        2.5.0
Release:        1%{?dist}
Summary:        Welcome to Expat, a stream-oriented XML parser library written in C.

License:        As-is
Group:          Development/Libraries
URL:            https://github.com/libexpat/libexpat
Source0:        https://github.com/libexpat/libexpat/releases/download/R_2_5_0/expat-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
Welcome to Expat, a stream-oriented XML parser library written in C.

%prep
%setup -q -n expat-%{version}

%build
%{_darwinx_configure}

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
%{_darwinx_libdir}/libexpat.*.dylib
%{_darwinx_libdir}/libexpat.dylib
%{_darwinx_libdir}/pkgconfig/*
%dir %{_darwinx_libdir}/cmake/expat-%{version}
%{_darwinx_libdir}/cmake/expat-%{version}/*

%changelog
* Sat Jan  6 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.8-1
- Initial RPM release.


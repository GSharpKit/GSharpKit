Name:           darwinx-libiconv
Version:        1.17
Release:        1%{?dist}
Summary:        International text is mostly encoded in Unicode

License:        LGPL
Group:          Development/Libraries
URL:            https://www.gnu.org/software/libiconv/
Source0:        https://ftp.gnu.org/pub/gnu/libiconv/libiconv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
International text is mostly encoded in Unicode

%prep
%setup -q -n libiconv-%{version}

%build
%{_darwinx_configure} \
	--disable-static

%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/*
%{_darwinx_includedir}/*
%{_darwinx_libdir}/libcharset.*.dylib
%{_darwinx_libdir}/libcharset.dylib
%{_darwinx_libdir}/libiconv.*.dylib
%{_darwinx_libdir}/libiconv.dylib
#{_darwinx_libdir}/pkgconfig/*

%changelog
* Sat Jan  6 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.8-1
- Initial RPM release.


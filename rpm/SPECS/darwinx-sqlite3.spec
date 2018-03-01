%define ver 3200100

Name:           darwinx-sqlite3
Version:        3.20.1.0
Release:        1%{?dist}
Summary:        SQL database engine.

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            https://www.sqlite.org/
Source0:        sqlite-autoconf-%{ver}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 12
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
SQL database engine.

%prep
%setup -q -n sqlite-autoconf-%{ver}

%build
%{_darwinx_configure} \
  --disable-static

%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_darwinx_datadir}/info/dir

# Remove info and man pages which duplicate stuff in Fedora already.
rm -rf $RPM_BUILD_ROOT%{_darwinx_infodir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_darwinx_bindir}/sqlite3
%{_darwinx_libdir}/libsqlite3.*.dylib
%{_darwinx_libdir}/libsqlite3.dylib
%{_darwinx_libdir}/libsqlite3.la
%{_darwinx_libdir}/pkgconfig/sqlite3.pc
%{_darwinx_includedir}/

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.6-1
- Initial RPM release.


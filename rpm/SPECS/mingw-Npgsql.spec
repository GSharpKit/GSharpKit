%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Npgsql
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-Npgsql
Version:        6.0.2
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:      mingw64-System.Common

%description -n mingw64-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.


%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > Npgsql.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires: System.Common System.Security
Version: %{version}
Libs: -r:${libdir}/Npgsql.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Npgsql.dll
%{mingw64_datadir}/pkgconfig/Npgsql.pc


%changelog
* Mon Oct 7 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.1.1-1
- Update to 4.1.1

* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.2-1
- Update to 4.0.2

* Fri Jun 16 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.4-1
- Rename RPM package to mingw-Npgsql
- Updated to use NuGet version

* Thu Feb 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.2.4.1-1
- Update to 2.2.4.1

* Wed Jan 2 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.0.14.3-1
- Initial version

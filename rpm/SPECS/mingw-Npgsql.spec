%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Npgsql
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 4.0.0.0

Name:           mingw-Npgsql
Version:        4.0.3
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

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono-core

Obsoletes:      mingw32-mono-data-npgsql
Provides:       mingw32-mono-data-npgsql

%description -n mingw32-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono-core

Obsoletes:      mingw64-mono-data-npgsql
Provides:       mingw64-mono-data-npgsql

%description -n mingw64-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.


%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > Npgsql32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:Facades/netstandard.dll -r:${libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll -r:${libdir}/mono/Npgsql/Npgsql.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll
Cflags:
EOF

cat > Npgsql64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:Facades/netstandard.dll -r:${libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll -r:${libdir}/mono/Npgsql/Npgsql.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Threading.Tasks.Extensions.4.5.0/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll -package System.Threading.Tasks.Extensions -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 System.Runtime.CompilerServices.Unsafe.4.5.0/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Npgsql32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Npgsql.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Threading.Tasks.Extensions.4.5.0/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll -package System.Threading.Tasks.Extensions -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.Runtime.CompilerServices.Unsafe.4.5.0/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Npgsql64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Npgsql.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/Npgsql/Npgsql.dll
%{mingw32_prefix}%{libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
%{mingw32_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{mingw32_datadir}/pkgconfig/Npgsql.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/Npgsql/Npgsql.dll
%{mingw64_prefix}%{libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
%{mingw64_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{mingw64_datadir}/pkgconfig/Npgsql.pc


%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.2-1
- Update to 4.0.2

* Fri Jun 16 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.4-1
- Rename RPM package to mingw-Npgsql
- Updated to use NuGet version

* Thu Feb 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.2.4.1-1
- Update to 2.2.4.1

* Wed Jan 2 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.0.14.3-1
- Initial version

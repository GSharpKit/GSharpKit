%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Npgsql
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-Npgsql
Version:        5.0.5
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
Obsoletes:      mingw32-mono-data-npgsql
Provides:       mingw32-mono-data-npgsql

%description -n mingw32-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Obsoletes:      mingw64-mono-data-npgsql
Provides:       mingw64-mono-data-npgsql

%description -n mingw64-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.


%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}
nuget install Microsoft.Bcl.AsyncInterfaces -Version 1.1.0
nuget install System.Memory -Version 4.5.3
nuget install System.Text.Json -Version 4.6.0
nuget install System.Threading.Channels -Version 4.7.0
nuget install System.Threading.Tasks.Extensions -Version 4.5.3

cat > Npgsql32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:${libdir}/Npgsql.dll -r:${libdir}/Microsoft.Bcl.AsyncInterfaces.dll -r:${libdir}/System.Memory.dll -r:${libdir}/System.Text.Json.dll -r:${libdir}/System.Threading.Channels.dll -r:${libdir}/System.Threading.Tasks.Extensions.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll
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
Libs: -r:${libdir}/Npgsql.dll -r:${libdir}/Microsoft.Bcl.AsyncInterfaces.dll -r:${libdir}/System.Memory.dll -r:${libdir}/System.Text.Json.dll -r:${libdir}/System.Threading.Channels.dll -r:${libdir}/System.Threading.Tasks.Extensions.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Microsoft.Bcl.AsyncInterfaces.1.1.0/lib/netstandard2.0/Microsoft.Bcl.AsyncInterfaces.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Memory.4.5.3/lib/netstandard2.0/System.Memory.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Text.Json.4.6.0/lib/netstandard2.0/System.Text.Json.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 System.Threading.Channels.4.7.0/lib/netstandard2.0/System.Threading.Channels.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Threading.Tasks.Extensions.4.5.3/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 System.Runtime.CompilerServices.Unsafe.4.6.0/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Text.Encodings.Web.4.6.0/lib/netstandard2.0/System.Text.Encodings.Web.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Buffers.4.5.0/lib/netstandard2.0/System.Buffers.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/
install -m 644 System.Numerics.Vectors.4.5.0/lib/netstandard2.0/System.Numerics.Vectors.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Npgsql32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Npgsql.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Microsoft.Bcl.AsyncInterfaces.1.1.0/lib/netstandard2.0/Microsoft.Bcl.AsyncInterfaces.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Memory.4.5.3/lib/netstandard2.0/System.Memory.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Text.Json.4.6.0/lib/netstandard2.0/System.Text.Json.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.Threading.Channels.4.7.0/lib/netstandard2.0/System.Threading.Channels.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Threading.Tasks.Extensions.4.5.3/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.Runtime.CompilerServices.Unsafe.4.6.0/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Text.Encodings.Web.4.6.0/lib/netstandard2.0/System.Text.Encodings.Web.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Buffers.4.5.0/lib/netstandard2.0/System.Buffers.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 System.Numerics.Vectors.4.5.0/lib/netstandard2.0/System.Numerics.Vectors.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Npgsql64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Npgsql.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Npgsql.dll
%{mingw32_prefix}%{libdir}/Microsoft.Bcl.AsyncInterfaces.dll
%{mingw32_prefix}%{libdir}/System.Memory.dll
%{mingw32_prefix}%{libdir}/System.Text.Json.dll
%{mingw32_prefix}%{libdir}/System.Threading.Channels.dll
%{mingw32_prefix}%{libdir}/System.Threading.Tasks.Extensions.dll
%{mingw32_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{mingw32_prefix}%{libdir}/System.Text.Encodings.Web.dll
%{mingw32_prefix}%{libdir}/System.Buffers.dll
%{mingw32_prefix}%{libdir}/System.Numerics.Vectors.dll
%{mingw32_datadir}/pkgconfig/Npgsql.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Npgsql.dll
%{mingw64_prefix}%{libdir}/Microsoft.Bcl.AsyncInterfaces.dll
%{mingw64_prefix}%{libdir}/System.Memory.dll
%{mingw64_prefix}%{libdir}/System.Text.Json.dll
%{mingw64_prefix}%{libdir}/System.Threading.Channels.dll
%{mingw64_prefix}%{libdir}/System.Threading.Tasks.Extensions.dll
%{mingw64_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{mingw64_prefix}%{libdir}/System.Text.Encodings.Web.dll
%{mingw64_prefix}%{libdir}/System.Buffers.dll
%{mingw64_prefix}%{libdir}/System.Numerics.Vectors.dll
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

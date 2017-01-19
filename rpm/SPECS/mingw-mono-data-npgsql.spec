%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name mono-data-npgsql
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 3.0.0.0

Name:           mingw-mono-data-npgsql
Version:        3.1.9
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Source0:        npgsql-%{version}.tar.gz
Patch0:         npgsql-3.1.7-async-cancel.patch

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
Requires:       mingw32-mono

%description -n mingw32-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono

%description -n mingw64-%{mingw_pkg_name}
This package contains the ADO.NET Data provider for the PostgreSQL
database.


%prep
%setup -q -n npgsql-%{version}
%patch0 -p1

sed -i -e 's!AssemblyVersion(".*")!AssemblyVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i -e 's!AssemblyFileVersion(".*")!AssemblyFileVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i -e 's!AssemblyInformationalVersion(".*")!AssemblyInformationalVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs

cat > Npgsql32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:System.Data -r:Mono.Security -r:${libdir}/Npgsql.dll
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
Libs: -r:System.Data -r:Mono.Security -r:${libdir}/Npgsql.dll
Cflags:
EOF


%build
cd src/Npgsql
xbuild /tv:4.0 /property:Configuration='Release' Npgsql.csproj

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll.mdb $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Npgsql32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Npgsql.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll.mdb $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Npgsql64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Npgsql.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Npgsql.dll
%{mingw32_prefix}%{libdir}/Npgsql.dll.mdb
%{mingw32_datadir}/pkgconfig/Npgsql.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Npgsql.dll
%{mingw64_prefix}%{libdir}/Npgsql.dll.mdb
%{mingw64_datadir}/pkgconfig/Npgsql.pc


%changelog
* Thu Feb 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.2.4.1-1
- Update to 2.2.4.1

* Wed Jan 2 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.0.14.3-1
- Initial version

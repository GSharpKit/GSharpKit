%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Microsoft.Data.SqlClient 
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-Microsoft.Data.SqlClient
Version:        4.0.0
Release:        2%{?dist}
Summary:        Provides the data provider for MS SQL Server.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Microsoft.Data.SqlClient
Prefix:		/usr
BuildArch:	noarch

%description
Provides the data provider for SQL Server. These classes provide access to versions of 
SQL Server and encapsulate database-specific protocols, including tabular data stream (TDS)

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
Provides the data provider for SQL Server. These classes provide access to versions of
SQL Server and encapsulate database-specific protocols, including tabular data stream (TDS)

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}
nuget install Microsoft.Identity.Client -Version 4.22.0

cat > Microsoft.Data.SqlClient.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Microsoft.Data.SqlClient
Description: Provides classes to use caching facilities.
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Microsoft.Data.SqlClient.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Microsoft.Data.SqlClient.%{version}/runtimes/unix/lib/netstandard2.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 Microsoft.Identity.Client.4.22.0/lib/netstandard1.3/Microsoft.Identity.Client.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Microsoft.Data.SqlClient.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Microsoft.Data.SqlClient.dll
%{mingw64_prefix}%{libdir}/Microsoft.Identity.Client.dll
%{mingw64_datadir}/pkgconfig/Microsoft.Data.SqlClient.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

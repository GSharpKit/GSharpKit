%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 4.0.0.0

Name:           Microsoft.Data.SqlClient
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

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}
nuget install Microsoft.Identity.Client -Version 4.22.0

cat > Microsoft.Data.SqlClient.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Microsoft.Data.SqlClient
Description: Provides classes to use caching facilities.
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Microsoft.Data.SqlClient.dll -r:${libdir}/Microsoft.Identity.Client.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Microsoft.Data.SqlClient.%{version}/runtimes/unix/lib/netstandard2.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 Microsoft.Identity.Client.4.22.0/lib/netstandard1.3/Microsoft.Identity.Client.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Microsoft.Data.SqlClient.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Microsoft.Data.SqlClient.dll
%{_prefix}%{libdir}/Microsoft.Identity.Client.dll
%{_datadir}/pkgconfig/Microsoft.Data.SqlClient.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

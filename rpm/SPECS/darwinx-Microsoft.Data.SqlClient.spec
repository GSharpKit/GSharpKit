%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 4.0.0.0

Name:           darwinx-Microsoft.Data.SqlClient
Version:        4.0.0
Release:        1%{?dist}
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
nuget install Microsoft.Data.SqlClient -Version %{version}

cat > Microsoft.Data.SqlClient.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

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

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Microsoft.Data.SqlClient.%{version}/runtimes/unix/lib/netstandard2.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Microsoft.Data.SqlClient.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Microsoft.Data.SqlClient.dll
%{_darwinx_datadir}/pkgconfig/Microsoft.Data.SqlClient.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

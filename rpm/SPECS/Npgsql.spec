#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib
%define apiversion 3.2.0.0

Name:           Npgsql
Version:        3.2.6
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.0.0
Requires:	mono-data >= 4.0.0

Obsoletes:	mono-data-postgresql
Obsoletes:	mono-data-npgsql

Provides:	mono-data-postgresql
Provides:	mono-data-npgsql


%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > Npgsql.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:System.Data.dll -r:${libdir}/Npgsql/Npgsql.dll -r:${libdir}/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i Npgsql.%{version}/lib/net451/Npgsql.dll -package Npgsql -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Threading.Tasks.Extensions.4.3.0/lib/netstandard1.0/System.Threading.Tasks.Extensions.dll -package System.Threading.Tasks.Extensions -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

#install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/Npgsql
#install -m 644 Npgsql.%{version}/lib/net451/Npgsql.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/Npgsql/
#install -m 644 System.Threading.Tasks.Extensions.4.3.0/lib/netstandard1.0/System.Threading.Tasks.Extensions.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/Npgsql

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/Npgsql/Npgsql.dll
%{_prefix}%{libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
%{_datadir}/pkgconfig/Npgsql.pc

%changelog
* Fri Jun 16 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.4-1
- Rename RPM package to Npgsql
- Updated to use NuGet version
* Mon Jan 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

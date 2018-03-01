#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib
%define apiversion 3.0.0.0

Name:           darwinx-Npgsql
Version:        3.2.6
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-mono-core >= 4.8

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -c %{name}-%{version} -T
nuget install Npgsql -Version %{version}

cat > Npgsql.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:System.Data.dll -r:${libdir}/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll -r:${libdir}/Npgsql/Npgsql.dll
Cflags:
EOF

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/mono/gac
gacutil -i Npgsql.%{version}/lib/net451/Npgsql.dll -package Npgsql -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Threading.Tasks.Extensions.4.3.0/lib/netstandard1.0/System.Threading.Tasks.Extensions.dll -package System.Threading.Tasks.Extensions -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/Npgsql/Npgsql.dll
%{_darwinx_prefix}%{libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%changelog
* Mon Jun 22 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

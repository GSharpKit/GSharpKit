#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-Npgsql
Version:        6.0.3
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:       darwinx-System.Common >= 1.0.0
Requires:       darwinx-System.Security >= 6.0.0

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -c %{name}-%{version} -T
nuget install Npgsql -Version %{version}

cat > Npgsql.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

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

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Npgsql.dll
%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%changelog
* Mon Oct 7 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.1.1-1
- Update to 4.1.1

* Mon Jun 22 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

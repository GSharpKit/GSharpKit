#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:           Npgsql
Version:        6.0.3
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

Requires:	System.Common >= 1.0.0
Requires:	System.Security >= 6.0.0

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > Npgsql.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

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

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Npgsql.dll
%{_datadir}/pkgconfig/Npgsql.pc

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.7
- Updated to use System.Common and System.Security
* Fri Dec 11 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.0.0-1
- Updated to 5.0.0
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.2-1
- Update to 4.0.2
* Fri Jun 16 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.4-1
- Rename RPM package to Npgsql
- Updated to use NuGet version
* Mon Jan 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

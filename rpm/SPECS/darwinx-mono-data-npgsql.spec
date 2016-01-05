#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib
%define apiversion 3.0.0.0

Name:           darwinx-mono-data-npgsql
Version:        3.0.5
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/Npgsql/releases
Source0:        npgsql-%{version}.tar.gz
Patch0:		npgsql-3.0.0-cancel.patch

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-mono >= 4.0

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-mono >= 4.0

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -q -n npgsql-%{version}
%patch0 -p1

sed -i '' 's!AssemblyVersion("0.0.0")!AssemblyVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i '' 's!AssemblyFileVersion("0.0.0")!AssemblyFileVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i '' 's!AssemblyInformationalVersion("0.0.0")!AssemblyInformationalVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs

cat > Npgsql.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}/lib

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:System.Data -r:Mono.Security -r:${libdir}/Npgsql.dll
Cflags:
EOF

%build
pushd packages
nuget install AsyncRewriter -Version 0.6.0
popd
cd src/Npgsql
%{_darwinx_env} ; xbuild /tv:4.0 /property:Configuration='Release' Npgsql.csproj

%install
%{__rm} -rf %{buildroot}


install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll.mdb $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Npgsql.dll
%{_darwinx_prefix}%{libdir}/Npgsql.dll.mdb
%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%changelog
* Mon Jun 22 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

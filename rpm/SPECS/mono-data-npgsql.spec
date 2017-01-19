#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib
%define apiversion 3.0.0.0

Name:           mono-data-npgsql
Version:        3.1.9
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Source0:        npgsql-%{version}.tar.gz
Patch0:		npgsql-3.1.7-async-cancel.patch

Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.0.0
Requires:	mono-data >= 4.0.0

Obsoletes:	mono-data-postgresql

%description
This package contains the ADO.NET Data provider for the PostgreSQL
database.

%prep
%setup -q -n npgsql-%{version}
%patch0 -p1

sed -i -e 's!AssemblyVersion(".*")!AssemblyVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i -e 's!AssemblyFileVersion(".*")!AssemblyFileVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs
sed -i -e 's!AssemblyInformationalVersion(".*")!AssemblyInformationalVersion("%{apiversion}")!g' src/CommonAssemblyInfo.cs

#sed -i -e 's!<WarningLevel>4</WarningLevel>!<WarningLevel>0</WarningLevel>!g' src/Npgsql/Npgsql.csproj

cat > Npgsql.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:System.Data -r:Mono.Security -r:${libdir}/Npgsql.dll
Cflags:
EOF

%build
#pushd packages
#nuget install AsyncRewriter -Version 0.6.0
#popd
cd src/Npgsql
xbuild /tv:4.0 /property:Configuration='Release' Npgsql.csproj

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 src/Npgsql/obj/Release/Npgsql.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%{_prefix}%{libdir}/Npgsql.dll
%{_prefix}%{libdir}/Npgsql.dll.mdb
%{_datadir}/pkgconfig/Npgsql.pc


%changelog
* Mon Jan 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

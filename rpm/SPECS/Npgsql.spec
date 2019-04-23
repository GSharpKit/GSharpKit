#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib

Name:           Npgsql
Version:        4.0.6
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 5.0.0
Requires:	mono-data >= 5.0.0

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
libdir=%{_prefix}%{libdir}

Name: Npgsql
Description: Npgsql - Postgresql database connectivity for C#
Requires:
Version: %{version}
Libs: -r:${libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll -r:${libdir}/mono/System.Buffers/System.Buffers.dll -r:${libdir}/mono/System.Memory/System.Memory.dll -r:${libdir}/System.Numerics.Vectors.dll -r:${libdir}/mono/Npgsql/Npgsql.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll -package Npgsql -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Threading.Tasks.Extensions.4.5.2/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll -package System.Threading.Tasks.Extensions -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Buffers.4.4.0/lib/netstandard2.0/System.Buffers.dll -package System.Buffers -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac
gacutil -i System.Memory.4.5.2/lib/netstandard2.0/System.Memory.dll -package System.Memory -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.Runtime.CompilerServices.Unsafe.4.5.2/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 System.Numerics.Vectors.4.4.0/lib/netstandard2.0/System.Numerics.Vectors.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/Npgsql/Npgsql.dll
%{_prefix}%{libdir}/mono/System.Threading.Tasks.Extensions/System.Threading.Tasks.Extensions.dll
%{_prefix}%{libdir}/mono/System.Buffers/System.Buffers.dll
%{_prefix}%{libdir}/mono/System.Memory/System.Memory.dll
%{_prefix}%{libdir}/System.Numerics.Vectors.dll
%{_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{_datadir}/pkgconfig/Npgsql.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.2-1
- Update to 4.0.2
* Fri Jun 16 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.2.4-1
- Rename RPM package to Npgsql
- Updated to use NuGet version
* Mon Jan 5 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

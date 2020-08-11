#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-Npgsql
Version:        4.1.4
Release:        1%{?dist}
Summary:        Postgresql database connectivity for C#
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18

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
Requires:
Version: %{version}
Libs: -r:${libdir}/System.Threading.Tasks.Extensions.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll -r:${libdir}/System.Buffers.dll -r:${libdir}/System.Memory.dll -r:${libdir}/System.Numerics.Vectors.dll -r:${libdir}/Npgsql.dll 
Cflags:
EOF

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Npgsql.%{version}/lib/netstandard2.0/Npgsql.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.Threading.Tasks.Extensions.4.5.3/lib/netstandard2.0/System.Threading.Tasks.Extensions.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.Text.Json.4.6.0/lib/netstandard2.0/System.Text.Json.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.Buffers.4.5.0/lib/netstandard2.0/System.Buffers.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/
install -m 644 System.Memory.4.5.3/lib/netstandard2.0/System.Memory.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/
install -m 644 Microsoft.Bcl.AsyncInterfaces.1.1.0/lib/netstandard2.0/Microsoft.Bcl.AsyncInterfaces.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/
install -m 644 System.Text.Encodings.Web.4.6.0/lib/netstandard2.0/System.Text.Encodings.Web.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/
install -m 644 System.Runtime.CompilerServices.Unsafe.4.6.0/lib/netstandard2.0/System.Runtime.CompilerServices.Unsafe.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/
install -m 644 System.Numerics.Vectors.4.5.0/lib/netstandard2.0/System.Numerics.Vectors.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Npgsql.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Npgsql.dll
%{_darwinx_prefix}%{libdir}/System.Threading.Tasks.Extensions.dll
%{_darwinx_prefix}%{libdir}/System.Text.Json.dll
%{_darwinx_prefix}%{libdir}/System.Buffers.dll
%{_darwinx_prefix}%{libdir}/System.Memory.dll
%{_darwinx_prefix}%{libdir}/Microsoft.Bcl.AsyncInterfaces.dll
%{_darwinx_prefix}%{libdir}/System.Text.Encodings.Web.dll
%{_darwinx_prefix}%{libdir}/System.Runtime.CompilerServices.Unsafe.dll
%{_darwinx_prefix}%{libdir}/System.Numerics.Vectors.dll
%{_darwinx_datadir}/pkgconfig/Npgsql.pc

%changelog
* Mon Oct 7 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.1.1-1
- Update to 4.1.1

* Mon Jun 22 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.0-1
- Initial version

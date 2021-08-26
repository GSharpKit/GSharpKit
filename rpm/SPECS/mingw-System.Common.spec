%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.Common
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.Common
Version:        1.0.0
Release:        1%{?dist}
Summary:        System Common libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet
Prefix:		/usr
BuildArch:	noarch

%description
System Common libraries

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
System Common libraries

%prep
%setup -c %{name}-%{version} -T
nuget install Microsoft.Bcl.AsyncInterfaces -Version 5.0.0
nuget install System.Buffers -Version 4.5.1
nuget install System.Data.DataSetExtensions -Version 4.5.0
nuget install System.Memory -Version 4.5.4
nuget install System.Numerics.Vectors -Version 4.5.0
nuget install System.Reflection.TypeExtensions -Version 4.7.0
nuget install System.Reflection.DispatchProxy -Version 4.7.1
nuget install System.Runtime.CompilerServices.Unsafe -Version 5.0.0
nuget install System.Text.Encoding.CodePages -Version 5.0.0
nuget install System.Text.Encodings.Web -Version 5.0.0
nuget install System.Text.Json -Version 5.0.0
nuget install System.Threading.Channels -Version 5.0.0
nuget install System.Threading.Tasks.Extensions -Version 4.5.4

cat > System.Common.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: System.Common
Description: System.Common
Requires:
Version: %{version}
Libs: -r:${libdir}/System.Text.Encoding.CodePages.dll -r:${libdir}/System.Text.Encodings.Web.dll -r:${libdir}/System.Data.DataSetExtensions.dll -r:${libdir}/System.Reflection.TypeExtensions.dll -r:${libdir}/System.Reflection.DispatchProxy.dll -r:${libdir}/System.Buffers.dll -r:${libdir}/Microsoft.Bcl.AsyncInterfaces.dll -r:${libdir}/System.Memory.dll -r:${libdir}/System.Text.Json.dll -r:${libdir}/System.Threading.Channels.dll -r:${libdir}/System.Threading.Tasks.Extensions.dll -r:${libdir}/System.Runtime.CompilerServices.Unsafe.dll -r:${libdir}/System.Numerics.Vectors.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

rm -rf System.Runtime.CompilerServices.Unsafe.4.5.3

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 System.Common.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/System.Common.pc

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0
- Initial version

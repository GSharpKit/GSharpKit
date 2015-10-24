%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-Newtonsoft.Json
Version:        6.0.7
Release:        1%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Source0:        Newtonsoft.Json-%{version}.tar.gz
Prefix:		/usr

BuildArch:	noarch

Requires:	darwinx-mono >= 3.12.0

Obsoletes:      darwinx-newtonsoft-json
Provides:       darwinx-newtonsoft-json

%description
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -q -n Newtonsoft.Json-%{version}

cat > Newtonsoft.Json.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{version}
Libs: -r:${libdir}/Newtonsoft.Json.dll
Cflags:
EOF

%build
cd Src/Newtonsoft.Json
xbuild Newtonsoft.Json.Net40.csproj                     \
/property:SignAssembly=true                             \
/property:AssemblyOriginatorKeyFile=Dynamic.snk         \
/property:Configuration=Release                         \
/property:DefineConstants='SIGNED NET40'

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll.mdb $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Newtonsoft.Json.dll
%{_darwinx_prefix}%{libdir}/Newtonsoft.Json.dll.mdb
%{_darwinx_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Wed Jul 02 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5-1
- Initial version

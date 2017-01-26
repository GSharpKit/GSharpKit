%global debug_package %{nil}

%define libdir /lib
%define api_version 9.0.0.0

Name:           Newtonsoft.Json
Version:        9.0.1
Release:        2%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Source0:        Newtonsoft.Json-%{version}.tar.gz
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 3.0.0
Requires:	mono-data >= 3.0.0

Obsoletes:	newtonsoft-json
Provides:	newtonsoft-json

%description
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -q

cat > Newtonsoft.Json.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Newtonsoft.Json.dll
Cflags:
EOF

%build
cd Src/Newtonsoft.Json
xbuild Newtonsoft.Json.Net40.csproj			\
/property:SignAssembly=true                             \
/property:AssemblyOriginatorKeyFile=Dynamic.snk         \
/property:Configuration=Release				\
/property:DefineConstants='SIGNED NET40'

%install
%{__rm} -rf %{buildroot}


install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}

#gacutil -i Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll -f -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.md
#{_prefix}%{libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll
#{_prefix}%{libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll.mdb
%{_prefix}%{libdir}/Newtonsoft.Json.dll
%{_prefix}%{libdir}/Newtonsoft.Json.dll.mdb
%{_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Sat Dec 23 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.7-1
- Updated to 6.0.7

* Sat Dec 29 2012 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 4.5-1
- Initial version

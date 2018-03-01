%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-Newtonsoft.Json
Version:        10.0.3
Release:        1%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

Requires:	darwinx-mono-core >= 4.8

Obsoletes:      darwinx-newtonsoft-json
Provides:       darwinx-newtonsoft-json

%description
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -q -T -c Newtonsoft.Json-%{version}
nuget install Newtonsoft.Json -Version %{version}

cat > Newtonsoft.Json.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{version}
Libs: -r:${libdir}/Newtonsoft.Json/Newtonsoft.Json.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/mono/gac
gacutil -i Newtonsoft.Json.%{version}/lib/net45/Newtonsoft.Json.dll -package Newtonsoft.Json -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/Newtonsoft.Json/Newtonsoft.Json.dll
%{_darwinx_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Wed Jul 02 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5-1
- Initial version

%global debug_package %{nil}

%define libdir /lib
%define api_version 10.0.0.0

Name:           Newtonsoft.Json
Version:        10.0.3
Release:        2%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 3.0.0
Requires:	mono-data >= 3.0.0

Obsoletes:	newtonsoft-json
Provides:	newtonsoft-json

%description
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > Newtonsoft.Json.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{api_version}
Libs: -r:${libdir}/%{name}/Newtonsoft.Json.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i Newtonsoft.Json.%{version}/lib/net45/Newtonsoft.Json.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/Newtonsoft.Json.dll
%{_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Thu Oct 03 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 10.0.3-1
- Updated to 10.0.3

* Sat Dec 23 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.7-1
- Updated to 6.0.7

* Sat Dec 29 2012 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 4.5-1
- Initial version

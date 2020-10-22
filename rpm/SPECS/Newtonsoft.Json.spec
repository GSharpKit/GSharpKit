%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:           Newtonsoft.Json
Version:        12.0.3
Release:        1%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr
BuildArch:	noarch

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
Version: %{version}
Libs: -r:${libdir}/%{name}/Newtonsoft.Json.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i Newtonsoft.Json.%{version}/lib/netstandard2.0/Newtonsoft.Json.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

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
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 11.0.2-1
- Fixed API version to 11.0.0.0

* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 11.0.2-1
- Updated to 11.0.2

* Thu Oct 03 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 10.0.3-1
- Updated to 10.0.3

* Sat Dec 23 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.7-1
- Updated to 6.0.7

* Sat Dec 29 2012 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 4.5-1
- Initial version

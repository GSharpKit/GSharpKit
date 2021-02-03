%global debug_package %{nil}

%define libdir /lib

Name:           Mono.Data.Sqlite
Version:        1.0.61.1
Release:        1%{?dist}
Summary:        Mono.Data.Sqlite to any Xamarin or Windows .NET app 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Data.Sqlite
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

%description
Add Mono.Data.Sqlite to any Xamarin or Windows .NET app. 
Supports Xamarin.Android, Xamarin.iOS, Windows 8, Windows Desktop and Windows Phone 8

%prep
%setup -c %{name}-%{version} -T
nuget install %{name}.Core -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{name} - %{summary}
Version: %{version}
Libs: -r:${libdir}/Mono.Data.Sqlite.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 %{name}.Core.%{version}/lib/netstandard2.0/Mono.Data.Sqlite.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Mono.Data.Sqlite.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Aug 9 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.61-1
- Initial version

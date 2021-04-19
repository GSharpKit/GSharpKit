%global __strip /bin/true

%global darwinx_pkg_name Mono.Data.Sqlite

%define pkg_name Mono.Data.Sqlite.Core
%define debug_package %{nil}

%define libdir /lib

Name:           darwinx-Mono.Data.Sqlite
Version:        1.0.61.1
Release:        1%{?dist}
Summary:        Mono.Data.Sqlite to any Xamarin or Windows .NET app. 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Data.Sqlite

Prefix:		/usr
BuildArch:	noarch

%description
Add Mono.Data.Sqlite to any Xamarin or Windows .NET app.
Supports Xamarin.Android, Xamarin.iOS, Windows 8, Windows Desktop and Windows Phone 8

%prep
%setup -c %{name}-%{version} -T
nuget install %{pkg_name} -Version %{version}

cat > Mono.Data.Sqlite.pc << \EOF
prefix=%{darwinx_prefix}
exec_prefix=${prefix}
libdir=%{darwinx_prefix}%{libdir}

Name: Mono.Data.Sqlite
Description: %{name} - %{summary}
Version: %{version}
Libs: -r:${libdir}/Mono.Data.Sqlite.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
install -m 644 %{pkg_name}.%{version}/lib/netstandard2.0/Mono.Data.Sqlite.dll $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_datadir}/pkgconfig/
install -m 644 Mono.Data.Sqlite.pc $RPM_BUILD_ROOT%{darwinx_datadir}/pkgconfig/Mono.Data.Sqlite.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n darwinx-%{darwinx_pkg_name}
%defattr(-,root,root,-)
%{darwinx_prefix}%{libdir}/Mono.Data.Sqlite.dll
%{darwinx_datadir}/pkgconfig/Mono.Data.Sqlite.pc

%changelog
* Fri Aug 9 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.3.5-1
- Initial version

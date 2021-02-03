%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Mono.Data.Sqlite
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-Mono.Data.Sqlite
Version:        1.0.61.1
Release:        1%{?dist}
Summary:        Mono.Data.Sqlite to any Xamarin or Windows .NET app. 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Data.Sqlite

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget


%description
Add Mono.Data.Sqlite to any Xamarin or Windows .NET app.
Supports Xamarin.Android, Xamarin.iOS, Windows 8, Windows Desktop and Windows Phone 8

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-BouncyCastle

%description -n mingw32-%{mingw_pkg_name}
Add Mono.Data.Sqlite to any Xamarin or Windows .NET app.
Supports Xamarin.Android, Xamarin.iOS, Windows 8, Windows Desktop and Windows Phone 8

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-BouncyCastle

%description -n mingw64-%{mingw_pkg_name}
Add Mono.Data.Sqlite to any Xamarin or Windows .NET app.
Supports Xamarin.Android, Xamarin.iOS, Windows 8, Windows Desktop and Windows Phone 8

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name}.Core -Version %{version}

cat > Mono.Data.Sqlite32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Mono.Data.Sqlite
Description: %{name} - %{summary}
Version: %{version}
Libs: -r:${libdir}/Mono.Data.Sqlite.dll
Cflags:
EOF

cat > Mono.Data.Sqlite64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

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
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Mono.Data.Sqlite.Core.%{version}/lib/netstandard2.0/Mono.Data.Sqlite.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Mono.Data.Sqlite32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Mono.Data.Sqlite.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Mono.Data.Sqlite.Core.%{version}/lib/netstandard2.0/Mono.Data.Sqlite.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Mono.Data.Sqlite64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Mono.Data.Sqlite.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Mono.Data.Sqlite.dll
%{mingw32_datadir}/pkgconfig/Mono.Data.Sqlite.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Mono.Data.Sqlite.dll
%{mingw64_datadir}/pkgconfig/Mono.Data.Sqlite.pc

%changelog
* Fri Aug 9 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.3.5-1
- Initial version

%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Mono.Posix.NETStandard
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 1.0.0.0

Name:           mingw-Mono.Posix.NETStandard
Version:        1.0.0
Release:        1%{?dist}
Summary:        Provides functionality to access Posix/Unix features 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Posix.NETStandard

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  nuget

%description
Provides functionality to access Posix/Unix features

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:	%{summary}
Provides:	mingw64(api-ms-win-crt-filesystem-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-heap-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-locale-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-runtime-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-stdio-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-time-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-utility-l1-1-0.dll)
Provides:	mingw64(vcruntime140.dll)

%description -n mingw64-%{mingw_pkg_name}
Provides functionality to access Posix/Unix features

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > Mono.Posix.NETStandard64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Mono.Posix.NETStandard
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Mono.Posix.NETStandard.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Mono.Posix.NETStandard.%{version}/runtimes/win-x64/lib/netstandard2.0/Mono.Posix.NETStandard.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 Mono.Posix.NETStandard.%{version}/runtimes/win-x64/native/libMonoPosixHelper.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 Mono.Posix.NETStandard.%{version}/runtimes/win-x64/native/MonoPosixHelper.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Mono.Posix.NETStandard64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Mono.Posix.NETStandard.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Mono.Posix.NETStandard.dll
%{mingw64_prefix}%{libdir}/libMonoPosixHelper.dll
%{mingw64_prefix}%{libdir}/MonoPosixHelper.dll
%{mingw64_datadir}/pkgconfig/Mono.Posix.NETStandard.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Mono.Posix
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 7.1.0.0
%define rel final.1.21458.1

Name:           mingw-Mono.Posix
Version:        7.1.0
Release:        1%{?dist}
Summary:        Provides functionality to access Posix/Unix features 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Posix

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  nuget

%description
Provides functionality to access Posix/Unix features

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:	%{summary}
Obsoletes:      mingw64-Mono.Posix.NETStandard
Provides:       mingw64-Mono.Posix.NETStandard

%description -n mingw64-%{mingw_pkg_name}
Provides functionality to access Posix/Unix features

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}-%{rel}

cat > Mono.Posix.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Mono.Posix
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Mono.Posix.dll -r:${libdir}/Mono.Unix.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Mono.Posix.%{version}-%{rel}/lib/netstandard2.0/Mono.Posix.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/
install -m 644 Mono.Unix.%{version}-%{rel}/lib/netstandard2.0/Mono.Unix.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Mono.Posix.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Mono.Posix.dll
%{mingw64_prefix}%{libdir}/Mono.Unix.dll
%{mingw64_datadir}/pkgconfig/Mono.Posix.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 1.0.0.0
%define rel final.1.21458.1

Name:           Mono.Posix
Version:        7.1.0
Release:        1%{?dist}
Summary:        Provides functionality to access Posix/Unix features

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Posix.NETStandard
Prefix:		/usr
BuildArch:	x86_64

Obsoletes:	Mono.Posix.NETStandard
Provides:	Mono.Posix.NETStandard

%description
Provides functionality to access Posix/Unix features

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}-%{rel}

cat > Mono.Posix.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Mono.Posix.NETStandard
Description: Provides functionality to access Posix/Unix features
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Mono.Posix.dll -r:${libdir}/Mono.Unix.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Mono.Posix.%{version}-%{rel}/lib/netstandard2.0/Mono.Posix.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 Mono.Unix.%{version}-%{rel}/lib/netstandard2.0/Mono.Unix.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 Mono.Unix.%{version}-%{rel}/runtimes/linux-x64/native/libMono.Unix.so $RPM_BUILD_ROOT%{_prefix}%{libdir}/libintl.so

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Mono.Posix.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Mono.Posix.dll
%{_prefix}%{libdir}/Mono.Unix.dll
%{_prefix}%{libdir}/libintl.so
%{_prefix}%{libdir}/libMono.Unix.so
%{_datadir}/pkgconfig/Mono.Posix.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0-1
- Initial version

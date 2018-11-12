%global debug_package %{nil}

%define libdir /lib
%define api_version 1.0.0.0

Name:           Mono.Posix.NETStandard
Version:        1.0.0
Release:        1%{?dist}
Summary:        Provides functionality to access Posix/Unix features

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Posix.NETStandard
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 5.0.0

%description
Provides functionality to access Posix/Unix features

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > Mono.Posix.NETStandard.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: Mono.Posix.NETStandard
Description: Provides functionality to access Posix/Unix features
Requires:
Version: %{api_version}
Libs: -r:${libdir}/Mono.Posix.NETStandard.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Mono.Posix.NETStandard.%{version}/ref/netstandard2.0/Mono.Posix.NETStandard.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 Mono.Posix.NETStandard.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/Mono.Posix.NETStandard.dll
%{_datadir}/pkgconfig/Mono.Posix.NETStandard.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0-1
- Initial version

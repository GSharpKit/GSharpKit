%global darwinx_pkg_name Mono.Posix.NETStandard

%define libdir /lib

Name:           darwinx-Mono.Posix.NETStandard
Version:        1.0.0
Release:        1%{?dist}
Summary:        Provides functionality to access Posix/Unix features 

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Mono.Posix.NETStandard

Source0:	libMonoPosixHelper.dylib
Source1:	darwinx-Mono.Posix.dll

Prefix:		/usr
BuildArch:	noarch

%description
Provides functionality to access Posix/Unix features

%prep
%setup -c %{name}-%{version} -T
nuget install %{darwinx_pkg_name} -Version %{version}

cat > Mono.Posix.NETStandard.pc << \EOF
prefix=%{darwinx_prefix}
exec_prefix=${prefix}
libdir=%{darwinx_prefix}%{libdir}

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

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
#install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}/libMonoPosixHelper.dylib
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}/Mono.Posix.dll
install -m 644 Mono.Posix.NETStandard.%{version}/ref/netstandard2.0/Mono.Posix.NETStandard.dll $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_datadir}/pkgconfig/
install -m 644 Mono.Posix.NETStandard.pc $RPM_BUILD_ROOT%{darwinx_datadir}/pkgconfig/Mono.Posix.NETStandard.pc

%clean
%{__rm} -rf %{buildroot}

%files -n darwinx-%{darwinx_pkg_name}
%defattr(-,root,root,-)
#{darwinx_prefix}%{libdir}/libMonoPosixHelper.dylib
%{darwinx_prefix}%{libdir}/Mono.Posix.dll
%{darwinx_prefix}%{libdir}/Mono.Posix.NETStandard.dll
%{darwinx_datadir}/pkgconfig/Mono.Posix.NETStandard.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

%global debug_package %{nil}

%define darwinx_pkg_name Sprache
%define libdir /lib

Name:           darwinx-Sprache
Version:        2.2.0
Release:        1%{?dist}
Summary:        Sprache is a simple, lightweight library for constructing parsers directly in C# code

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

%description
Sprache is a simple, lightweight library for constructing parsers directly in C# code

%prep
%setup -q -T -c %{darwinx_pkg_name}-%{version}
nuget install %{darwinx_pkg_name}.Signed -Version %{version}

cat > %{darwinx_pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{darwinx_pkg_name}
Description: Sprache is a simple, lightweight library for constructing parsers directly in C# code 
Requires:
Version: %{version}
Libs: -r:${libdir}/Sprache.Signed.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Sprache.Signed.%{version}/lib/netstandard2.0/Sprache.Signed.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 %{darwinx_pkg_name}.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/%{darwinx_pkg_name}.Signed.dll
%{_darwinx_datadir}/pkgconfig/%{darwinx_pkg_name}.pc


%changelog
* Wed Jun 19 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.2.0-1
- Initial version

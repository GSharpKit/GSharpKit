%global debug_package %{nil}

%define libdir /lib
%define api_version 2.2.0.0

Name:           Sprache
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
%setup -c %{name}-%{version} -T
nuget install %{name}.Signed -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: Sprache is a simple, lightweight library for constructing parsers directly in C# code
Requires:
Version: %{api_version}
Libs: -r:${libdir}/%{name}.Signed.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 %{name}.Signed.%{version}/lib/netstandard2.0/%{name}.Signed.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/%{name}.Signed.dll
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Mon Oct 01 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.1.2-1
- Initial version

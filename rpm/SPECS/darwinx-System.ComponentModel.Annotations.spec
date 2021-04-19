%global debug_package %{nil}

%define pkg_name System.ComponentModel.Annotations
%define libdir /lib

Name:           darwinx-System.ComponentModel.Annotations
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides attributes that are used to define metadata for objects used as data sources.

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

%description
Provides attributes that are used to define metadata for objects used as data sources.

%prep
%setup -q -T -c %{name}-%{version}
nuget install %{pkg_name} -Version %{version}

cat > %{pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{pkg_name}
Description: Provides attributes that are used to define metadata for objects used as data sources.
Requires:
Version: %{version}
Libs: -r:${libdir}/%{pkg_name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{pkg_name}.%{version}/lib/netstandard2.0/%{pkg_name}.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 %{pkg_name}.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll
%{_darwinx_datadir}/pkgconfig/*.pc


%changelog
* Fri Apr 16 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial version

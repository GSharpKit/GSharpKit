%define libdir /lib

%global nuget_pkg_name SharpCamera

Name:           SharpCamera
Version:        0.3.7
Release:        1%{?dist}
Summary:        A libgphoto2 backed interface to tether cameras.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/SharpCamera

Prefix:		/usr
BuildArch:	noarch

Requires:	libgphoto2-sharp

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
A libgphoto2 backed interface to tether cameras.

%prep
%setup -c %{name}-%{version} -T
nuget install %{nuget_pkg_name} -Version %{version}

cat > %{nuget_pkg_name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{nuget_pkg_name}
Description: %{name} - %{summary}
Requires: libgphoto2-sharp
Version: %{version}
Libs: -r:${libdir}/SharpCamera.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono
install -m 644 %{nuget_pkg_name}.%{version}/lib/netstandard2.0/SharpCamera.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{nuget_pkg_name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/SharpCamera.dll
%{_datadir}/pkgconfig/%{nuget_pkg_name}.pc

%changelog
* Mon Nov 19 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.3.7-1
- Initial version

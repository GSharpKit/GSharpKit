%define libdir /lib

%global nuget_pkg_name libgphoto2

Name:           libgphoto2-sharp
Version:        0.3.2
Release:        1%{?dist}
Summary:        C# friendly bindings to libgphoto2.

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/

Prefix:		/usr
BuildArch:	noarch

Requires:	libgphoto2

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
C# friendly bindings to libgphoto2.

%prep
%setup -c %{name}-%{version} -T
nuget install %{nuget_pkg_name} -Version %{version}

cat > libgphoto2-sharp.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: libgphoto2-sharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/libgphoto2-sharp.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 libgphoto2.%{version}/lib/netstandard2.0/libgphoto2.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/libgphoto2-sharp.dll

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 libgphoto2-sharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/libgphoto2-sharp.dll
%{_datadir}/pkgconfig/libgphoto2-sharp.pc

%changelog
* Mon Nov 19 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.2.3-1
- Initial version

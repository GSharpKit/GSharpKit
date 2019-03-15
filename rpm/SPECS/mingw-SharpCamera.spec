%?mingw_package_header

%global __strip /bin/true

%global nuget_pkg_name SharpCamera

%global mingw_pkg_name SharpCamera
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-SharpCamera
Version:        0.3.7
Release:        1%{?dist}
Summary:        C# friendly bindings to SharpCamera.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/SharpCamera

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
C# friendly bindings to SharpCamera.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-libgphoto2-sharp

%description -n mingw32-%{mingw_pkg_name}
C# friendly bindings to SharpCamera.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-libgphoto2-sharp

%description -n mingw64-%{mingw_pkg_name}
C# friendly bindings to SharpCamera.

%prep
%setup -c %{name}-%{version} -T
nuget install %{nuget_pkg_name} -Version %{version}

cat > SharpCamera32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: SharpCamera
Description: %{name} - %{summary}
Requires: libgphoto2-sharp
Version: %{version}
Libs: -r:${libdir}/SharpCamera.dll
Cflags:
EOF

cat > SharpCamera64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: SharpCamera
Description: %{name} - %{summary}
Requires: libgphoto2-sharp
Version: %{version}
Libs: -r:${libdir}/SharpCamera.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 SharpCamera.%{version}/lib/netstandard2.0/SharpCamera.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 SharpCamera32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/SharpCamera.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 SharpCamera.%{version}/lib/netstandard2.0/SharpCamera.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 SharpCamera64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/SharpCamera.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/SharpCamera.dll
%{mingw32_datadir}/pkgconfig/SharpCamera.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/SharpCamera.dll
%{mingw64_datadir}/pkgconfig/SharpCamera.pc


%changelog
* Mon Nov 19 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.2.3-1
- Initial version

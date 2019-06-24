%?mingw_package_header

%global __strip /bin/true

%global nuget_pkg_name libgphoto2

%global mingw_pkg_name libgphoto2-sharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:           mingw-libgphoto2-sharp
Version:        0.3.2
Release:        1%{?dist}
Summary:        C# friendly bindings to libgphoto2.

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
C# friendly bindings to libgphoto2.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono
Requires:       mingw32-libgphoto2

%description -n mingw32-%{mingw_pkg_name}
C# friendly bindings to libgphoto2.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono
Requires:       mingw64-libgphoto2

%description -n mingw64-%{mingw_pkg_name}
C# friendly bindings to libgphoto2.

%prep
%setup -c %{name}-%{version} -T
nuget install %{nuget_pkg_name} -Version %{version}

cat > libgphoto2-sharp32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: libgphoto2-sharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/libgphoto2-sharp.dll
Cflags:
EOF

cat > libgphoto2-sharp64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

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

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 libgphoto2.%{version}/lib/netstandard2.0/libgphoto2.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/libgphoto2-sharp.dll

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 libgphoto2-sharp32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/libgphoto2-sharp.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 libgphoto2.%{version}/lib/netstandard2.0/libgphoto2.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/libgphoto2-sharp.dll

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 libgphoto2-sharp64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/libgphoto2-sharp.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/libgphoto2-sharp.dll
%{mingw32_datadir}/pkgconfig/libgphoto2-sharp.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/libgphoto2-sharp.dll
%{mingw64_datadir}/pkgconfig/libgphoto2-sharp.pc


%changelog
* Mon Nov 19 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.2.3-1
- Initial version

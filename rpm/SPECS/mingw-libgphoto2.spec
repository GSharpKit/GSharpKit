%?mingw_package_header

%global mingw_pkg_name libgphoto2

Name:           mingw-libgphoto2
Version:        2.5.20
Release:        1%{?dist}
Summary:        libgphoto2 is a library that can be used by applications to access various digital cameras.

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/gphoto/libgphoto2
Source0:        https://github.com/gphoto/libgphoto2/libgphoto2-%{version}.tar.bz2
Patch00:	libgphoto2-gp_system_filename-fix.patch
Patch01:	libgphoto2-shlobj.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-libusbx-static
BuildRequires:  mingw64-libusbx-static
BuildRequires:  mingw32-libexif-static
BuildRequires:  mingw64-libexif-static
BuildRequires:  mingw32-libltdl
BuildRequires:  mingw64-libltdl

%description
libgphoto2 is a library that can be used by applications to access various digital cameras.

%package -n mingw32-libgphoto2
Summary:        libgphoto2 is a library that can be used by applications to access various digital cameras.
Requires:	mingw32-libusbx
Requires:	mingw32-libexif

%description -n mingw32-libgphoto2
libgphoto2 is a library that can be used by applications to access various digital cameras.

%package -n mingw32-libgphoto2-static
Summary:        libgphoto2 is a library that can be used by applications to access various digital cameras.
Requires:       mingw32-libgphoto2 = %{version}-%{release}

%description -n mingw32-libgphoto2-static
libgphoto2 is a library that can be used by applications to access various digital cameras.

%package -n mingw64-libgphoto2
Summary:        libgphoto2 is a library that can be used by applications to access various digital cameras.
Requires:       mingw64-libusbx
Requires:	mingw64-libexif

%description -n mingw64-libgphoto2
libgphoto2 is a library that can be used by applications to access various digital cameras.

%package -n mingw64-libgphoto2-static
Summary:        libgphoto2 is a library that can be used by applications to access various digital cameras.
Requires:       mingw64-libgphoto2 = %{version}-%{release}

%description -n mingw64-libgphoto2-static
libgphoto2 is a library that can be used by applications to access various digital cameras.


%?mingw_debug_package

%prep
%setup -q -n %{mingw_pkg_name}-%{version}
%patch00 -p1
%patch01 -p1

%build
%mingw_configure --disable-static

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libgphoto2/%{version}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libgphoto2/%{version}/*.la

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libgphoto2_port/0.12.0/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libgphoto2_port/0.12.0/*.la

rm -f $RPM_BUILD_ROOT%{mingw32_includedir}/gphoto2/gphoto2
rm -f $RPM_BUILD_ROOT%{mingw64_includedir}/gphoto2/gphoto2

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}

rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/udev
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/udev

%files -n mingw32-libgphoto2
%{mingw32_bindir}/gphoto2-config
%{mingw32_bindir}/gphoto2-port-config
%{mingw32_bindir}/libgphoto2-6.dll
%{mingw32_bindir}/libgphoto2_port-12.dll

%dir %{mingw32_includedir}/gphoto2
%{mingw32_includedir}/gphoto2/*.h

%dir %{mingw32_libdir}/libgphoto2
%{mingw32_libdir}/libgphoto2/print-camera-list.exe

%dir %{mingw32_libdir}/libgphoto2/%{version}
%{mingw32_libdir}/libgphoto2/%{version}/*.dll

%dir %{mingw32_libdir}/libgphoto2_port
%dir %{mingw32_libdir}/libgphoto2_port/0.12.0
%{mingw32_libdir}/libgphoto2_port/0.12.0/*.dll

%{mingw32_libdir}/pkgconfig/libgphoto2.pc
%{mingw32_libdir}/pkgconfig/libgphoto2_port.pc

%files -n mingw32-libgphoto2-static
%{mingw32_libdir}/*.a
%{mingw32_libdir}/libgphoto2/%{version}/*.a
%{mingw32_libdir}/libgphoto2_port/0.12.0/*.a

%files -n mingw64-libgphoto2
%{mingw64_bindir}/gphoto2-config
%{mingw64_bindir}/gphoto2-port-config
%{mingw64_bindir}/libgphoto2-6.dll
%{mingw64_bindir}/libgphoto2_port-12.dll

%dir %{mingw64_includedir}/gphoto2
%{mingw64_includedir}/gphoto2/*.h

%dir %{mingw64_libdir}/libgphoto2
%{mingw64_libdir}/libgphoto2/print-camera-list.exe

%dir %{mingw64_libdir}/libgphoto2/%{version}
%{mingw64_libdir}/libgphoto2/%{version}/*.dll

%dir %{mingw64_libdir}/libgphoto2_port
%dir %{mingw64_libdir}/libgphoto2_port/0.12.0
%{mingw64_libdir}/libgphoto2_port/0.12.0/*.dll

%{mingw64_libdir}/pkgconfig/libgphoto2.pc
%{mingw64_libdir}/pkgconfig/libgphoto2_port.pc

%files -n mingw64-libgphoto2-static
%{mingw64_libdir}/*.a
%{mingw64_libdir}/libgphoto2/%{version}/*.a
%{mingw64_libdir}/libgphoto2_port/0.12.0/*.a


%changelog
* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to mingw-libgphoto2
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

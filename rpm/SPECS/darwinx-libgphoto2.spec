%global darwinx_pkg_name libgphoto2

Name:           darwinx-libgphoto2
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

BuildRequires:  darwinx-filesystem >= 107

BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-gtk3

%description
libgphoto2 is a library that can be used by applications to access various digital cameras.

%prep
%setup -q -n %{darwinx_pkg_name}-%{version}
%patch00 -p1
%patch01 -p1

%build
%darwinx_configure --disable-static

%darwinx_make %{?_smp_mflags} V=1

%install
%darwinx_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{darwinx_libdir}/*.la

rm -f $RPM_BUILD_ROOT%{darwinx_libdir}/libgphoto2/%{version}/*.la

rm -f $RPM_BUILD_ROOT%{darwinx_libdir}/libgphoto2_port/0.12.0/*.la

rm -rf $RPM_BUILD_ROOT%{darwinx_includedir}/gphoto2

rm -rf $RPM_BUILD_ROOT%{darwinx_datadir}

rm -rf $RPM_BUILD_ROOT%{darwinx_libdir}/udev

%files -n darwinx-libgphoto2
%{darwinx_bindir}/gphoto2-config
%{darwinx_bindir}/gphoto2-port-config

%{darwinx_libdir}/libgphoto2.dylib
%{darwinx_libdir}/libgphoto2.6.dylib
%{darwinx_libdir}/libgphoto2_port.dylib
%{darwinx_libdir}/libgphoto2_port.12.dylib

#dir %{darwinx_includedir}/gphoto2
#{darwinx_includedir}/gphoto2/*.h

%dir %{darwinx_libdir}/libgphoto2
%{darwinx_libdir}/libgphoto2/print-camera-list

%dir %{darwinx_libdir}/libgphoto2/%{version}
%{darwinx_libdir}/libgphoto2/%{version}/*.so

%dir %{darwinx_libdir}/libgphoto2_port
%dir %{darwinx_libdir}/libgphoto2_port/0.12.0
%{darwinx_libdir}/libgphoto2_port/0.12.0/*.so

%{darwinx_libdir}/pkgconfig/libgphoto2.pc
%{darwinx_libdir}/pkgconfig/libgphoto2_port.pc

%changelog
* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to darwinx-libgphoto2
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

%?mingw_package_header

Name:           mingw-dbus
Version:        1.13.16
Release:        1%{?dist}
Summary:        MinGW Windows port of D-Bus

License:        GPLv2+ or AFL
Group:          Development/Libraries
URL:            http://www.freedesktop.org/wiki/Software/dbus
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-expat

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-expat


%description
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

# Win32
%package -n mingw32-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig

%description -n mingw32-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw32-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw32-dbus = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

# Win64
%package -n mingw64-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig

%description -n mingw64-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw64-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw64-dbus = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library


%?mingw_debug_package


%prep
%setup -q -n dbus-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove manpages because they duplicate what's in the
# Fedora native package already.
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}/dbus
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}/dbus

# Remove cmake files
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/cmake
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/cmake

# Win32
%files -n mingw32-dbus
%doc COPYING
%{mingw32_bindir}/dbus-daemon.exe
%{mingw32_bindir}/dbus-launch.exe
%{mingw32_bindir}/dbus-monitor.exe
%{mingw32_bindir}/dbus-send.exe
%{mingw32_bindir}/dbus-test-tool.exe
%{mingw32_bindir}/dbus-run-session.exe
%{mingw32_bindir}/dbus-update-activation-environment.exe
%{mingw32_bindir}/libdbus-1-3.dll
%{mingw32_libdir}/libdbus-1.dll.a
%{mingw32_libdir}/pkgconfig/dbus-1.pc
%{mingw32_sysconfdir}/dbus-1/
%{mingw32_datadir}/dbus-1/
%{mingw32_datadir}/xml/dbus-1/
%{mingw32_includedir}/dbus-1.0/
%{mingw32_libdir}/dbus-1.0/

%files -n mingw32-dbus-static
%{mingw32_libdir}/libdbus-1.a

# Win64
%files -n mingw64-dbus
%doc COPYING
%{mingw64_bindir}/dbus-daemon.exe
%{mingw64_bindir}/dbus-launch.exe
%{mingw64_bindir}/dbus-monitor.exe
%{mingw64_bindir}/dbus-send.exe
%{mingw64_bindir}/dbus-test-tool.exe
%{mingw64_bindir}/dbus-run-session.exe
%{mingw64_bindir}/dbus-update-activation-environment.exe
%{mingw64_bindir}/libdbus-1-3.dll
%{mingw64_libdir}/libdbus-1.dll.a
%{mingw64_libdir}/pkgconfig/dbus-1.pc
%{mingw64_sysconfdir}/dbus-1/
%{mingw64_datadir}/dbus-1/
%{mingw64_datadir}/xml/dbus-1/
%{mingw64_includedir}/dbus-1.0/
%{mingw64_libdir}/dbus-1.0/

%files -n mingw64-dbus-static
%{mingw64_libdir}/libdbus-1.a


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.16-1
- Update to 1.8.16

* Tue Dec 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.12-1
- Update to 1.8.12

* Tue Dec 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.28-1
- Update to 1.6.28
- Fixes CVE-2014-7824 (RHBZ #1173557)
- Fixes CVE-2014-3638 CVE-2014-3639 CVE-2014-3636
  CVE-2014-3637 and CVE-2014-3635 (RHBZ #1142582)
- Fixes CVE-2014-3477 (RHBZ #1117395)
- Fixes CVE-2014-3533 CVE-2014-3532 (RHBZ #1115637)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Ivan Romanov <drizt@land.ru> - 1.6.12-1
- A new upstream version

* Thu Aug 29 2013 Ivan Romanov <drizt@land.ru> - 1.6.8-4
- Added patch to rename interface argument name (RHBZ #980278)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.8-1
- Update to 1.6.8

* Sun Sep 23 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.4-1
- Update to 1.6.4
- Fixes compatibility issue with c++11 support

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.16-1
- Update to 1.4.16
- Added win64 support
- Link against libxml2 instead of expat
- Dropped upstreamed patches

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.4.6-5
- Remove .la files

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.6-4
- Renamed the source package to mingw-dbus (RHBZ #800858)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.6-3
- Rebuild against the mingw-w64 toolchain
- Added patch to prevent redeclaration of the symbol ELEMENT_TYPE

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 28 2011 Ivan Romanov <drizt@land.ru> - 1.4.6-1
- New upstream version
- Removed clean stage
- Added dbus-1.4.6-path-is-absolute.patch patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-0.2.20101008git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 8 2010 Ivan Romanov <drizt@land.ru> - 1.4.1-0.1.20101008git
- Updated to 1.4.1 version from git
- windbus is now part of freedesktop dbus
- Removed mingw32-dbus-c++ package (c++ bindings it's not part of dbus)
- Removed mingw32-dbus-1.2.4-20081031-mingw32.patch
- Removed unusual dependencies
- Removed init.d script
- Changed define tags on the top to global tags
- Added static subpackage with static library
- Added debuginfo

* Fri Feb 6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.3.20081031svn
- Include license.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.2.20081031svn
- Requires pkgconfig.

* Mon Nov 3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-0.1.20081031svn
- Initial RPM release.

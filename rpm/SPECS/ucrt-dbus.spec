%{?ucrt_package_header}

Name:           ucrt-dbus
Version:        1.16.2
Release:        2%{?dist}
Summary:        MinGW Windows port of D-Bus

# The effective license of the majority of the package, including the shared
# library, is "GPL-2+ or AFL-2.1". Certain utilities are "GPL-2+" only.
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/dbus
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

# Restore support for static libs
Patch0:         dbus-static-libs.patch

BuildArch:      noarch

BuildRequires:  cmake

BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-glib2
BuildRequires:  ucrt64-expat


%description
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.


# Win64
%package -n ucrt64-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig

%description -n ucrt64-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.


%package -n ucrt64-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       ucrt64-dbus = %{version}-%{release}

%description -n ucrt64-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library


%{?ucrt_debug_package}


%prep
%autosetup -p1 -n dbus-%{version}


%build
%ucrt64_cmake -DDBUS_ENABLE_DOXYGEN_DOCS=OFF -DENABLE_QT_HELP=OFF
%ucrt64_make


%install
%ucrt64_make install DESTDIR=%{buildroot}

# Remove manpages because they duplicate what's in the
# Fedora native package already.
rm -rf %{buildroot}%{ucrt64_datadir}/doc
rm -rf %{buildroot}%{ucrt64_datadir}/xml


# Win64
%files -n ucrt64-dbus
%license COPYING
%{ucrt64_bindir}/dbus-daemon.exe
%{ucrt64_bindir}/dbus-env.bat
%{ucrt64_bindir}/dbus-launch.exe
%{ucrt64_bindir}/dbus-monitor.exe
%{ucrt64_bindir}/dbus-run-session.exe
%{ucrt64_bindir}/dbus-send.exe
%{ucrt64_bindir}/dbus-test-tool.exe
%{ucrt64_bindir}/dbus-update-activation-environment.exe
%{ucrt64_bindir}/libdbus-1-3.dll
%{ucrt64_libdir}/dbus-1.0/
%{ucrt64_libdir}/libdbus-1.dll.a
%{ucrt64_libdir}/cmake/DBus1/
%{ucrt64_libdir}/pkgconfig/dbus-1.pc
%{ucrt64_sysconfdir}/dbus-1/
%{ucrt64_includedir}/dbus-1.0/
%{ucrt64_datadir}/dbus-1/

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sat Dec 27 2025 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Sandro Mani <manisandro@gmail.com> - 1.16.0-1
- Update to 1.16.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14.10-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Sandro Mani <manisandro@gmail.com> - 1.14.10-1
- Update to 1.14.10

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Sandro Mani <manisandro@gmail.com> - 1.14.8-1
- Update to 1.14.8

* Sat Feb 11 2023 Sandro Mani <manisandro@gmail.com> - 1.14.6-1
- Update to 1.14.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 1.14.4-1
- Update to 1.14.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.8.16-16
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.8.16-10
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

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
- Renamed the source package to ucrt-dbus (RHBZ #800858)
- Use ucrt macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.6-3
- Rebuild against the ucrt-w64 toolchain
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
- Removed ucrt32-dbus-c++ package (c++ bindings it's not part of dbus)
- Removed ucrt32-dbus-1.2.4-20081031-ucrt32.patch
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

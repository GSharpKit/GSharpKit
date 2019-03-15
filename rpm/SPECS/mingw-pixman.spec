%?mingw_package_header

Name:           mingw-pixman
Version:        0.38.0
Release:        1%{?dist}
Summary:        MinGW Windows Pixman library

License:        MIT
URL:            http://cgit.freedesktop.org/pixman/
Group:          Development/Libraries

Source0:        http://cairographics.org/releases/pixman-%{version}.tar.gz
Source1:        make-pixman-snapshot.sh

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils


%description
MinGW Windows Pixman library.


# Win32
%package -n mingw32-pixman
Summary:        MinGW Windows Pixman library

%description -n mingw32-pixman
MinGW Windows Pixman library.


%package -n mingw32-pixman-static
Summary:        Static version of the MinGW Windows Pixman library
Requires:       mingw32-pixman = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-pixman-static
Static version of the MinGW Windows Pixman library.

# Win64
%package -n mingw64-pixman
Summary:        MinGW Windows Pixman library

%description -n mingw64-pixman
MinGW Windows Pixman library.

%package -n mingw64-pixman-static
Summary:        Static version of the cross compiled Pixman library
Requires:       mingw64-pixman = %{version}-%{release}

%description -n mingw64-pixman-static
Static version of the cross compiled Pixman library.


%?mingw_debug_package


%prep
%setup -q -n pixman-%{version}


%build
# Uses GTK for its testsuite, so disable this otherwise
# we have a chicken & egg problem on mingw
%mingw_configure --disable-gtk --disable-sse2 --enable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-pixman
%license COPYING
%{mingw32_bindir}/libpixman-1-0.dll
%{mingw32_includedir}/pixman-1
%{mingw32_libdir}/libpixman-1.dll.a
%{mingw32_libdir}/pkgconfig/pixman-1.pc

%files -n mingw32-pixman-static
%{mingw32_libdir}/libpixman-1.a

# Win64
%files -n mingw64-pixman
%license COPYING
%{mingw64_bindir}/libpixman-1-0.dll
%{mingw64_includedir}/pixman-1
%{mingw64_libdir}/libpixman-1.dll.a
%{mingw64_libdir}/pkgconfig/pixman-1.pc

%files -n mingw64-pixman-static
%{mingw64_libdir}/libpixman-1.a


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 0.34.0-1
- Update to 0.34.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 0.33.2-1
- Update to 0.33.2
- Use license macro for COPYING files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Kalev Lember <kalevlember@gmail.com> - 0.32.6-1
- Update to 0.32.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 0.32.0-1
- Update to 0.32.0

* Wed Sep 04 2013 Kalev Lember <kalevlember@gmail.com> - 0.30.0-4
- Disable SSE2 (fdo#68300)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.30.0-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Tue May 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.26.2-1
- Update to 0.26.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.24.4-3
- Added win64 support
- Dropped unneeded BR: mingw32-dlfcn

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 0.24.4-2
- Renamed the source package to mingw-pixman (#800445)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 0.24.4-1
- Update to 0.24.4
- Remove .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.24.2-2
- Rebuild against the mingw-w64 toolchain

* Wed Feb 01 2012 Kalev Lember <kalevlember@gmail.com> - 0.24.2-1
- Update to 0.24.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 16 2011 Kalev Lember <kalevlember@gmail.com> - 0.22.2-1
- Update to 0.22.2
- Use automatic mingw dep extraction
- Cleaned up the spec file for modern rpmbuild

* Sun May 08 2011 Kalev Lember <kalev@smartlink.ee> - 0.22.0-1
- Update to 0.22.0

* Mon Apr 25 2011 Kalev Lember <kalev@smartlink.ee> - 0.20.2-1
- Update to 0.20.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.19.4-1
- Update to 0.19.4
- Fixed Source URL
- Fixed a small rpmlint warning

* Tue Sep  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.19.2-1
- Update to 0.19.2

* Mon Jul 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2 (RHBZ #613665)

* Tue Sep 29 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.16.2-1
- Update to 0.16.2

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.16.0-2
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sat Aug 29 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.15.20-1
- Update to version 0.15.20
- Updated SOURCE0 and URL
- Automatically generate debuginfo subpackage
- Don't build the 'blitters-test' testcase as it requires the memalign function
  which we don't have on MinGW

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.15.10-1
- Update to 0.15.10
- Use %%global instead of %%define
- Dropped pixman-0.13.2-license.patch as freedesktop bug #19582 is resolved

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.13.2-5
- Fixed %%defattr line
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-3
- Rebuild for mingw32-gcc 4.4

* Thu Jan 15 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-2
- Include LICENSE file (freedesktop bug 19582).

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-1
- Resynch with Fedora package (0.13.2).
- Disable static library for speed.
- Use _smp_mflags.
- Requires pkgconfig.
- Depends on dlfcn.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.12.0-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 0.12.0-1
- Update to 0.12.0 release

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 0.11.10-2
- Remove static library.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 0.11.10-1
- Initial RPM release

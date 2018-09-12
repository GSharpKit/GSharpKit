%{?mingw_package_header}

Name:           mingw-pango
Version:        1.42.3
Release:        1%{?dist}
Summary:        MinGW Windows Pango library

License:        LGPLv2+
URL:            http://www.pango.org
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        http://download.gnome.org/sources/pango/%{release_version}/pango-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-fribidi

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-fribidi

BuildRequires:  pkgconfig

# Needed for the delay-load patch
BuildRequires:  mingw-w64-tools
BuildRequires:  autoconf automake libtool gtk-doc


%description
MinGW Windows Pango library.


# Win32
%package -n mingw32-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig

%description -n mingw32-pango
MinGW Windows Pango library.

%package -n mingw32-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw32-pango = %{version}-%{release}

%description -n mingw32-pango-static
Static version of the MinGW Windows Pango library.

# Win64
%package -n mingw64-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig

%description -n mingw64-pango
MinGW Windows Pango library.

%package -n mingw64-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw64-pango = %{version}-%{release}

%description -n mingw64-pango-static
Static version of the MinGW Windows Pango library.


%?mingw_debug_package


%prep
%setup -q -n pango-%{version}

%build
%mingw_configure \
  --enable-static \
  --enable-shared \
  --enable-delay-load

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pango/
mkdir -p $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pango/

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/charset.alias

rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}/man1

# Drop the gtk-doc documentation
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

# Drop the .def files as they aren't needed by other binaries
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.def
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.def

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-pango
%license COPYING
%{mingw32_bindir}/libpango-1.0-0.dll
%{mingw32_bindir}/libpangocairo-1.0-0.dll
%{mingw32_bindir}/libpangoft2-1.0-0.dll
%{mingw32_bindir}/libpangowin32-1.0-0.dll
%{mingw32_bindir}/pango-view.exe
%{mingw32_bindir}/pango-list.exe
%{mingw32_includedir}/pango-1.0/
%{mingw32_libdir}/libpango-1.0.dll.a
%{mingw32_libdir}/libpangocairo-1.0.dll.a
%{mingw32_libdir}/libpangoft2-1.0.dll.a
%{mingw32_libdir}/libpangowin32-1.0.dll.a
%{mingw32_libdir}/pkgconfig/pango.pc
%{mingw32_libdir}/pkgconfig/pangocairo.pc
%{mingw32_libdir}/pkgconfig/pangoft2.pc
%{mingw32_libdir}/pkgconfig/pangowin32.pc
%{mingw32_sysconfdir}/pango/

%files -n mingw32-pango-static
%{mingw32_libdir}/libpango-1.0.a
%{mingw32_libdir}/libpangocairo-1.0.a
%{mingw32_libdir}/libpangoft2-1.0.a
%{mingw32_libdir}/libpangowin32-1.0.a

# Win64
%files -n mingw64-pango
%license COPYING
%{mingw64_bindir}/libpango-1.0-0.dll
%{mingw64_bindir}/libpangocairo-1.0-0.dll
%{mingw64_bindir}/libpangoft2-1.0-0.dll
%{mingw64_bindir}/libpangowin32-1.0-0.dll
%{mingw64_bindir}/pango-view.exe
%{mingw64_bindir}/pango-list.exe
%{mingw64_includedir}/pango-1.0/
%{mingw64_libdir}/libpango-1.0.dll.a
%{mingw64_libdir}/libpangocairo-1.0.dll.a
%{mingw64_libdir}/libpangoft2-1.0.dll.a
%{mingw64_libdir}/libpangowin32-1.0.dll.a
%{mingw64_libdir}/pkgconfig/pango.pc
%{mingw64_libdir}/pkgconfig/pangocairo.pc
%{mingw64_libdir}/pkgconfig/pangoft2.pc
%{mingw64_libdir}/pkgconfig/pangowin32.pc
%{mingw64_sysconfdir}/pango/

%files -n mingw64-pango-static
%{mingw64_libdir}/libpango-1.0.a
%{mingw64_libdir}/libpangocairo-1.0.a
%{mingw64_libdir}/libpangoft2-1.0.a
%{mingw64_libdir}/libpangowin32-1.0.a
 

%changelog
* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.40.12-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.40.12-1
- Update to 1.40.12

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 1.40.7-1
- Update to 1.40.7

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 1.40.6-1
- Update to 1.40.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 1.40.3-1
- Update to 1.40.3
- Rebase the delay load patch

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 1.40.1-1
- Update to 1.40.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 1.38.1-2
- Use global instead of define.

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 1.38.1-1
- Update to 1.38.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 1.38.0-1
- Update to 1.38.0

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 1.37.3-1
- Update to 1.37.3
- Remove modules support from packaging as it's gone upstream
- Use license macro for COPYING files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.8-1
- Update to 1.36.8

* Fri Sep 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.7-1
- Update to 1.36.7

* Wed Jul 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.5-2
- Fix build failure on environments with older gtk-doc

* Tue Jul 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.5-1
- Update to 1.36.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 1.36.3-1
- Update to 1.36.3

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.2-1
- Update to 1.36.2

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.1-1
- Update to 1.36.1

* Tue Sep 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.36.0-1
- Update to 1.36.0

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.35.3-1
- Update to 1.35.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.35.0-1
- Update to 1.35.0

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.34.1-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 1.34.1-1
- Update to 1.34.1

* Tue Mar 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.34.0-1
- Update to 1.34.0

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.33.9-1
- Update to 1.33.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.6-1
- Update to 1.32.6

* Sun Jan  6 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.5-1
- Update to 1.32.5

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.3-1
- Update to 1.32.3

* Fri Oct  5 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.1-1
- Update to 1.32.1

* Fri Sep 21 2012 Kalev Lember <kalevlember@gmail.com> - 1.31.0-2
- Build the basic-win32 engine in statically
- Update the pango.modules file for 1.8.0 module ABI

* Sat Aug 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.31.0-1
- Update to 1.31.0
- Added BR: mingw32-harfbuzz/mingw64-harfbuzz

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 26 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.30.0-3
- Use the proper configure flag to enable delay-load support

* Sun May 20 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.30.0-2
- Make fontconfig and freetype runtime dependencies instead of hard dependencies

* Wed Mar 28 2012 Kalev Lember <kalevlember@gmail.com> - 1.30.0-1
- Update to 1.30.0
- Regenerate pango.modules

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.29.5-4
- Added win64 support

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 1.29.5-3
- Renamed the source package to mingw-pango (#800444)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.29.5-2
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.29.5-1
- Update to 1.29.5
- Dropped all .la files
- Dropped the .dll.a files for all pango modules
- Dropped upstream patch
- Rebuild against libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 1.29.4-1
- Update to 1.29.4
- Dropped upstreamed fallback engine patch

* Tue Aug 30 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.29.3-1
- Update to 1.29.3
- Dropped the dependency on the autotools by rewriting the patch
- Added two patches from Kalev Lember to fix a crash on Win32. GNOME Bug #653985

* Sun Jul 10 2011 Kalev Lember <kalevlember@gmail.com> - 1.28.4-4
- Stop using G_CONST_RETURN
- Use automatic mingw dep extraction
- Cleaned up the spec file for modern rpmbuild
- Removed the .def files

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.28.4-3
- Rebuilt against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 1.28.4-2
- Removed devhelp documentation which duplicates what is in base Fedora

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.28.4-1
- Update to 1.28.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.28.3-1
- Update to 1.28.3
- Rebuild in order to have soft dependency on libintl

* Sun Jul  4 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.28.1-1
- Update to 1.28.1

* Fri Jun 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.28.0-1
- Update to 1.28.0

* Wed Feb 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.27.1-1
- Update to 1.27.1

* Mon Sep 21 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0
- Use relative paths instead of absolute paths in the pango.modules file

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.6-2
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Tue Sep  8 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.6-1
- Update to 1.25.6

* Mon Aug 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.5-1
- Update to 1.25.5

* Tue Aug 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.4-1
- Update to 1.25.4
- Drop upstreamed patches

* Fri Aug 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.3-1
- Update to 1.25.3
- Drop upstreamed patch
- Added some (already upstreamed) patches to get pango compiled on mingw32

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.2-1
- Update to 1.25.2
- Added BR: mingw32-gcc-c++
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2
- Use %%global instead of %%define

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.23.0-1
- Remove man page which duplicates what is in base Fedora.
- Rebase to 1.23.0 to match Fedora.
- +BR mingw32-dlfcn.

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 1.22.1-6
- Added -static subpackage

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-5
- Rebuild for mingw32-gcc 4.4

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-4
- Requires pkgconfig.

* Tue Jan 27 2009 Levente Farkas <lfarkas@lfarkas.org> - 1.22.1-3
- Include license file in documentation section.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-2
- Disable static libraries.
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-1
- New upstream version 1.22.1.
- BR cairo >= 1.8.0 because of important fixes.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-6
- Rename mingw -> mingw32.

* Tue Sep 23 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-5
- Remove use of wine in %%-post.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-4
- Add dep on pkgconfig

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-3
- post/preun scripts to update the pango.modules list.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-2
- Run the correct glib-mkenums.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-1
- Initial RPM release

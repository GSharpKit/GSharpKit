%?mingw_package_header

Summary:       MinGW Windows Enchanting Spell Checking Library
Name:          mingw-enchant
Version:       1.6.0
Release:       24%{?dist}
License:       LGPLv2+
Source0:       http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
URL:           http://www.abisource.com/

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-glib2
BuildRequires: mingw32-hunspell

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-glib2
BuildRequires: mingw64-hunspell

BuildRequires: m4

BuildArch:     noarch

# Fix a compile issue
Patch0:        enchant-mingw-compile-fix.patch

# Workaround for bug 12755 as upstream isn't alive any more
# Fixes a regression where relocatable support got broken
# http://bugzilla.abisource.com/show_bug.cgi?id=12755
Patch1:        enchant-remove-define-enchant-global-module-dir.patch

%description
A library that wraps other spell checking backends.

This is the MinGW build of enchant


# Win32
%package -n mingw32-enchant
Summary:       MinGW Windows Enchanting Spell Checking Library
Requires:      pkgconfig

%description -n mingw32-enchant
A library that wraps other spell checking backends.

This is the MinGW build of enchant

%package -n mingw32-enchant-static
Summary:       Static version of the MinGW Windows enchant library
Requires:      mingw32-enchant = %{version}-%{release}

%description -n mingw32-enchant-static
Static version of the MinGW Windows enchant spell checking library.

# Win64
%package -n mingw64-enchant
Summary:       MinGW Windows Enchanting Spell Checking Library
Requires:      pkgconfig

%description -n mingw64-enchant
A library that wraps other spell checking backends.

This is the MinGW build of enchant

%package -n mingw64-enchant-static
Summary:       Static version of the MinGW Windows enchant library
Requires:      mingw64-enchant = %{version}-%{release}

%description -n mingw64-enchant-static
Static version of the MinGW Windows enchant spell checking library.


%?mingw_debug_package


%prep
%setup -qn "enchant-%{version}"

%patch0 -p0 -b .mingw
%patch1 -p0 -b .relocatable


%build
%mingw_configure        \
    --disable-ispell    \
    --disable-hspell    \
    --disable-aspell    \
    --enable-static     \
    --enable-shared

# Work around a build issue
pushd build_win32/src
WINDRES=%{mingw32_windres} ../../compile-resource libenchant.rc enchant-win32res.o
popd
pushd build_win64/src
WINDRES=%{mingw64_windres} ../../compile-resource libenchant.rc enchant-win32res.o
popd

%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Drop the man-pages
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-enchant
%doc AUTHORS COPYING.LIB README
%{mingw32_bindir}/enchant-lsmod.exe
%{mingw32_bindir}/enchant.exe
%{mingw32_bindir}/libenchant.dll
%{mingw32_includedir}/enchant/
%dir %{mingw32_libdir}/enchant/
%{mingw32_libdir}/enchant/libenchant_myspell.dll
%{mingw32_libdir}/enchant/libenchant_myspell.dll.a
%{mingw32_libdir}/libenchant.dll.a
%{mingw32_libdir}/pkgconfig/enchant.pc
%{mingw32_datadir}/enchant/

%files -n mingw32-enchant-static
%{mingw32_libdir}/libenchant.a
%{mingw32_libdir}/enchant/libenchant_myspell.a

# Win64
%files -n mingw64-enchant
%doc AUTHORS COPYING.LIB README
%{mingw64_bindir}/enchant-lsmod.exe
%{mingw64_bindir}/enchant.exe
%{mingw64_bindir}/libenchant.dll
%{mingw64_includedir}/enchant/
%dir %{mingw64_libdir}/enchant/
%{mingw64_libdir}/enchant/libenchant_myspell.dll
%{mingw64_libdir}/enchant/libenchant_myspell.dll.a
%{mingw64_libdir}/libenchant.dll.a
%{mingw64_libdir}/pkgconfig/enchant.pc
%{mingw64_datadir}/enchant/

%files -n mingw64-enchant-static
%{mingw64_libdir}/libenchant.a
%{mingw64_libdir}/enchant/libenchant_myspell.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.6.0-22
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 1.6.0-19
- Rebuild (hunspell)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Sandro Mani <manisandro@gmail.com> - 1.6.0-16
- Rebuild (mingw-hunspell)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 1.6.0-13
- Rebuild (hunspell)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.0-8
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Mon Aug 13 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.0-7
- Added workaround for upstream bug 12755
  This fixes a regression where relocatable support got broken

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.0-5
- Added win64 support

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.0-4
- Renamed the source package to mingw-enchant (RHBZ #800863)
- Use mingw macros without leading underscore
- Drop all .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.0-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Kalev Lember <kalevlember@gmail.com> - 1.6.0-1
- Update to 1.6.0
- Dropped all the patches as they are now included upstream

* Thu Jul  7 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-10
- Rebuild against win-iconv

* Wed Apr 27 2011 Kalev Lember <kalev@smartlink.ee> - 1.5.0-9
- Rebuilt for proxy-libintl removal

* Mon Apr 25 2011 Kalev Lember <kalev@smartlink.ee> - 1.5.0-8
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-6
- Rebuild for updated mingw32-hunspell

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-5
- Rebuild in order to have soft dependency on libintl

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-4
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sun Aug 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-3
- Automatically generate debuginfo subpackage

* Sun Aug  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-2
- Dropped BR: autoconf libtool
- Added BR: m4
- Use 'rm -rf $RPM_BUILDROOT' in the %%clean phase
- Fixed a 'strange-permission' rpmlint warning
- Moved the file %%{_mingw32_libdir}/enchant/libenchant_myspell.a to
  the -static subpackage
- Use a more verbose %%files list
- Added a Requires: pkgconfig to the main package
- Added patches from the native enchant package
- Dropped another patch which isn't necessary anymore

* Sat Aug  8 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.5.0-1
- Update to version 1.5.0
- Drop upstreamed patch
- Don't use 'make %%{?_smp_mflags}' as this causes a compile failure in Koji

* Mon May 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.4.2-6
- Ported the native package to have MinGW support
- Dropped the epoch as this is a new package
- Fixed %%defattr line

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 26 2008 Michael Schwendt <mschwendt@fedoraproject.org> 1:1.4.2-4
- Rebuild for ABI-incompatible hunspell-1.2.4.2-2.fc10

* Thu Jul 10 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-3
- Fix 426712: don't build static libs (patch from Michael Schwendt)

* Wed May 21 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-2
- Rebuild

* Wed May 21 2008 Marc Maurer <uwog@abisource.com> 1:1.4.2-1
- New upstream release
- Add voikko support in an enchant-voikko package
- Bump glib-devel BR to 2.6.0

* Fri Feb 08 2008 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-4.fc9
- minor cockup

* Sat Jan 26 2008 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-3.fc9
- Resolves: rhbz#426402 use system hunspell not internal one and 
  split out aspell backend.
- See: rhbz#430354 hspell backend disabled until pic issue fixed

* Wed Dec 19 2007 Caolan McNamara <caolanm@redhat.com> 1:1.3.0-2.fc9
- tell enchant where the myspell dictionaries are

* Thu Oct 12 2006 Marc Maurer <uwog@abisource.com> 1:1.3.0-1.fc6
- Update to 1.3.0

* Mon Sep 11 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-3.fc6
- Rebuild for FC6

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-2.fc6
- Rebuild

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 1:1.2.5-1.fc6
- Package the data dir as well (bug 188516)
- New upstream version
- Add hspell requirement/support

* Tue Feb 14 2006 Marc Maurer <uwog@abisource.com> 1:1.2.2-2.fc5
- Rebuild for Fedora Extras 5

* Sun Feb 05 2006 Marc Maurer <uwog@abisource.com> 1:1.2.2-1.fc5
- Update to 1.2.2

* Mon Jan 30 2006 Marc Maurer <uwog@abisource.com> 1:1.2.1-1.fc5
- Update to 1.2.1
- Drop glib Require

* Sat Oct 22 2005 Marc Maurer <uwog@abisource.com> 1:1.2.0-1.fc5
- Update to 1.2.0

* Wed Oct  5 2005 Marc Maurer <uwog@abisource.com> 1:1.1.6-4.fc5
- Add dist flag to the release number

* Mon Apr  4 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1:1.1.6-3
- make in %%build
- disable bad buildroot rpaths in libs, don't use %%makeinstall
- require %%{epoch} of main package in -devel package (Fridrich Strba)

* Thu Mar 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1:1.1.6-2
- add dep glib2-devel for pkgconfig in -devel package
- include %%{_libdir}/enchant dir in main package
- make -devel package require exact VR of main package
- use -p /sbin/ldconfig in scriptlets

* Mon Mar 28 2005 Marc Maurer <uwog@abisource.com> 1:1.1.6-1
- update to 1.1.6
- drop the manpage patch (RH#145010#)
- fix version numbers in the spec changelog

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-3
- rebuild with gcc4

* Fri Jan 14 2005 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-2
- RH#145010# misformatted manpage

* Mon Dec 20 2004 Caolan McNamara <caolanm@redhat.com> 1:1.1.5-1
- initial fedora import

* Sun Aug 24 2003 Rui Miguel Seabra <rms@1407.org>
- update spec to current stat of affairs
- building from source rpm is now aware of --with and --without flags:
- --without aspell --without ispell --without myspell --with uspell

* Wed Jul 16 2003 Rui Miguel Seabra <rms@1407.org>
- take advantage of environment rpm macros

* Sun Jul 13 2003 Dom Lachowicz <cinamod@hotmail.com>
- Initial version

%{?ucrt_package_header}

Name:           ucrt-libxml2
Version:        2.12.10
Release:        3%{?dist}
Summary:        MinGW Windows libxml2 XML processing library

License:        MIT
URL:            http://xmlsoft.org/
# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        https://download.gnome.org/sources/libxml2/%{release_version}/libxml2-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  automake autoconf libtool
BuildRequires:  make

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-gettext
BuildRequires:  ucrt64-win-iconv
BuildRequires:  ucrt64-zlib


%description
MinGW Windows libxml2 XML processing library.


# Win64
%package -n ucrt64-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig

%description -n ucrt64-libxml2
MinGW Windows libxml2 XML processing library.

%package -n ucrt64-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       ucrt64-libxml2 = %{version}-%{release}

%description -n ucrt64-libxml2-static
Static version of the MinGW Windows XML processing library.


%?ucrt_debug_package


%prep
%autosetup -p1 -n libxml2-%{version}


%build
NOCONFIGURE=1 ./autogen.sh

# LibXML2 can't build static and shared libraries in one go, so we build LibXML2 twice here
mkdir static
pushd static
UCRT64_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL" \
%ucrt64_configure --without-python --with-modules --enable-static --disable-shared --with-threads=win32
%ucrt64_make
popd

mkdir shared
pushd shared
%ucrt64_configure --without-python --with-modules --disable-static --enable-shared --with-threads=win32
%ucrt64_make
popd


%install
pushd static
make install DESTDIR=%{buildroot}
popd
pushd shared
make install DESTDIR=%{buildroot}
popd

# Remove documentation which duplicates Fedora native.
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{ucrt64_docdir}
rm -rf %{buildroot}%{ucrt64_datadir}/gtk-doc/

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win64
%files -n ucrt64-libxml2
%license Copyright
%{ucrt64_bindir}/libxml2-2.dll
%{ucrt64_bindir}/xml2-config
%{ucrt64_bindir}/xmlcatalog.exe
%{ucrt64_bindir}/xmllint.exe
%{ucrt64_libdir}/libxml2.dll.a
%{ucrt64_libdir}/cmake/libxml2/
%{ucrt64_libdir}/pkgconfig/libxml-2.0.pc
%{ucrt64_includedir}/libxml2
%{ucrt64_datadir}/aclocal/*

%files -n ucrt64-libxml2-static
%{ucrt64_libdir}/libxml2.a


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 15 2025 Sandro Mani <manisandro@gmail.com> - 2.12.10-1
- Update to 2.12.10

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Sandro Mani <manisandro@gmail.com> - 2.12.9-1
- Update to 2.12.9

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Sandro Mani <manisandro@gmail.com> - 2.12.8-1
- Update to 2.12.8

* Thu May 16 2024 Richard W.M. Jones <rjones@redhat.com> - 2.12.7-1
- Update to 2.12.7 (RHBZ#2280535, CVE-2024-34459)

* Sun Mar 17 2024 Sandro Mani <manisandro@gmail.com> - 2.12.6-1
- Update to 2.12.6

* Tue Feb 06 2024 Sandro Mani <manisandro@gmail.com> - 2.12.5-1
- Update to 2.12.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Sandro Mani <manisandro@gmail.com> - 2.12.4-1
- Update to 2.12.4

* Tue Dec 12 2023 Sandro Mani <manisandro@gmail.com> - 2.12.3-1
- Update to 2.12.3

* Thu Dec 07 2023 Sandro Mani <manisandro@gmail.com> - 2.12.2-1
- Update to 2.12.2

* Tue Nov 28 2023 Sandro Mani <manisandro@gmail.com> - 2.12.1-1
- Update to 2.12.1

* Tue Nov 21 2023 Sandro Mani <manisandro@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Wed Aug 16 2023 Sandro Mani <manisandro@gmail.com> - 2.11.5-1
- Update to 2.11.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 2.10.4-1
- Update to 2.10.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Sandro Mani <manisandro@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 2.9.14-1
- Update to 2.9.14

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.9.13-3
- Rebuild with ucrt-gcc-12

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 2.9.13-2
- Rebuild

* Tue Feb 22 2022 Sandro Mani <manisandro@gmail.com> - 2.9.13-1
- Update to 2.9.13
- Cleanup spec

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 2.9.12-1
- Update to 2.9.12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Richard W.M. Jones <rjones@redhat.com> - 2.9.10-8
- Add correct fix for CVE-2020-24977 (RHBZ#1877788), thanks: Jan de Groot.

* Fri Sep 11 2020 Richard W.M. Jones <rjones@redhat.com> - 2.9.10-7
- Add fix for CVE-2020-24977 (RHBZ#1877788, RHBZ#1877789).

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 David King <amigadave@amigadave.com> - 2.9.10-1
- Update to 2.9.10
- Fix CVE-2019-19956 (#1788858)
- Fix CVE-2019-20388 (#1799738)
- Fix CVE-2020-7595 (#1799788)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Richard W.M. Jones <rjones@redhat.com> - 2.9.9-2
- Resync with Fedora Rawhide libxml2 2.9.9-2.
- Use autosetup.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.3-1
- Update to 2.9.3
- Fixes various CVE's:
  RHBZ #1213960, #1262853, #1262854, #1274225, #1274226, #1276299
  RHBZ #1276300, #1277149, #1277150, #1281952, #1281953

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2
- Avoid corrupting the xml catalogs
- Fix CVE-2014-0191 (RHBZ #1107557)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.1-3
- Added the license and other %%doc files (RHBZ #980288)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1

* Fri Apr 12 2013 Nicola Fontana <ntd@entidi.it> - 2.9.0-3
- Throw off LDFLAGS and CFLAGS settings (#951472)
- Simplified static libraries installation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-7
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-6
- Dropped .la files

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 2.7.8-5
- Renamed the source package to ucrt-libxml2 (#800440)
- Modernize the spec file
- Use ucrt macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-4
- Rebuild against the ucrt-w64 toolchain

* Fri Jan  6 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-3
- Re-added patch which was dropped in 2.7.8-1 as it is still needed
  to get DTD validation working (GNOME BZ #561340, #663588)

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.7.8-2
- Rebuilt against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.7.8-1
- Update to 2.7.8
- Dropped upstreamed patches
- Use the CVE-2010-4494 patch from Fedora native libxml2 (#665965)

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.7.6-3
- Don't install html documentation which duplicates what is in Fedora native

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.6-1
- Update to 2.7.6
- Updated the configure arguments so that the native Win32 thread API
  will be used instead of pthreads

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.5-2
- Added a patch to fix GNOME bug #561340

* Thu Sep 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-3
- Rebuild because of broken ucrt32-gcc/ucrt32-binutils

* Sat Sep 12 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-2
- Always use the native win32 thread API even when pthreads is available
- Dropped a patch which isn't necessary anymore

* Fri Sep 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-1
- Update to 2.7.4
- Drop upstreamed libxml2-2.7.3-ficora-parse.patch patch
- Added a new patch to fix compatibility with the w32 port of pthreads
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Mon Aug 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-3
- two patches for parsing problems CVE-2009-2414 and CVE-2009-2416

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May  4 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.3-1
- Update to 2.7.3

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.2-9
- Fixed %%defattr line
- Added -static subpackage. Applications which want to link
  against this static library needs to add -DLIBXML_STATIC to the CFLAGS
- This package shouldn't own %%{ucrt32_libdir}/pkgconfig

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-7
- Rebuild for ucrt32-gcc 4.4

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-6
- Rerun autoreconf after patching configure.in (Erik van Pienbroek).
- Rebuild libtool for Rawhide / libtool 2.
- Add BRs dlfcn and iconv.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-5
- Use _smp_mflags.
- Disable static libraries.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-4
- Requires pkgconfig.

* Sat Oct 25 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-3
- Enable modules support for libxslt.

* Fri Oct 17 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-1
- Resynch to native Fedora package + patch.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.1-2
- Rename ucrt -> ucrt32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.7.1-1
- Update to 2.7.1 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-5
- Remove manpages which duplicate Fedora native.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-4
- Remove static libraries.
- List libdir files explicitly.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-3
- Use RPM macros from ucrt-filesystem.
- BuildArch is noarch.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-1
- Initial RPM release, largely based on earlier work from several sources.

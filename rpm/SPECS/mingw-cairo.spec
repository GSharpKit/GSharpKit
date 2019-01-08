%?mingw_package_header

Name:           mingw-cairo
Version:        1.16.0
Release:        4%{?dist}
Summary:        MinGW Windows Cairo library

License:        LGPLv2 or MPLv1.1
URL:            http://cairographics.org
Source0:        http://cairographics.org/snapshots/cairo-%{version}.tar.xz
Group:          Development/Libraries

# Backported upstream patches to add API required by gtk3
#Patch0:         0001-win32-Add-cairo-API-to-set-up-a-Win32-surface-for-an.patch
#Patch1:         0002-win32-Add-a-win32-boilerplate-that-uses-a-real-windo.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 104
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-glib2

BuildRequires:  mingw64-filesystem >= 104
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-glib2

BuildRequires:  mingw-w64-tools
BuildRequires:  pkgconfig


%description
MinGW Windows Cairo library.


# Win32
%package -n mingw32-cairo
Summary:        MinGW Windows Cairo library
Requires:       mingw32-fontconfig
Requires:       mingw32-freetype
Requires:       pkgconfig

%description -n mingw32-cairo
MinGW Windows Cairo library.

%package -n mingw32-cairo-static
Summary:        Static version of the MinGW Windows Cairo library
Requires:       mingw32-cairo = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw32-cairo-static
Static version of the MinGW Windows Cairo library.

# Win64
%package -n mingw64-cairo
Summary:        MinGW Windows Cairo library
Requires:       mingw64-fontconfig
Requires:       mingw64-freetype
Requires:       pkgconfig

%description -n mingw64-cairo
MinGW Windows Cairo library.

%package -n mingw64-cairo-static
Summary:        Static version of the MinGW Windows Cairo library
Requires:       mingw64-cairo = %{version}-%{release}
Group:          Development/Libraries

%description -n mingw64-cairo-static
Static version of the MinGW Windows Cairo library.


%?mingw_debug_package


%prep
%setup -q -n cairo-%{version}
#patch0 -p1
#patch1 -p1


%build
# Function to generate an import library for delay-loading
gen_delay_lib()
{
    local DLL="$1"
    local OUT_IMPLIB="$2"

    gendef - "%{mingw32_bindir}/$DLL" > build_win32/delay_load.def
    %{mingw32_dlltool} --def build_win32/delay_load.def --kill-at --output-delaylib "build_win32/$OUT_IMPLIB"

    gendef - "%{mingw64_bindir}/$DLL" > build_win64/delay_load.def
    %{mingw64_dlltool} --def build_win64/delay_load.def --kill-at --output-delaylib "build_win64/$OUT_IMPLIB"
}

mkdir build_win32
mkdir build_win64

# Generate import libs for delay-loading fontconfig and freetype
gen_delay_lib libfontconfig-1.dll libfontconfig-delayed.dll.a
gen_delay_lib libfreetype-6.dll libfreetype-delayed.dll.a

MINGW_CONFIGURE_ARGS=" \
  ax_cv_c_float_words_bigendian=no \
  --disable-pthread \
  --disable-xlib \
  --disable-xcb \
  --enable-win32 \
  --enable-fc \
  --enable-ft \
  --enable-png \
  --enable-static \
  --enable-gobject \
  --enable-tee"

# The regular %%mingw_configure macro can't be used here as we need to inject custom
# environment variables which are different between the win32 and win64 build
pushd build_win32
    %mingw32_configure \
        FONTCONFIG_LIBS="-L`pwd` -lfontconfig-delayed" \
        FREETYPE_LIBS="-L`pwd` -lfreetype-delayed"
popd

pushd build_win64
    %mingw64_configure \
        FONTCONFIG_LIBS="-L`pwd` -lfontconfig-delayed" \
        FREETYPE_LIBS="-L`pwd` -lfreetype-delayed"
popd

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/charset.alias

rm -r $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -r $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-cairo
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{mingw32_bindir}/libcairo-2.dll
%{mingw32_bindir}/libcairo-gobject-2.dll
%{mingw32_bindir}/libcairo-script-interpreter-2.dll
%{mingw32_includedir}/cairo/
%{mingw32_libdir}/libcairo.dll.a
%{mingw32_libdir}/libcairo-gobject.dll.a
%{mingw32_libdir}/libcairo-script-interpreter.dll.a
%{mingw32_libdir}/pkgconfig/cairo-fc.pc
%{mingw32_libdir}/pkgconfig/cairo-ft.pc
%{mingw32_libdir}/pkgconfig/cairo-gobject.pc
%{mingw32_libdir}/pkgconfig/cairo-pdf.pc
%{mingw32_libdir}/pkgconfig/cairo-png.pc
%{mingw32_libdir}/pkgconfig/cairo-ps.pc
%{mingw32_libdir}/pkgconfig/cairo-script.pc
%{mingw32_libdir}/pkgconfig/cairo-svg.pc
%{mingw32_libdir}/pkgconfig/cairo-tee.pc
%{mingw32_libdir}/pkgconfig/cairo-win32-font.pc
%{mingw32_libdir}/pkgconfig/cairo-win32.pc
%{mingw32_libdir}/pkgconfig/cairo.pc

%files -n mingw32-cairo-static
%{mingw32_libdir}/libcairo.a
%{mingw32_libdir}/libcairo-gobject.a
%{mingw32_libdir}/libcairo-script-interpreter.a

# Win64
%files -n mingw64-cairo
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{mingw64_bindir}/libcairo-2.dll
%{mingw64_bindir}/libcairo-gobject-2.dll
%{mingw64_bindir}/libcairo-script-interpreter-2.dll
%{mingw64_includedir}/cairo/
%{mingw64_libdir}/libcairo.dll.a
%{mingw64_libdir}/libcairo-gobject.dll.a
%{mingw64_libdir}/libcairo-script-interpreter.dll.a
%{mingw64_libdir}/pkgconfig/cairo-fc.pc
%{mingw64_libdir}/pkgconfig/cairo-ft.pc
%{mingw64_libdir}/pkgconfig/cairo-gobject.pc
%{mingw64_libdir}/pkgconfig/cairo-pdf.pc
%{mingw64_libdir}/pkgconfig/cairo-png.pc
%{mingw64_libdir}/pkgconfig/cairo-ps.pc
%{mingw64_libdir}/pkgconfig/cairo-script.pc
%{mingw64_libdir}/pkgconfig/cairo-svg.pc
%{mingw64_libdir}/pkgconfig/cairo-tee.pc
%{mingw64_libdir}/pkgconfig/cairo-win32-font.pc
%{mingw64_libdir}/pkgconfig/cairo-win32.pc
%{mingw64_libdir}/pkgconfig/cairo.pc

%files -n mingw64-cairo-static
%{mingw64_libdir}/libcairo.a
%{mingw64_libdir}/libcairo-gobject.a
%{mingw64_libdir}/libcairo-script-interpreter.a


%changelog
* Thu Apr 21 2016 Kalev Lember <klember@redhat.com> - 1.14.6-1
- Update to 1.14.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Kalev Lember <klember@redhat.com> - 1.14.4-1
- Update to 1.14.4

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 1.14.2-3
- Backport upstream patches to add API required by gtk3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Kalev Lember <kalevlember@gmail.com> - 1.14.2-1
- Update to 1.14.2
- Use the license macro for COPYING files

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.18-1
- Update to 1.12.18

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.16-2
- Fix build against gcc 4.9 by disabling LTO
  Thanks to LRN for the hint

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.16-1
- Update to 1.12.16

* Sun Aug  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.14-5
- Fix assertion failure when using the latest gtk3 (RHBZ #991829, FD BZ #63787)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.14-3
- Rebuild against libpng 1.6

* Tue Apr  2 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.12.14-2
- Fix corrupted drawing, cherry-picked from upstream (fdo#61876)
- Add a few windows related fixes

* Fri Mar 29 2013 Kalev Lember <kalevlember@gmail.com> - 1.12.14-1
- Update to 1.12.14

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.10-1
- Update to 1.12.10

* Fri Nov 23 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.8-1
- Update to 1.12.8

* Fri Oct 26 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.6-1
- Update to 1.12.6

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.2-13
- Manually Require fontconfig and freetype, now that they are delay-loaded

* Sat Mar 17 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-12
- Make freetype/fontconfig an optional runtime dependency (delay-load)

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-11
- Added win64 support
- Enable tee support

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-10
- Renamed the source package to mingw-cairo (RHBZ #800373)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-9
- Rebuild against the mingw-w64 toolchain

* Thu Feb 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.2-8
- Enable cairo-fc and cairo-ft
  (needed by e.g. poppler and webkitgtk freetype font backend)

* Thu Feb 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.2-7
- Apply patches recommended by the GTK+ Windows team:
- Fix A1 format win32 surfaces
- Reset clip region when writing fallback results

* Tue Jan 24 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-6
- Rebuild against libpng 1.5
- Dropped .la files
- Dropped unneeded RPM tags

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.10.2-4
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 1.10.2-3
- Really rebuild without proxy-libintl

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.2-2
- Dropped the proxy-libintl pieces

* Mon Apr 25 2011 Kalev Lember <kalev@smartlink.ee> - 1.10.2-1
- Update to 1.10.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-2
- Rebuild in order to have soft dependency on libintl

* Fri Sep 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0
- Added the GObject library
- Fixed a small rpmlint warning

* Sun Jul  4 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.10-2
- Rebuild for libpng 1.4

* Wed Feb 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.10-1
- Update to 1.8.10
- Dropped BR: mingw32-dlfcn as it's unneeded

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.8-1
- Update to 1.8.8
- Automatically generate debuginfo subpackage
- Use %%global instead of %%define

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.6-2
- Fixed %%defattr line
- Added -static subpackage
- Use ./configure --disable-pthread to avoid conflict with native pthread library

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.6-1
- Rebase to 1.8.6, same as Fedora native version.
- Source URL corrected.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-8
- Rebuild for mingw32-gcc 4.4

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-7
- Remove gtk-doc (Levente Farkas).

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-6
- Requires pkgconfig (Erik van Pienbroek).

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-5
- Don't need to remove extra pkgconfig file in install section.

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-4
- Disable freetype in configure so it doesn't break if freetype
  or fontconfig are actually installed. (Erik van Pienbroek).

* Mon Jan 19 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-3
- Include license file in documentation section.
- Disable building static library to save time.
- Remove BRs on mingw32-fontconfig and mingw32-freetype which are
  not needed on Win32.
- Use _smp_mflags.
- Added BRs mingw32-dlfcn, mingw32-iconv, mingw32-zlib.

* Wed Oct 29 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-2
- Fix mixed spaces/tabs in specfile.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-1
- New upstream version 1.8.0.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.4-4
- Rename mingw -> mingw32.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.7.4-3
- Added dep on pkgconfig

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.7.4-2
- Remove static libraries.
- Fix source URL.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.7.4-1
- Initial RPM release

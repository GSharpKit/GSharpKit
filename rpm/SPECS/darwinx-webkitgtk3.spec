%define debug_package %{nil}

Name:		darwinx-webkitgtk3
Version:	2.4.11
Release:	1%{?dist}
Summary:	Darwin web content engine library

Group:		Development/Libraries
License:	LGPLv2+ and BSD
URL:		http://webkit.org/

Source0:	http://www.webkitgtk.org/webkitgtk-%{version}.tar.xz

Patch0:		webkitgtk-2.4.9-plugin-quartz.patch
Patch1:		webkitgtk-2.2.6-plugin.patch
Patch2:		webkitgtk-2.4.11-icu.patch
Patch3:		webkitgtk-2.2.6-idl.patch
Patch4:		webkitgtk-2.2.6-gstreamer.patch
Patch5:		webkitgtk-2.4.11-jpeg.patch

Patch10:	webkitgtk-2.4.11-cast_uchar.patch
Patch11:	webkitgtk-2.4.11-semicolon.patch
Patch12:	webkitgtk-2.4.11-js.patch
Patch13:	webkitgtk-2.4.11-inline.patch
Patch14:	webkitgtk-2.4.11-no-jsc-objc.patch
Patch15:	webkitgtk-2.4.11-asm.patch
Patch16:	patch-qtwebkit_fix_page_shift.diff
Patch17:	webkitgtk-2.4.11-bison.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:  ruby
BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-odcctools
BuildRequires:  darwinx-sdk
BuildRequires:	darwinx-icu
BuildRequires:	darwinx-gtk3
BuildRequires:	darwinx-sqlite
BuildRequires:	darwinx-libxml2
BuildRequires:	darwinx-libxslt
BuildRequires:	darwinx-libsoup
BuildRequires:	darwinx-enchant
BuildRequires:	darwinx-gstreamer1
BuildRequires:	darwinx-gstreamer1-plugins-base

Requires:	darwinx-filesystem >= 18

%description 
%{name} is an open-source Web content engine library.
This package contains the shared libraries for the WebKit GTK+ port
as well as the sample GtkLauncher tool. 

%prep
%setup -qn "webkitgtk-%{version}"
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p0
%patch 5 -p1

%patch 10 -p1
%patch 11 -p1
%patch 12 -p1
%patch 13 -p1
%patch 14 -p1
%patch 15 -p1

%patch 16 -p0
%patch 17 -p1

%{_darwinx_env}
autoreconf --verbose --install -I Source/autotools

mkdir -p DerivedSources/InjectedBundle
mkdir -p DerivedSources/webkit
mkdir -p DerivedSources/webkitdom
mkdir -p DerivedSources/WebKit2/webkit2gtk/webkit2
mkdir -p DerivedSources/WebKit2/include
mkdir -p DerivedSources/WebCore
mkdir -p DerivedSources/Platform

sed -i '' 's!python!python3!g' configure
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/inline-and-minify-stylesheets-and-scripts.py
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/generate-combined-inspector-json.py
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/jsmin.py
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/cssmin.py
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/CodeGeneratorInspector.py
sed -i '' 's!python!python3!g' Source/JavaScriptCore/inspector/scripts/CodeGeneratorInspector.py
sed -i '' 's!python!python3!g' Source/WebKit2/Scripts/generate-messages-header.py
sed -i '' 's!python!python3!g' Source/WebKit2/Scripts/generate-message-receiver.py
sed -i '' 's!python!python3!g' Source/WebCore/html/parser/create-html-entity-table
sed -i '' 's!python!python3!g' Tools/gtk/check-for-webkitdom-api-breaks
sed -i '' 's!python!python3!g' Tools/gtk/webkitdom.py
sed -i '' 's!python!python3!g' Tools/gtk/common.py
sed -i '' 's!python!python3!g' Tools/gtk/generate-feature-defines-files
sed -i '' 's!python!python3!g' Tools/gtk/generate-inspector-gresource-manifest.py
sed -i '' 's!python!python3!g' Tools/gtk/generate-gtkdoc

#sed -i '' 's!-ljpeg!-L/Library/Frameworks/GSharpKit/lib -lturbojpeg!g' configure
sed -i '' 's!#define USE_ACCELERATE_FFT 1!#define USE_ACCELERATE_FFT 0!g' Source/WebCore/platform/audio/FFTFrame.h


%build
%global _darwinx_cflags %(echo %{_darwinx_cflags} | sed 's/-g /-g1 /') -fpermissive -DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_64 -DASSERT_ENABLED=0

#DARWINX_CFLAGS="-Qunused-arguments" DARWINX_CXXFLAGS="-pthread -std=c++11 -Wno-c++11-compat -Wno-error=c++11-narrowing -ftemplate-depth=256 -stdlib=libc++ -Wno-c++11-extensions -Qunused-arguments" DARWINX_CPPFLAGS="-DGTEST_HAS_TR1_TUPLE=0" DARWINX_LDFLAGS="-stdlib=libc++"
DARWINX_CXXFLAGS="-std=c++11 -Wno-c++11-compat -Wno-error=c++11-narrowing -ftemplate-depth=256 -stdlib=libc++ -DDISABLE_BUILTIN_CLEAR_CACHE=1 -DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_64 -DASSERT_ENABLED=0" DARWINX_CPPFLAGS="-DGTEST_HAS_TR1_TUPLE=0 -I/Library/Frameworks/GSharpKit/include -DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_64 -DASSERT_ENABLED=0" DARWINX_LDFLAGS="-stdlib=libc++" %{_darwinx_configure} \
	--enable-quartz-target			\
	--with-gtk=3.0                          \
	--disable-accelerated-compositing       \
	--disable-egl                           \
	--disable-credential-storage            \
	--disable-geolocation                   \
	--disable-webkit2                       \
	--disable-jit				\
	--disable-gtk-doc-html

#make %{?_smp_mflags} V=99
make V=99

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}
install -m 755 Programs/.libs/GtkLauncher %{buildroot}%{_darwinx_bindir}

rm -rf %{buildroot}%{_darwinx_datadir}/gtk-doc 
rm -rf %{buildroot}/webkitgtk
rm -rf %{buildroot}/webkitdomgtk

%find_lang webkitgtk --all-name

%clean
rm -rf %{buildroot}

%files -f webkitgtk.lang
%defattr(-,root,wheel,-)
%{_darwinx_bindir}/jsc-3
%{_darwinx_bindir}/GtkLauncher

%{_darwinx_includedir}/webkitgtk-3.0/

%{_darwinx_libdir}/libwebkitgtk-3.0.0.dylib
%{_darwinx_libdir}/libwebkitgtk-3.0.dylib
%{_darwinx_libdir}/libjavascriptcoregtk-3.0.0.dylib
%{_darwinx_libdir}/libjavascriptcoregtk-3.0.dylib

%{_darwinx_libdir}/pkgconfig/javascriptcoregtk-3.0.pc
%{_darwinx_libdir}/pkgconfig/webkitgtk-3.0.pc

%{_darwinx_datadir}/webkitgtk-3.0

%changelog
* Wed Jan 30 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.9-2
- Updated to Gtk3

* Thu Oct 15 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.15-4
- And some more features

* Wed Oct 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.15-3
- Enabled some more features

* Sun Oct 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.15-2
- Ported the MinGW package to Darwin

* Thu Sep 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.15-1
- Update to 1.1.15

* Sun Sep 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.14-1
- Update to 1.1.14

* Tue Sep  5 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.13-1
- Update to 1.1.13
- Added several patches to get this package compiled

* Wed Aug 19 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.12-1
- Update to 1.1.12
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage
- Dropped the strip command in the %%install phase as that's now done automatically
- Updated the patches 1-1.1.5-replace_icu_with_glib_idn.diff and 2-1.1.5-mingw.diff

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Sun May 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6
- Updated the patches to apply cleanly against version 1.1.6
- Renamed the package to mingw32-webkitgtk
- Merged the changes from the native webkitgtk package up to 1.1.6-1
- Added a BR: mingw32-enchant (required as of version 1.1.6)

* Sat Apr 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.5-1
- Adjusted native WebKit .spec file so that it supports mingw32
- Update to 1.1.5
- Updated Source URL
- Added patches from Mikkel Kruse Johnsen for compilation on Win32 environments

* Sat Mar 07 2009 Peter Gordon <peter@thecodergeek.com> - 1.1.1-1
- Update to new upstream release (1.1.1), includes a soname bump.
- Enable gnome-keyring support.

* Wed Mar  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1.0-0.21.svn41071
- Compile libJavaScriptCore.a with -fno-strict-aliasing to
  do workaround for #488112

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.20.svn41071
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Peter Gordon <peter@thecodergeek.com> 1.1.0-0.19.svn41071
- Update to new upstream snapshot (SVN 41071).
- Drop libsoup build conditional. Use libsoup as default HTTP backend instead
  of cURL, following upstream's default.

* Fri Jan 30 2009 Peter Gordon <peter@thecodergeek.com> 1.1.0-0.18.svn40351
- Fix ownership of doc directory...this time without the oops (#473619).
- Bump package version number to match that used in the configure/build
  scripts. (Thanks to Martin Sourada for the bug report via email.)

* Thu Jan 29 2009 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.17.svn40351
- Update to new upstream snapshot (SVN 40351): adds the WebPolicyDelegate
  implementaton and related API (#482739).
- Drop Bison 2.4 patch (fixed upstream):
  - bison24.patch
- Fixes CVE-2008-6059: Sensitive information disclosure from cookies via
  XMLHttpRequest calls (#484197).

* Sat Nov 29 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.16.svn39370
- Update to new upstream snapshot (SVN 39370)
- Fix ownership of %%_docdir in the doc subpackage. 
- Resolves: bug 473619 (WebKit : Unowned directories).
- Adds webinspector data to the gtk-devel subpackage.
- Add patch from upstream bug 22205 to fix compilation errors with Bison 2.4:
  + bison24.patch
- Add build-time conditional for WML support.

* Thu Oct 23 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.15.svn37790
- Update to new upstream snapshot (SVN 37790).
- Default to freetype font backend for improved CJK/Unicode support. (#448693)
- Add some notes to the build options comments block.
- Add a build-time conditional for jit

* Sun Aug 24 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.14.svn35904
- Update to new upstream snapshot (SVN 35904)

* Fri Jul 04 2008 Peter Gordon <peter@thecodergeek.com>
- Remove outdated and unnecessary GCC 4.3 patch:
  - gcc43.patch
- Fix the curl-devel BuildRequire conditional. (It is only needed when building
  against curl instead of libsoup.)

* Thu Jun 12 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.13.svn34655
- Update to new upstream snapshot (SVN 34655)
- Add some build-time conditionals for non-default features: debug, 
  html5video, libsoup, pango, svg. 

* Tue Jun  3 2008 Caolán McNamara <caolanm@redhat.com> - 1.0.0-0.12.svn34279
- rebuild for new icu

* Tue Jun  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.0-0.11.svn34279
- Update to new upstream snapshot (SVN 34279) anyway
- Add BR: libXt-devel

* Tue Apr 29 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.10.svn32531
- Remove the -Qt subpackage stuff. QtWebKit is now included in Qt proper, as
  of qt-4.4.0-0.6.rc1. (We no longer need separate build-qt and build-gtk
  subdirectories either.)
- Reference: bug 442200 (RFE: WebKit Migration)
- Add libjpeg dependency (was previously pulled in by the qt4-devel dependency
  tree).

* Mon Apr 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.0-0.9.svn32531
- Update to new upstream snapshot (SVN 32531).
- Fix bug 443048 and hopefully fix bug 444445
- Modify the process of building GTK+ port a bit
- on qt port WebKit/qt/Plugins is not built for qt >= 4.4.0

* Sat Apr 12 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.8.svn31787
- Update to new upstream snapshot (SVN 31787).
- Resolves: CVE-2008-1010 (bug 438532: Arbitrary code execution) and
  CVE-2008-1011 (bug 438531: Cross-Site Scripting).
- Switch to using autotools for building the GTK+ port.

* Wed Mar 05 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.7.svn30667
- Fix the WebKitGtk pkgconfig data (should depend on gtk+-2.0). Resolves
  bug 436073 (Requires: gtk+-2.0 missing from WebKitGtk.pc).
- Thanks to Mamoru Tasaka for helping find and squash these many bugs. 
  
* Sat Mar 01 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.6.svn30667
- Fix include directory naming. Resolves: bug 435561 (Header file <> header
  file location mismatch)
- Remove qt4-devel runtime dependency and .prl file from WebKit-gtk-devel.
  Resolves: bug 433138 (WebKit-gtk-devel has a requirement on qt4-devel) 

* Fri Feb 29 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.5.svn30667
- Update to new upstream snapshot (SVN 30667)
- Add some build fixes for GCC 4.3:
  + gcc43.patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-0.5.svn29336
- Autorebuild for GCC 4.3

* Wed Jan 09 2008 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.4.svn29336
- Update to new upstream snapshot (SVN 29336).
- Drop TCSpinLock pthread workaround (fixed upstream):
  - TCSpinLock-use-pthread-stubs.patch

* Thu Dec 06 2007 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.3.svn28482
- Add proper %%defattr line to qt, qt-devel, and doc subpackages.
- Add patch to forcibly build the TCSpinLock code using the pthread
  implementation:
  + TCSpinLock-use-pthread-stubs.patch

* Thu Dec 06 2007 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.2.svn28482
- Package renamed from WebKitGtk.
- Update to SVN 28482.
- Build both the GTK and Qt ports, putting each into their own respective
  subpackages.
- Invoke qmake-qt4 and make directly (with SMP build flags) instead of using
  the build-webkit script from upstream.
- Add various AUTHORS, README, and LICENSE files (via the doc subpackage). 

* Tue Dec 04 2007 Peter Gordon <peter@thecodergeek.com> 1.0.0-0.1.svn28383
- Initial packaging for Fedora.

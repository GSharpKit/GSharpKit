# Fix rebuild on non-Fedora
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global         add_to_doc_files()      \
        mkdir -p %{buildroot}%{_pkgdocdir} ||: ; \
        cp -p %1  %{buildroot}%{_pkgdocdir}/$(echo '%1' | sed -e 's!/!.!g')


%define rel_version 2.4.11

Name:           webkitgtk3
Version:        2.4.12
Release:        3%{?dist}
Summary:        GTK+ Web content engine library

Group:          Development/Libraries
License:        LGPLv2+ and BSD
URL:            http://www.webkitgtk.org/

Source0:        http://webkitgtk.org/releases/webkitgtk-%{rel_version}.tar.xz

# https://bugs.webkit.org/show_bug.cgi?id=142074
Patch0:         webkitgtk-2.4.8-user-agent.patch
Patch1:         webkitgtk-2.4.9-abs.patch
Patch2:         webkitgtk-2.4.11-ruby.patch
Patch3:         webkitgtk-2.4.11-js.patch
Patch4:         webkitgtk-2.4.11-semicolon.patch

Patch6:         webkitgtk-2.4.11-inline.patch
Patch7:         webkitgtk-2.4.11-icu.patch
Patch8:         webkitgtk-2.4.11-bison.patch

Patch9:         webkitgtk-2.4.11-context-menu.patch
Patch10:        webkitgtk-2.4.11-right-click.patch
Patch11:	webkitgtk-2.4.11-growPropertyStorage.patch
Patch12:        webkitgtk-2.4.11-wchar.patch
Patch14:        webkitgtk-2.4.11-icu76.patch

BuildRequires:  at-spi2-core-devel
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  chrpath
BuildRequires:  enchant-devel
BuildRequires:  flex
BuildRequires:  fontconfig-devel >= 2.5
BuildRequires:  freetype-devel
BuildRequires:  geoclue2-devel
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk3-devel >= 3.6
BuildRequires:  gtk-doc
BuildRequires:  glib2-devel >= 2.36.0
BuildRequires:  harfbuzz-devel
BuildRequires:  libsoup-devel >= 2.42.0
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsecret-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxslt-devel
BuildRequires:  libXt-devel
BuildRequires:  pcre-devel
BuildRequires:  sqlite-devel
BuildRequires:  gobject-introspection-devel >= 1.32.0
BuildRequires:  perl-Switch
BuildRequires:  ruby rubypick rubygems
BuildRequires:  mesa-libGL-devel
%ifarch ppc
BuildRequires:  libatomic
%endif
Requires:       geoclue2

%description
WebKitGTK+ is the port of the portable web rendering engine WebKit to the
GTK+ platform.

This package contains an insecure and deprecated version of WebKitGTK+ for GTK+ 3. Use WebKit2 instead.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains developer documentation for %{name}.

%prep
%setup -qn "webkitgtk-%{rel_version}"
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 10 -p1
%patch 11 -p0
%patch 12 -p1
%patch 14 -p1

%build
# Use linker flags to reduce memory consumption
%global optflags %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads

%ifarch s390 %{arm} mips mipsel
# Decrease debuginfo verbosity to reduce memory consumption even more
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

%ifarch ppc
# Use linker flag -relax to get WebKit2 build under ppc(32) with JIT disabled
%global optflags %{optflags} -Wl,-relax
%endif

%ifarch s390 s390x ppc %{power64} aarch64 %{mips}
%global optflags %{optflags} -DENABLE_YARR_JIT=0
%endif

# Workaround crashes with gcc 6.1
%global optflags %{optflags} -fno-delete-null-pointer-checks -fpermissive -DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_64

%if 0%{?fedora}
%global optflags %{optflags} -DUSER_AGENT_GTK_DISTRIBUTOR_NAME=\'\\"Fedora\\"\'
%endif

%configure                                                      \
                        --with-gtk=3.0                          \
                        --enable-web-audio                      \
                        --enable-video                          \
                        --disable-webgl                         \
                        --disable-accelerated-compositing       \
                        --disable-jit                           \
                        --disable-egl                           \
                        --disable-credential-storage            \
                        --disable-geolocation                   \
                        --disable-webkit2                       \
                        --disable-gtk-doc-html

mkdir -p DerivedSources/webkit
mkdir -p DerivedSources/WebCore
mkdir -p DerivedSources/ANGLE
mkdir -p DerivedSources/WebKit2
mkdir -p DerivedSources/webkitdom/
mkdir -p DerivedSources/InjectedBundle
mkdir -p DerivedSources/Platform
mkdir -p DerivedSources/WebKit2/webkit2gtk/webkit2

# Disable the parallel compilation as it fails to compile in brew.
# https://bugs.webkit.org/show_bug.cgi?id=34846
#make %{_smp_mflags} V=1
make -j1 V=1

%install
make install DESTDIR=%{buildroot}

install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libexecdir}/%{name}

# Remove lib64 rpaths
chrpath --delete %{buildroot}%{_bindir}/jsc-3
chrpath --delete %{buildroot}%{_libdir}/libwebkitgtk-3.0.so
chrpath --delete %{buildroot}%{_libexecdir}/%{name}/GtkLauncher

# Remove .la files
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -delete

%find_lang WebKitGTK-3.0

## Finally, copy over and rename the various files for %%doc inclusion.
%add_to_doc_files Source/WebKit/LICENSE
%add_to_doc_files Source/WebKit/gtk/NEWS
%add_to_doc_files Source/WebCore/icu/LICENSE
%add_to_doc_files Source/WebCore/LICENSE-APPLE
%add_to_doc_files Source/WebCore/LICENSE-LGPL-2
%add_to_doc_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_doc_files Source/JavaScriptCore/COPYING.LIB
%add_to_doc_files Source/JavaScriptCore/THANKS
%add_to_doc_files Source/JavaScriptCore/AUTHORS
%add_to_doc_files Source/JavaScriptCore/icu/README
%add_to_doc_files Source/JavaScriptCore/icu/LICENSE


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f WebKitGTK-3.0.lang
%doc %{_pkgdocdir}/
%{_libdir}/libwebkitgtk-3.0.so.*
%{_libdir}/libjavascriptcoregtk-3.0.so.*
%{_libdir}/girepository-1.0/WebKit-3.0.typelib
%{_libdir}/girepository-1.0/JavaScriptCore-3.0.typelib
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/GtkLauncher
%{_datadir}/webkitgtk-3.0

%files  devel
%{_bindir}/jsc-3
%{_includedir}/webkitgtk-3.0
%{_libdir}/libwebkitgtk-3.0.so
%{_libdir}/libjavascriptcoregtk-3.0.so
%{_libdir}/pkgconfig/webkitgtk-3.0.pc
%{_libdir}/pkgconfig/javascriptcoregtk-3.0.pc
%{_datadir}/gir-1.0/WebKit-3.0.gir
%{_datadir}/gir-1.0/JavaScriptCore-3.0.gir

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/webkitgtk
%{_datadir}/gtk-doc/html/webkitdomgtk

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.4.11-4
- Rebuild (libwebp)

* Fri Jun 24 2016 Tomas Popela <tpopela@redhat.com> - 2.4.11-3
- Workaround crashes with gcc 6.1
- rhbz#1349856 - Programs using webkitgtk3 compiled with gcc 6.1 crash on start. F.e: midori, xombrero, etc.

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.4.11-2
- rebuild for ICU 57.1

* Mon Apr 11 2016 Tomas Popela <tpopela@redhat.com> - 2.4.11-1
- Update to 2.4.11

* Tue Apr 05 2016 Tomas Popela <tpopela@redhat.com> - 2.4.10-4
- Fix the compilation on aarch64

* Tue Apr 05 2016 Tomas Popela <tpopela@redhat.com> - 2.4.10-3
- rhbz#1321722 - [abrt] evolution: WTF::StringImpl::startsWith(): SIGSEGV with webkitgtk3-2.4.10

* Thu Mar 24 2016 Tomas Popela <tpopela@redhat.com> - 2.4.10-2
- Add a workaround for rhbz#1320240

* Mon Mar 14 2016 Tomas Popela <tpopela@redhat.com> - 2.4.10-1
- Update to 2.4.10

* Tue Feb  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.9-10
- Add ruby deps for build

* Sat Feb 06 2016 Tomas Popela <tpopela@redhat.com> - 2.4.9-9
- Fix the build with gcc 6 (use Kevin's patch from the webkitgtk package)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Michal Toman <mtoman@fedoraproject.org> - 2.4.9-7
- Add support for MIPS

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.9-6
- Rebuilt for libwebp soname bump

* Mon Dec 07 2015 Tomas Popela <tpopela@redhat.com> - 2.4.9-5
- rhbz#1289053 - Retire nspluginwrapper and remove from Fedora 24

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.4.9-4
- rebuild for ICU 56.1

* Fri Sep 25 2015 Tomas Popela <tpopela@redhat.com> - 2.4.9-3
- rhbz#1189303 - [abrt] midori: WebCore::SQLiteStatement::prepare(): midori killed by SIGSEGV
  Initialize string in SQLiteStatement before using it

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 20 2015 Tomas Popela <tpopela@redhat.com> - 2.4.9-1
- Update to 2.4.9

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.8-9
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 2.4.8-7
- Remove the fix for late certificate validation because we use --disable-webkit2

* Tue Mar 17 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 2.4.8-7
- Backport fix for late certificate validation

* Tue Mar 10 2015 Tomas Popela <tpopela@redhat.com> - 2.4.8-6
- Backport fix for use-after-free when destroying frame

* Fri Feb 27 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 2.4.8-5
- Add Fedora branding to the user agent

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.4.8-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 18 2015 Tomas Popela <tpopela@redhat.com> - 2.4.8-3
- Add support for gcc 5.0
- Let the package compile with latest glib

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.4.8-2
- rebuild for ICU 54.1

* Wed Jan 07 2015 Tomas Popela <tpopela@redhat.com> - 2.4.8-1
- Update to 2.4.8

* Wed Oct 22 2014 Tomas Popela <tpopela@redhat.com> - 2.4.7-1
- Update to 2.4.7

* Tue Oct 21 2014 Tomas Popela <tpopela@redhat.com> - 2.4.6-2
- Disable the SSLv3 to address the POODLE vulnerability

* Mon Sep 29 2014 Tomas Popela <tpopela@redhat.com> - 2.4.6-1
- Update to 2.4.6
- Run make with -j1 to let it successfully compile in brew

* Tue Sep 02 2014 Tomas Popela <tpopela@redhat.com> - 2.4.5-4
- Rebase the aarch64 patch

* Tue Aug 26 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.5-3
- Disable support for webkit2 API which is now provided by the webkitgtk4
  package

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.4.5-2
- rebuild for ICU 53.1

* Tue Aug 26 2014 Tomas Popela <tpopela@redhat.com> - 2.4.5-1
- Update to 2.4.5

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Tomas Popela <tpopela@redhat.com> - 2.4.4-4
- Remove geoclue-devel from BR

* Wed Jul 23 2014 Tomas Popela <tpopela@redhat.com> - 2.4.4-3
- Fix CLoop on ppc32 and s390
- Add geoclue-devel as BR as WK1 needs it

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.4-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jul 08 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Fri Jul  4 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.3-4
- Fix for 64k pages on aarch64 (#1074093, #1113345)

* Fri Jul 04 2014 Tomas Popela <tpopela@redhat.com> 2.4.3-3
- rhbz#1088480 - [abrt] libwebkit2gtk: TSymbolTableLevel::~TSymbolTableLevel(): WebKitWebProcess killed by SIGSEGV

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Tomas Popela <tpopela@redhat.com> 2.4.3-1
- Update to 2.4.3

* Sun May 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.2-4
- Fix aarch64 build

* Wed May 14 2014 Tomas Popela <tpopela@redhat.com> 2.4.2-3
- Add support for ppc64le
- Fix for CLoop on ppc64, ppc64le and s390x

* Tue May 13 2014 Karsten Hopp <karsten@redhat.com> 2.4.2-2
- PPC (32bit) needs libatomic in the buildroot

* Mon May 12 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.1-2
- Make sure -devel pulls in libwebkit2gtk

* Mon Apr 14 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Wed Mar 19 2014 Kalev Lember <kalevlember@gmail.com> - 2.3.92-2
- Switch over to geoclue2

* Tue Mar 18 2014 Tomas Popela <tpopela@redhat.com> - 2.3.92-1
- Update to 2.3.92

* Tue Mar 4 2014 Tomas Popela <tpopela@redhat.com> - 2.3.91-1
- Update to 2.3.91

* Thu Feb 27 2014 Karsten Hopp <karsten@redhat.com> 2.3.90-3
- disable libatomic patch on ppc. webkitgtk3 now uses std::atomic

* Tue Feb 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.90-2
- Disable JIT on aarch64

* Tue Feb 18 2014 Tomas Popela <tpopela@redhat.com> - 2.3.90-1
- Update to 2.3.90
- Enable full debuginfo on s390x

* Thu Feb 13 2014 Paul Howarth <paul@city-fan.org> - 2.3.5-3
- Rebuild against new libicu

* Fri Feb  7 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.5-2
- Add support for aarch64

* Thu Feb 6 2014 Tomas Popela <tpopela@redhat.com> - 2.3.5-1
- Update to 2.3.5

* Mon Jan 13 2014 Tomas Popela <tpopela@redhat.com> - 2.3.4-1
- Update to 2.3.4
- Add patch that fixes compilation on i686

* Thu Jan 02 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.3-2
- Rebuild for libwebp soname bump

* Thu Dec 19 2013 Tomas Popela <tpopela@redhat.com> - 2.3.3-1
- Update to 2.3.3

* Thu Dec 5 2013 Tomas Popela <tpopela@redhat.com> - 2.3.2-1
- Update to 2.3.2
- Add libatomic as BR on ppc

* Wed Dec 4 2013 Tomas Popela <tpopela@redhat.com> - 2.2.3-1
- Update to 2.2.3

* Thu Nov 28 2013 Tomas Popela <tpopela@redhat.com> - 2.2.2-2
- Fix for RH bug #1035764 - Crashes with certain Google Drive documents

* Mon Nov 11 2013 Tomas Popela <tpopela@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Fri Oct 18 2013 Tomas Popela <tpopela@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Fri Sep 27 2013 Kalev Lember <kalevlember@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.92-1
- Update to 2.1.92

* Thu Sep 12 2013 Dan Horák <dan[at]danny.cz> - 2.1.91-2
- rediff the ppc32 patch, it failed to apply on s390

* Wed Sep 11 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.91-1
- Update to 2.1.91

* Fri Aug 30 2013 Karsten Hopp <karsten@redhat.com> 2.1.90.1-2
- modify ppc32 patch, the macro interpretResolveWithBase got removed

* Fri Aug 30 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.90.1-1
- Update to 2.1.90.1

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.90-1
- Update to 2.1.90
- Add missing at-spi2-core-devel build dep

* Mon Aug 12 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.3-3
- Switch to unversioned docdirs (#993890)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 9 2013 Tomas Popela <tpopela@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Wed Jun 19 2013 Tomas Popela <tpopela@redhat.com> - 2.1.2-1
- Update to 2.1.2

* Fri Jun 07 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.1-3
- Link with harfbuzz-icu (split into separate library in harfbuzz 0.9.18)

* Mon Jun 03 2013 Kalev Lember <kalevlember@gmail.com> - 2.1.1-2
- Remove glib-compile-schemas scriptlets: the schemas are no longer installed
- Add ldconfig calls to the libwebkit2gtk subpackage
- Remove rpath from MiniBrowser
- Re-enable full debuginfo (#861452)

* Mon Jun 3 2013 Tomas Popela <tpopela@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Drop unused patches

* Mon May 13 2013 Tomas Popela <tpopela@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Mon May  6 2013 Matthias Clasen <mclasen@redhat.com> - 2.0.1-2
- Split libwebkit2gtk off into a subpackage to avoid
  pulling this 35M behemoth of a library onto the livecd
  needlessly

* Tue Apr 16 2013 Tomas Popela <tpopela@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Thu Apr 11 2013 Tomas Popela <tpopela@redhat.com> - 2.0.0-3
- Add fix for broken GObject casting

* Wed Apr 3 2013 Tomas Popela <tpopela@redhat.com> - 2.0.0-2
- Apply double2intsPPC32.patch also on s390

* Wed Mar 27 2013 Tomas Popela <tpopela@redhat.com> - 2.0.0-1
- Update to 2.0.0
- Update BR versions
- Drop unused patches

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.92-1
- Update to 1.11.92

* Fri Mar 08 2013 Tomas Popela <tpopela@redhat.com> 1.11.91-1
- Update to 1.11.91
- Fix for RH bug #915990 - Seed segfaults in JSC::LLInt::CLoop::execute()

* Mon Feb 25 2013 Tomas Popela <tpopela@redhat.com> 1.11.90-3
- Fix for not building on ppc32 with JIT disabled

* Sat Feb 23 2013 Kevin Fenzi <kevin@scrye.com> 1.11.90-2
- Add webkit2 MiniBrowser

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.90-1
- Update to 1.11.90

* Fri Feb 22 2013 Tomas Popela <tpopela@redhat.com> 1.11.5-5
- Fix for not building on ppc32 with JIT disabled
- BR libatomic (needs gcc >= 4.8.0) for ppc32

* Mon Feb 18 2013 Tomas Popela <tpopela@redhat.com> 1.11.5-4
- Backported fixes for not building with disabled JIT

* Sat Feb 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.5-3
- Re-enable JIT on ARM (hopefully the gmail crash is fixed)

* Thu Feb 14 2013 Tomas Popela <tpopela@redhat.com> 1.11.5-2
- Add upstream patch for RH bug #908143 - AccessibilityTableRow::parentTable crash

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.5-1
- Update to 1.11.5
- Drop upstreamed patches

* Wed Jan 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.11.4-5
- Rebuild against new icu again

* Sat Jan 26 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.4-4
- Rebuilt for icu 50

* Fri Jan 25 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.4-3
- Backport a fix for a crash in AccessibilityTableCell::parentTable()

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.11.4-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 16 2013 Kalev Lember <kalevlember@gmail.com> - 1.11.4-1
- Update to 1.11.4
- Remove conditional pango deps; the build now uses harfbuzz directly
- BR libwebp-devel
- Drop upstreamed librt linking patch

* Tue Dec 18 2012 Dan Horák <dan[at]danny.cz> - 1.11.2-3
- fix 32-bit non-JIT arches

* Tue Dec 18 2012 Dan Horák <dan[at]danny.cz> - 1.11.2-2
- fix build for non-JIT arches

* Sat Nov 24 2012 Kalev Lember <kalevlember@gmail.com> - 1.11.2-1
- Update to 1.11.2
- Add a patch to explicitly link with librt

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.1-1
- Update to 1.10.1
- Enable the parallel build
- Drop the upstreamed Geode-compatibility patch

* Fri Oct  5 2012 Daniel Drake <dsd@laptop.org> - 1.10.0-2
- Restore compatibility with AMD Geode processors

* Mon Sep 24 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.0-1
- Update to 1.10.0
- Adjust for webkit -> webkitgtk upstream tarball rename

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.92-2
- Build with gstreamer1

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.92-1
- Update to 1.9.92

* Wed Sep 05 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.91-1
- Update to 1.9.91

* Sun Sep  2 2012 Matthias Clasen <mclasen@redhat.com> - 1.9.90-2
- Rebuild

* Wed Aug 29 2012 Daniel Drake <dsd@laptop.org> - 1.9.90-1
- Update to latest release (#850520)

* Thu Aug  9 2012 Daniel Drake <dsd@laptop.org> - 1.9.5-2
- Add upstream patch to fix build without JIT (#843428)
- Add upstream patch to fix build with latest gcc/bison

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.5-1
- Update to 1.9.5
- Build with -g1 to avoid running into 4 GB ar format limit

* Wed Jul 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.9.4-3
- Fix %%post scriptlet dependencies.

* Wed Jul 04 2012 Dan Horák <dan[at]danny.cz> - 1.9.4-2
- apply workaround for s390x until #835957 is resolved (static library archive > 4 GB)

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.4-1
- Update to 1.9.4

* Thu Jun 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.9.3-1
- Update to 1.9.3
- Build webkit2gtk and BR gtk2-devel for its plugin process

* Tue May 15 2012 Karsten Hopp <karsten@redhat.com> 1.8.1-3
- disable JIT on PPC(64) as the autodetection enables it even if not supported

* Mon May 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.1-2
- Explicitly disable JIT on ARM as it's not currently stable with JS heavy pages

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 1.8.1-1
- Update to 1.8.1
- Dropped the backported patches
- Remove lib64 rpaths with chrpath
- Update gsettings rpm scriptlets

* Wed Apr 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.0-3
- Add upstream patch to fix crash when SSE2 isn't present
- Add upstream patch to flickering when some widgets are drawn

* Mon Apr 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.8.0-2
- Finish splitting out a -doc subpackage (#808917)

* Wed Mar 28 2012 Richard Hughes <rhughes@redhat.com> - 1.8.0-1
- Update to 1.8.0.

* Sat Mar 24 2012 Dan Horák <dan[at]danny.cz> - 1.7.92-2
- add ppc to low mem arches
- decrease debuginfo verbosity on s390 to save memory

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 1.7.92-1
- Update to 1.7.92
- Don't pass --enable-geolocation to configure; it's now enabled by default

* Thu Mar 15 2012 Karsten Hopp <karsten@redhat.com> 1.7.91-2
- disable jit on ppc(64)

* Thu Mar  8 2012 Matthias Clasen <mclasen@redhat.com> - 1.7.91-1
- Update to 1.7.91

* Tue Feb 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.5-3
- Add ARM to and optimise compile flags for low mem arches

* Mon Feb 20 2012 Dan Horák <dan[at]danny.cz> - 1.7.5-2
- don't enable jit on s390(x)

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Thu Nov 24 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Mon Nov 7 2011 Matthias Clasen <mclasen@redhat.com> 1.7.1-2
- Rebuild against new libpng

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> 1.7.1-1
- Update to 1.7.1

* Wed Oct 12 2011 Dan Horák <dan[at]danny.cz> 1.6.1-2
- fix build on s390(x)

* Wed Sep 28 2011 Ray Strode <rstrode@redhat.com> 1.6.1-1
- Update to 1.6.1

* Fri Sep 09 2011 Caolán McNamara <caolanm@redhat.com> - 1.5.1-2
- rebuild for icu 4.8.1

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 1.4.0-3
- Rebuild against newer GTK+

* Wed May 11 2011 Cosimo Cecchi <cosimoc@redhat.com> 1.4.0-2
- Add a doc package for gtk-doc documentation

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 1.4.0-1
- Update to 1.4.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 1.3.13-1
- Update to 1.3.13

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 1.3.10-3
- Rebuild against newer gtk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 1.3.11-1
- 1.3.11

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 1.3.10-2
- Rebuild against newer gtk

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 1.3.10-1
- Update to 1.3.10

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> 1.3.9-1
- Update to 1.3.9

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> 1.3.7-2
- Rebuild against new gtk

* Wed Dec  1 2010 Matthias Clasen <mclasen@redhat.com> 1.3.7-1
- Update to 1.3.7

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> 1.3.6-1
- Update to 1.3.6
- Disable the s390 patch again :-( Upstream it, maybe ?

* Thu Nov 11 2010 Dan Horák <dan[at]danny.cz> - 1.3.5-2
- Updated and re-enabled the s390 patch

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> 1.3.5-1
- Update to 1.3.5

* Wed Sep 29 2010 jkeating - 1.3.4-3
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Matthias Clasen <mclasen@redhat.com> 1.3.4-2
- Enable JIT/patch for execmem
- Move inspector to the main package

* Thu Sep 23 2010 Matthias Clasen <mclasen@redhat.com> 1.3.4-1
- Update to 1.3.4

* Wed Aug 25 2010 Dan Horák <dan[at]danny.cz> - 1.3.3-4
- Do not generate debug information to prevent linker memory exhaustion on s390 with its 2 GB address space

* Wed Jul 21 2010 Dan Horák <dan[at]danny.cz> - 1.3.3-3
- Fix build on s390(x)

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 1.3.3-2
- Rebuild with new gobject-introspection

* Fri Jul  9 2010 Matthias Clasen <mclasen@redhat.com> 1.3.2-2
- Fix conflicting gettext domain with webkitgtk
- Drop the -doc subpackage

* Thu Jul  1 2010 Matthias Clasen <mclasen@redhat.com> 1.3.2-1
- Initial packaging

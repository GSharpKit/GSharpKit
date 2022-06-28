%?mingw_package_header

%global mingw_build_win32 0
%global mingw_build_win64 1

%global bin_version 4.0.0

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gtk4
Version:        4.6.5
Release:        1%{?dist}
Summary:        MinGW Windows GTK+ library

License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  mingw64-atk
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-vulkan-loader
BuildRequires:  mingw64-graphene

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk4
# Native one for gdk-pixbuf-csource
BuildRequires:  gdk-pixbuf2-devel
# Native one for /usr/bin/perl
BuildRequires:  perl-interpreter

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw64-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme

%description -n mingw64-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%{?mingw_debug_package}

%prep
%setup -q -n gtk-%{version}

%build
%mingw_meson -Dwin32-backend=true -Dmedia-gstreamer=enabled -Dmedia-ffmpeg=disabled -Dprint-cups=enabled -Dvulkan=enabled -Dgtk_doc=false -Dman-pages=false -Ddemos=true -Dbuild-examples=false -Dbuild-tests=false -Dinstall-tests=false
%mingw_ninja

%install
%mingw_ninja_install
#mingw_make install DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/charset.alias

# Remove manpages which duplicate those in Fedora native.
#rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Remove documentation too.
#rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

# Remove unneeded files
#rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.def

# Remove files used only for tests.
#rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/libgtkreftestprivate-0.dll
#rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libgtkreftestprivate.dll.a

#rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
#rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
#rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.la

# Remove desktop files and corresponding icons as they aren't useful for win32
#rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/applications/*.desktop
#rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/icons/hicolor/*/apps/*.png

%mingw_find_lang %{name} --all-name

%postun -n mingw64-gtk4
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n mingw64-gtk4
/usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :


%files -n mingw64-gtk4 -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gtk4-demo-application.exe
%{mingw64_bindir}/gtk4-demo.exe
%{mingw64_bindir}/gtk4-icon-browser.exe
%{mingw64_bindir}/gtk4-widget-factory.exe
%{mingw64_bindir}/libgtk-4-1.dll
%{mingw64_bindir}/gtk4-builder-tool.exe
%{mingw64_bindir}/gtk4-encode-symbolic-svg.exe
%{mingw64_bindir}/gtk4-print-editor.exe
%{mingw64_bindir}/gtk4-query-settings.exe
%{mingw64_includedir}/gtk-4.0/
%dir %{mingw64_libdir}/gtk-4.0
%dir %{mingw64_libdir}/gtk-4.0/%{bin_version}
%{mingw64_libdir}/gtk-4.0/%{bin_version}/
%{mingw64_libdir}/libgtk-4.dll.a
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/gtk-4.0/
%{mingw64_datadir}/applications/
%{mingw64_datadir}/glib-2.0/schemas/
%{mingw64_datadir}/icons/hicolor/
%{mingw64_datadir}/metainfo/
%{mingw64_libdir}/pkgconfig/gtk4-win32.pc
%{mingw64_libdir}/pkgconfig/gtk4.pc
%{mingw64_bindir}/gtk4-update-icon-cache.exe

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Sandro Mani <manisandro@gmail.com> - 3.24.13-1
- Update to 3.24.13

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.24.12-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 3.24.12-1
- Update to 3.24.12

* Mon Sep 23 2019 Sandro Mani <manisandro@gmail.com> - 3.24.11-1
- Update to 3.24.11

* Thu Aug 29 2019 Sandro Mani <manisandro@gmail.com> - 3.24.10-1
- Update to 3.24.10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 3.22.30-1
- Update to 3.22.30
- Drop ancient obsoletes/conflicts

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 3.22.24-1
- Update to 3.22.24

* Tue Aug 22 2017 Kalev Lember <klember@redhat.com> - 3.22.19-1
- Update to 3.22.19

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 3.22.17-1
- Update to 3.22.17

* Wed Jun 21 2017 Kalev Lember <klember@redhat.com> - 3.22.16-1
- Update to 3.22.16

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 3.22.15-1
- Update to 3.22.15
- BR gtk-update-icon-cache instead of gtk2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2
- Split out gtk-update-icon-cache.exe in a subpackage

* Fri Oct 07 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.20.9-1
- Update to 3.20.9

* Wed Aug 10 2016 Kalev Lember <klember@redhat.com> - 3.20.8-1
- Update to 3.20.8

* Mon May 23 2016 Kalev Lember <klember@redhat.com> - 3.20.6-1
- Update to 3.20.6

* Sun May 22 2016 Kalev Lember <klember@redhat.com> - 3.20.5-1
- Update to 3.20.5
- Regenerate gtk.immodules

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.4-1
- Update to 3.20.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Kalev Lember <klember@redhat.com> - 3.18.6-1
- Update to 3.18.6

* Wed Nov 18 2015 Kalev Lember <klember@redhat.com> - 3.18.5-1
- Update to 3.18.5

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Sun Oct 04 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 3.17.7-1
- Update to 3.17.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Wed Mar 25 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-2
- Regenerate gtk.immodules
- Use license macro for the COPYING file
- Stop using unrecognized --enable-gtk2-dependency configure option
- Depend on mingw{32,64}-adwaita-icon-theme

* Wed Mar 25 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.5-1
- Update to 3.14.5

* Tue Oct 14 2014 David King <amigadave@amigadave.com> - 3.14.3-1
- Update to 3.14.3
- Refactor autoreconf handling

* Tue Sep 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.14.0-1
- Update to 3.14.0

* Sun Sep 21 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.13.9-1
- Update to 3.13.9

* Fri Sep 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.13.8-1
- Update to 3.13.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.13.2-1
- Update to 3.13.2

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0
- Regenerate gtk.immodules

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.11.2-1
- Update to 3.11.2

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.10.4-1
- Update to 3.10.4

* Tue Sep 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.14-1
- Update to 3.9.14

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.8-1
- Update to 3.9.8

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.0-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun May 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.0-2
- Fix the build (GNOME BZ #699690)
- Bumped the BR: mingw{32,64}-filesystem to >= 98 because of
  the updated pkg-config behaviour

* Sun May  5 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Fri Apr  5 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.0-2
- Workaround knownfolders.h linker issue when using a recent mingw-w64 snapshot

* Tue Mar 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.14-1
- Update to 3.7.14

* Sat Jan 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.6-1
- Update to 3.7.6

* Fri Nov  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Fri Oct  5 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Mon Aug 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.5.12-1
- Update to 3.5.12

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.4-1
- Update to 3.4.4
- Apply a build fix backported from git master

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.2-1
- Update to 3.4.2
- Drop an upstreamed patch

* Sat Apr 14 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1
- Added a patch to fix build without unix gio

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.4.0-2
- Fix upgrade path for people upgrading from the mingw-w64 testing repository

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 14 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.16-2
- Build 64 bit Windows binaries

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.16-1
- Update to 3.3.16

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.3.14-2
- Rebuild against the mingw-w64 toolchain

* Wed Feb 08 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.14-1
- Update to 3.3.14
- Removed the .la files

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.4-3
- Rebuilt for libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4

* Tue Oct 18 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Tue Aug 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.16-1
- Update to 3.1.16

* Sat Jul 30 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.8-2
- Added rpm scriplets for running glib-compile-schemas

* Sun Jul 10 2011 Kalev Lember <kalevlember@gmail.com> - 3.1.8-1
- Update to 3.1.8
- Dropped upstreamed patches
- Switched to xz compressed tarball

* Fri Jul 08 2011 Kalev Lember <kalevlember@gmail.com> - 3.0.11-1
- Update to 3.0.11
- Install missing gdk/win32/ headers, patch by Greg Hellings (#718802)

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 3.0.10-2
- Rebuilt against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.10-1
- Update to 3.0.10
- Renamed the base package to mingw-gtk3
- Use the automatic dep extraction available in mingw32-filesystem 68

* Mon May 02 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.9-3
- Backported an upstream patch for linking with libuuid

* Fri Apr 29 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.9-2
- Removed an unneeded PATH override (#700815)

* Fri Apr 29 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.9-1
- Initial RPM release

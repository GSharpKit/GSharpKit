%?mingw_package_header

%global bin_version 3.0.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

# Only enable if using patches that touches configure.ac,
# Makefile.am or other build system related files
%define enable_autoreconf 1

Name:           mingw-gtk3
Version:        3.24.8
Release:        1%{?dist}
Summary:        MinGW Windows GTK+ library

License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/%{release_version}/gtk+-%{version}.tar.xz
# wine /usr/i686-w64-mingw32/sys-root/mingw/bin/gtk-query-immodules-3.0.exe | sed -e 's@Z:/usr/i686-w64-mingw32/sys-root/mingw@..@' -e 's@/usr/i686-w64-mingw32/sys-root/mingw@..@' > gtk.immodules
Source1:        gtk.immodules

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildRequires:  mingw32-fribidi
BuildRequires:  mingw64-fribidi

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache
# Native one for gdk-pixbuf-csource
BuildRequires:  gdk-pixbuf2-devel
# Native one for /usr/bin/perl
BuildRequires:  perl-interpreter

%if 0%{?enable_autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
%endif


%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw32-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw32-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw32-gtk-update-icon-cache

%description -n mingw32-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw32-gtk-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw32-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.


%package -n mingw64-gtk3
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw64-gtk-update-icon-cache

%description -n mingw64-gtk3
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw64-gtk-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw64-gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.


%?mingw_debug_package


%prep
%setup -q -n gtk+-%{version}
%if 0%{?enable_autoreconf}
autoreconf --install --force
%endif


%build
export GLIB_COMPILE_RESOURCES=/usr/bin/glib-compile-resources
%mingw_configure --disable-cups

%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/charset.alias

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Remove documentation too.
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

# Remove unneeded files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.def
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.def

# Remove files used only for tests.
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/libgtkreftestprivate-0.dll
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/libgtkreftestprivate-0.dll
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libgtkreftestprivate.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libgtkreftestprivate.dll.a

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/*.la

# Remove desktop files and corresponding icons as they aren't useful for win32
rm -f $RPM_BUILD_ROOT%{mingw32_datadir}/applications/*.desktop
rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/applications/*.desktop
rm -f $RPM_BUILD_ROOT%{mingw32_datadir}/icons/hicolor/*/apps/*.png
rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/icons/hicolor/*/apps/*.png

# Install the gtk.immodules file
mkdir -p $RPM_BUILD_ROOT%{mingw32_sysconfdir}/gtk-3.0/
mkdir -p $RPM_BUILD_ROOT%{mingw64_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw32_sysconfdir}/gtk-3.0/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw64_sysconfdir}/gtk-3.0/

%mingw_find_lang %{name} --all-name


%postun -n mingw32-gtk3
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n mingw32-gtk3
/usr/bin/glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :

%postun -n mingw64-gtk3
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n mingw64-gtk3
/usr/bin/glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :


%files -n mingw32-gtk3 -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gtk3-demo-application.exe
%{mingw32_bindir}/gtk3-demo.exe
%{mingw32_bindir}/gtk3-icon-browser.exe
%{mingw32_bindir}/gtk3-widget-factory.exe
%{mingw32_bindir}/gtk-builder-tool.exe
%{mingw32_bindir}/gtk-encode-symbolic-svg.exe
%{mingw32_bindir}/gtk-launch.exe
%{mingw32_bindir}/gtk-query-immodules-3.0.exe
%{mingw32_bindir}/gtk-query-settings.exe
%{mingw32_bindir}/libgdk-3-0.dll
%{mingw32_bindir}/libgailutil-3-0.dll
%{mingw32_bindir}/libgtk-3-0.dll
%{mingw32_sysconfdir}/gtk-3.0/
%{mingw32_includedir}/gtk-3.0/
%{mingw32_includedir}/gail-3.0/
%dir %{mingw32_libdir}/gtk-3.0
%dir %{mingw32_libdir}/gtk-3.0/%{bin_version}
%dir %{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-am-et.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-cedilla.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-cyrillic-translit.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ime.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-inuktitut.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ipa.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-multipress.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-thai.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-er.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-et.dll
%{mingw32_libdir}/gtk-3.0/%{bin_version}/immodules/im-viqr.dll
%{mingw32_libdir}/libgailutil-3.dll.a
%{mingw32_libdir}/libgdk-3.dll.a
%{mingw32_libdir}/libgtk-3.dll.a
%{mingw32_libdir}/pkgconfig/gail-3.0.pc
%{mingw32_libdir}/pkgconfig/gdk-3.0.pc
%{mingw32_libdir}/pkgconfig/gdk-win32-3.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-3.0.pc
%{mingw32_libdir}/pkgconfig/gtk+-win32-3.0.pc
%{mingw32_datadir}/aclocal/gtk-3.0.m4
%{mingw32_datadir}/gettext/
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%{mingw32_datadir}/gtk-3.0/
%{mingw32_datadir}/themes/*

%files -n mingw32-gtk-update-icon-cache
%license COPYING
%{mingw32_bindir}/gtk-update-icon-cache.exe

%files -n mingw64-gtk3 -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gtk3-demo-application.exe
%{mingw64_bindir}/gtk3-demo.exe
%{mingw64_bindir}/gtk3-icon-browser.exe
%{mingw64_bindir}/gtk3-widget-factory.exe
%{mingw64_bindir}/gtk-builder-tool.exe
%{mingw64_bindir}/gtk-encode-symbolic-svg.exe
%{mingw64_bindir}/gtk-launch.exe
%{mingw64_bindir}/gtk-query-immodules-3.0.exe
%{mingw64_bindir}/gtk-query-settings.exe
%{mingw64_bindir}/libgdk-3-0.dll
%{mingw64_bindir}/libgailutil-3-0.dll
%{mingw64_bindir}/libgtk-3-0.dll
%{mingw64_sysconfdir}/gtk-3.0/
%{mingw64_includedir}/gtk-3.0/
%{mingw64_includedir}/gail-3.0/
%dir %{mingw64_libdir}/gtk-3.0
%dir %{mingw64_libdir}/gtk-3.0/%{bin_version}
%dir %{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-am-et.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-cedilla.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-cyrillic-translit.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ime.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-inuktitut.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ipa.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-multipress.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-thai.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-er.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-ti-et.dll
%{mingw64_libdir}/gtk-3.0/%{bin_version}/immodules/im-viqr.dll
%{mingw64_libdir}/libgailutil-3.dll.a
%{mingw64_libdir}/libgdk-3.dll.a
%{mingw64_libdir}/libgtk-3.dll.a
%{mingw64_libdir}/pkgconfig/gail-3.0.pc
%{mingw64_libdir}/pkgconfig/gdk-3.0.pc
%{mingw64_libdir}/pkgconfig/gdk-win32-3.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-3.0.pc
%{mingw64_libdir}/pkgconfig/gtk+-win32-3.0.pc
%{mingw64_datadir}/aclocal/gtk-3.0.m4
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.EmojiChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%{mingw64_datadir}/gtk-3.0/
%{mingw64_datadir}/themes/*

%files -n mingw64-gtk-update-icon-cache
%license COPYING
%{mingw64_bindir}/gtk-update-icon-cache.exe


%changelog
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

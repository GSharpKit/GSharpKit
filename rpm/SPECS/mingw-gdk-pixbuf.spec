%?mingw_package_header

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gdk-pixbuf
Version:        2.36.4
Release:        1%{?dist}
Summary:        MinGW Windows GDK Pixbuf library

License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/%{release_version}/gdk-pixbuf-%{version}.tar.xz

# If you want to rebuild this, do:
# wine /usr/i686-w64-mingw32/sys-root/mingw/bin/gdk-pixbuf-query-loaders.exe | sed s@'Z:/usr/i686-w64-mingw32/sys-root/mingw'@'..'@ > gdk-pixbuf.loaders
Source1:        gdk-pixbuf.loaders

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarsjal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk2
# Native one for gdk-pixbuf-csource
BuildRequires:  gtk2-devel

%description
MinGW Windows GDK Pixbuf library.


%package -n mingw32-gdk-pixbuf
Summary:        MinGW Windows GDK Pixbuf library

%description -n mingw32-gdk-pixbuf
MinGW Windows GDK Pixbuf library.


%package -n mingw64-gdk-pixbuf
Summary:        MinGW Windows GDK Pixbuf library

%description -n mingw64-gdk-pixbuf
MinGW Windows GDK Pixbuf library.


%?mingw_debug_package


%prep
%setup -q -n gdk-pixbuf-%{version}


%build
%mingw_configure \
  --enable-relocations \
  --with-included-loaders=gdip-bmp,gdip-emf,gdip-gif,gdip-ico,gdip-jpeg,gdip-tiff,gdip-wmf,png \
  --with-libjasper
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# The .def files are only used while compiling the libraries themselves
# (they contain a list of functions which need to be exported by the linker)
# so they serve no purpose for other libraries and applications
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gdk_pixbuf-2.0.def
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gdk_pixbuf-2.0.def

# The .dll.a files are import libraries, but as the regular .dll's are
# only dlopen'ed by GTK they provide no additional value so they can be dropped
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.dll.a

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# The gtk-doc documentation and man pages can also be dropped as they're
# already provided by the native package
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Install the loaders.cache file
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

%mingw_find_lang %{name} --all-name


%files -n mingw32-gdk-pixbuf -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gdk-pixbuf-csource.exe
%{mingw32_bindir}/gdk-pixbuf-pixdata.exe
%{mingw32_bindir}/gdk-pixbuf-query-loaders.exe
%{mingw32_bindir}/gdk-pixbuf-thumbnailer.exe
%{mingw32_bindir}/libgdk_pixbuf-2.0-0.dll
%dir %{mingw32_libdir}/gdk-pixbuf-2.0
%dir %{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jasper.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.dll
%{mingw32_libdir}/libgdk_pixbuf-2.0.dll.a
%{mingw32_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{mingw32_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
%{mingw32_includedir}/gdk-pixbuf-2.0/

%files -n mingw64-gdk-pixbuf -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gdk-pixbuf-csource.exe
%{mingw64_bindir}/gdk-pixbuf-pixdata.exe
%{mingw64_bindir}/gdk-pixbuf-query-loaders.exe
%{mingw64_bindir}/gdk-pixbuf-thumbnailer.exe
%{mingw64_bindir}/libgdk_pixbuf-2.0-0.dll
%dir %{mingw64_libdir}/gdk-pixbuf-2.0
%dir %{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-ani.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-icns.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jasper.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-pnm.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-qtif.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tga.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xbm.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-xpm.dll
%{mingw64_libdir}/libgdk_pixbuf-2.0.dll.a
%{mingw64_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{mingw64_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
%{mingw64_includedir}/gdk-pixbuf-2.0/


%changelog
* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.36.0-1
- Update to 2.36.0

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.34.0-1
- Update to 2.34.0
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 2.32.3-2
- Use global instead of define.

* Thu Dec 17 2015 Kalev Lember <klember@redhat.com> - 2.32.3-1
- Update to 2.32.3

* Wed Nov 18 2015 Kalev Lember <klember@redhat.com> - 2.32.2-1
- Update to 2.32.2

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 2.32.1-1
- Update to 2.32.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 2.31.6-1
- Update to 2.31.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Kalev Lember <kalevlember@gmail.com> - 2.31.3-1
- Update to 2.31.3
- Use license macro for the COPYING file

* Tue Oct 14 2014 Kalev Lember <kalevlember@gmail.com> - 2.31.1-1
- Update to 2.31.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.30.8-1
- Update to 2.30.8

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 2.30.7-1
- Update to 2.30.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.2-3
- Rebuild against libpng 1.6

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.2-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 2.28.2-1
- Update to 2.28.2

* Tue Mar 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.0-1
- Update to 2.28.0

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.3-1
- Update to 2.27.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.26.4-1
- Update to 2.26.4

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Kalev Lember <kalevlember@gmail.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 2.26.0-1
- Update to 2.26.0

* Wed Mar 14 2012 Kalev Lember <kalevlember@gmail.com> - 2.25.2-5
- Build 64 bit Windows binaries

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.2-4
- Renamed the source package to mingw-gdk-pixbuf (RHBZ #800383)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.2-3
- Rebuild against the mingw-w64 toolchain

* Sun Feb 19 2012 Kalev Lember <kalevlember@gmail.com> - 2.25.2-2
- Include all GDI+ loaders in the main DLL (#795152)
- Also include the PNG loader, for consistency with native gdk-pixbuf2 package

* Wed Feb 08 2012 Kalev Lember <kalevlember@gmail.com> - 2.25.2-1
- Update to 2.25.2
- Dropped upstreamed patches

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.0-1
- Update to 2.25.0
- Rebuild against libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Kalev Lember <kalevlember@gmail.com> - 2.24.0-1
- Update to 2.24.0

* Wed Jul  6 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.5-1
- Update to 2.23.5
- Rebuild against win-iconv

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.3-2
- Rebuild for libjpeg-turbo

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.3-1
- Update to 2.23.3
- Dropped the configure argument --enable-gdiplus as it's enabled by default
- Dropped upstreamed patch
- Dropped the proxy-libintl pieces

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-2
- Rebuild in order to have soft dependency on libintl
- Bump the BR: mingw32-filesystem to >= 61 because of mingw32(gdiplus.dll) provides

* Thu Sep 23 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Mon Sep 20 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.7-2
- Fixed a bug which caused the path /usr/i686-pc-mingw32/sys-root/mingw to get hardcoded
  in the resulting library resulting in runtime failures on Win32 environments
- Moved the file %%{_mingw32_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders to
  %%{_mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.7-1
- Initial release (split off from the mingw32-gtk2 package)
- Dropped the -static subpackage as it provides no added value
- Dropped all the .dll.a and .la files from the loaders as they provide no added value
- Dropped the libpng 1.4 hack as upstream has provided a proper fix


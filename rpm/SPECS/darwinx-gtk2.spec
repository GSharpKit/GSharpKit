Name:           darwinx-gtk2
Version:        2.24.23
Release:        1%{?dist}
Summary:        Darwin Gtk2 library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/3.10/gtk+-%{version}.tar.xz
Patch0:		gtk+-2.24.23-dir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-odcctools
BuildRequires:  darwinx-sdk

BuildRequires:  darwinx-atk >= 2.10.0
BuildRequires:  darwinx-cairo >= 1.12.10
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-glib2 >= 2.38.0
BuildRequires:  darwinx-jasper
BuildRequires:  darwinx-libjpeg-turbo
BuildRequires:  darwinx-libpng >= 1.5.13
BuildRequires:  darwinx-pango >= 1.34.0
BuildRequires:  darwinx-pixman

BuildRequires:  pkgconfig

# These are required for the static library patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       pkgconfig


%description
Darwin Gtk2 library.


%package static
Summary:        Static version of the Darwin Gtk2 library
Requires:       %{name} = %{version}-%{release}

%description static
Static version of the Darwin Gtk2 library.


%prep
%setup -q -n gtk+-%{version}
%patch0 -p1

%build
%{_darwinx_configure} \
    --enable-static \
    --without-x \
    --with-gdktarget=quartz \
    --enable-quartz-relocation \
    --enable-cups \
    --enable-test-print-backend \
    --enable-packagekit=no
%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot} program_transform_name=""

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove documentation too.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

mv $RPM_BUILD_ROOT%{_darwinx_bindir}/gtk-update-icon-cache $RPM_BUILD_ROOT%{_darwinx_bindir}/gtk-update-icon-cache-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_darwinx_bindir}/gtk-query-immodules-2.0
%{_darwinx_bindir}/gtk-update-icon-cache-2.0
%{_darwinx_bindir}/gtk-builder-convert
%{_darwinx_sysconfdir}/gtk-2.0/
%{_darwinx_includedir}/gail-1.0/
%{_darwinx_includedir}/gtk-2.0/
%{_darwinx_includedir}/gtk-unix-print-2.0/
%{_darwinx_libdir}/gtk-2.0/include/gdkconfig.h
%dir %{_darwinx_libdir}/gtk-2.0/
%dir %{_darwinx_libdir}/gtk-2.0/2.10.0
%dir %{_darwinx_libdir}/gtk-2.0/2.10.0/immodules
%dir %{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-thai.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-thai.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-quartz.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-quartz.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-cups.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-cups.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-file.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-file.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-lpr.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-lpr.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-test.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-test.so
%{_darwinx_libdir}/gtk-2.0/2.10.0/engines/libpixmap.la
%{_darwinx_libdir}/gtk-2.0/2.10.0/engines/libpixmap.so
%{_darwinx_libdir}/gtk-2.0/modules/libferret.la
%{_darwinx_libdir}/gtk-2.0/modules/libferret.so
%{_darwinx_libdir}/gtk-2.0/modules/libgail.la
%{_darwinx_libdir}/gtk-2.0/modules/libgail.so
%{_darwinx_libdir}/libgailutil.18.dylib
%{_darwinx_libdir}/libgailutil.dylib
%{_darwinx_libdir}/libgailutil.la
%{_darwinx_libdir}/libgdk-quartz-2.0.0.dylib
%{_darwinx_libdir}/libgdk-quartz-2.0.dylib
%{_darwinx_libdir}/libgdk-quartz-2.0.la
%{_darwinx_libdir}/libgtk-quartz-2.0.0.dylib
%{_darwinx_libdir}/libgtk-quartz-2.0.dylib
%{_darwinx_libdir}/libgtk-quartz-2.0.la
%{_darwinx_libdir}/pkgconfig/gail.pc
%{_darwinx_libdir}/pkgconfig/gdk-2.0.pc
%{_darwinx_libdir}/pkgconfig/gdk-quartz-2.0.pc
%{_darwinx_libdir}/pkgconfig/gtk+-2.0.pc
%{_darwinx_libdir}/pkgconfig/gtk+-quartz-2.0.pc
%{_darwinx_libdir}/pkgconfig/gtk+-unix-print-2.0.pc
%{_darwinx_datadir}/aclocal/gtk-2.0.m4
%{_darwinx_datadir}/themes/
%{_darwinx_datadir}/locale/

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-am-et.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cedilla.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-cyrillic-translit.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-inuktitut.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ipa.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-multipress.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-thai.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-er.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-ti-et.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-viqr.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/immodules/im-quartz.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-cups.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-file.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-lpr.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/printbackends/libprintbackend-test.a
%{_darwinx_libdir}/gtk-2.0/2.10.0/engines/libpixmap.a
%{_darwinx_libdir}/gtk-2.0/modules/libferret.a
%{_darwinx_libdir}/gtk-2.0/modules/libgail.a
%{_darwinx_libdir}/libgailutil.a
%{_darwinx_libdir}/libgdk-quartz-2.0.a
%{_darwinx_libdir}/libgtk-quartz-2.0.a


%changelog
* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.12-4.macos_fixes
- Rebuild for PPC fix in GLib

* Sat Mar 20 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.12-3.macos_fixes
- Rebuild for GLib changes
- Build without x86_64 support as pango doesn't support it yet

* Sat Jan 30 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.12-2.macos_fixes
- Rebuild for x86_64 support

* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.12-1.macos_fixes
- Update to version 2.17.12 of the macos-fixes fork: http://git.dronelabs.com/gtk+/?h=macos-fixes

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0
- Drop several upstreamed patches

* Sat Aug 29 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.9-1
- Update to 2.17.9
- Backported some upstream patches to fix clipping and redrawing issues

* Tue Aug 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.8-1
- Update to 2.17.8
- Drop upstreamed patch

* Sat Jul 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.3-1
- Update to 2.17.3
- Rebuild for universal binary support

* Sun Jun 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.17.1-1
- Update to 2.17.1

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.16.1-3
- Use macros instead of static paths

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.16.1-2
- Ported the mingw package to darwin

* Sat Apr 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.16.1-1
- Update to 2.16.1

* Fri Mar 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.5-2
- Force build against latest mingw32-filesystem.

* Sun Mar 8 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.15.5-1
- Update to 2.15.5
- Disable gdiplus support for now because of GNOME BZ#552678
- Use the ./configure flag --without-libtiff until mingw32-libtiff is packaged
- Fixed the %%defattr line
- Dropped the .def files as they aren't used anymore after compilation
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-3
- Remove documentation.
- Add license file.
- Added extra BRs suggested by auto-buildrequires.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-2
- Requires pkgconfig.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-1
- Rebase to Fedora native version 2.15.0.
- Disable static libraries.
- Use _smp_mflags.
- Use find_lang macro.

* Mon Oct 27 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.4-3
- Remove preun script, no longer used.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.4-1
- New upstream version 2.14.4.
- Require cairo >= 1.8.0 because of important fixes.
- Remove a couple of patches which are now upstream.

* Fri Oct 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-3
- Remove the requirement for Wine at build or install time.
- Conflicts with (native) cups-devel.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.2-1
- Update to 2.14.2 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-5
- Remove manpages duplicating those in Fedora native packages.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.0-4
- Added dep on pkgconfig, gettext and glib2 (native)

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-3
- post/preun scripts to update the gdk-pixbuf.loaders list.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-2
- Jasper DLLs now fixed.
- Fix source URL.
- Run the correct glib-mkenums.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.14.0-1
- Initial RPM release

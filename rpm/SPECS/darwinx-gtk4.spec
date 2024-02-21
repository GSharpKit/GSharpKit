Name:           darwinx-gtk4
Version:        4.12.5
Release:        1%{?dist}
Summary:        Darwin Gtk3 library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gtk+/4.12/gtk-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 109
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-odcctools
BuildRequires:  darwinx-sdk

BuildRequires:  darwinx-atk >= 2.20.0
BuildRequires:  darwinx-cairo >= 1.14.0
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-glib2 >= 2.48.0
BuildRequires:  darwinx-jasper
BuildRequires:  darwinx-libjpeg-turbo
BuildRequires:  darwinx-libpng >= 1.6.0
BuildRequires:  darwinx-pango >= 1.40.0
BuildRequires:  darwinx-pixman
BuildRequires:  darwinx-libepoxy >= 1.3
BuildRequires:  darwinx-graphene
BuildRequires:  darwinx-gstreamer1

BuildRequires:  pkgconfig

# These are required for the static library patch
BuildRequires:  libtool

Requires:       pkgconfig

Requires:  	darwinx-filesystem >= 18

%description
Darwin Gtk3 library.

%prep
%setup -q -n gtk-%{version}

%build
%darwinx_meson \
	-Dmacos-backend=true \
	-Dx11-backend=false \
	-Dwayland-backend=false \
	-Dbroadway-backend=false \
	-Dwin32-backend=false \
	-Ddocumentation=false \
	-Dman-pages=false \
	-Dintrospection=disabled \
	-Dbuild-demos=true \
	-Dbuild-examples=true \
	-Dbuild-tests=false \
	-Dbuild-testsuite=false

%darwinx_meson_build

%install
%darwinx_meson_install

# Remove manpages which duplicate those in Fedora native.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove documentation too.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel,-)
%{_darwinx_bindir}/gtk4-demo
%{_darwinx_bindir}/gtk4-demo-application
%{_darwinx_bindir}/gtk4-widget-factory
%{_darwinx_bindir}/gtk4-launch
%{_darwinx_bindir}/gtk4-icon-browser
%{_darwinx_bindir}/gtk4-encode-symbolic-svg
%{_darwinx_bindir}/gtk4-builder-tool
%{_darwinx_bindir}/gtk4-update-icon-cache
%{_darwinx_bindir}/gtk4-node-editor
%{_darwinx_bindir}/gtk4-print-editor
%{_darwinx_bindir}/gtk4-query-settings
%{_darwinx_bindir}/gtk4-rendernode-tool
%{_darwinx_includedir}/gtk-4.0/
%dir %{_darwinx_libdir}/gtk-4.0/
%dir %{_darwinx_libdir}/gtk-4.0/4.0.0
%dir %{_darwinx_libdir}/gtk-4.0/4.0.0/printbackends
%{_darwinx_libdir}/gtk-4.0/4.0.0/printbackends/libprintbackend-cups.so
%{_darwinx_libdir}/gtk-4.0/4.0.0/printbackends/libprintbackend-file.so
%dir %{_darwinx_libdir}/gtk-4.0/4.0.0/media
%{_darwinx_libdir}/gtk-4.0/4.0.0/media/libmedia-gstreamer.so
%{_darwinx_libdir}/libgtk-4.*.dylib
%{_darwinx_libdir}/libgtk-4.dylib
%{_darwinx_libdir}/pkgconfig/gtk4.pc
%{_darwinx_libdir}/pkgconfig/gtk4-macos.pc
%{_darwinx_libdir}/pkgconfig/gtk4-unix-print.pc
%{_darwinx_datadir}/gettext/
%{_darwinx_datadir}/glib-2.0/schemas
%{_darwinx_datadir}/gtk-4.0/
%{_darwinx_datadir}/metainfo/
%{_darwinx_datadir}/locale/
%{_darwinx_datadir}/applications/
%{_darwinx_datadir}/icons/


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

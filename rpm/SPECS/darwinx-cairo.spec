Name:           darwinx-cairo
Version:        1.18.4
Release:        1%{?dist}
Summary:        Darwin Cairo library

License:        LGPLv2 or MPLv1.1
URL:            http://cairographics.org
Source0:        http://cairographics.org/releases/cairo-%{version}.tar.xz
Group:          Development/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-odcctools
BuildRequires:  darwinx-zlib
BuildRequires:  darwinx-freetype
BuildRequires:  darwinx-fontconfig
BuildRequires:  darwinx-libpng
BuildRequires:  pkgconfig

Requires:       pkgconfig
Requires:  	darwinx-freetype
Requires:  	darwinx-fontconfig
Requires:  	darwinx-libpng
Requires:  	darwinx-glib2

%description
Darwin Cairo library.


%prep
%setup -q -n cairo-%{version}

%build
%darwinx_meson \
	-Dquartz=enabled \
	-Dxcb=disabled \
	-Dxlib=disabled \
	-Dsymbol-lookup=disabled \
	-Dspectre=disabled \
	-Dtests=disabled \
	-Dfreetype=enabled \
	-Dlzo=disabled \
	-Dgtk_doc=false

%darwinx_meson_build

%install
%darwinx_meson_install

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/charset.alias
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel,-)
%doc COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_darwinx_bindir}/cairo-trace
%{_darwinx_includedir}/cairo/
%{_darwinx_libdir}/libcairo.2.dylib
%{_darwinx_libdir}/libcairo.dylib
%{_darwinx_libdir}/cairo/libcairo-trace.dylib
%{_darwinx_libdir}/cairo/libcairo-fdr.dylib
%{_darwinx_libdir}/libcairo-gobject.2.dylib
%{_darwinx_libdir}/libcairo-gobject.dylib
%{_darwinx_libdir}/libcairo-script-interpreter.2.dylib
%{_darwinx_libdir}/libcairo-script-interpreter.dylib
%{_darwinx_libdir}/pkgconfig/cairo-ft.pc
%{_darwinx_libdir}/pkgconfig/cairo-gobject.pc
%{_darwinx_libdir}/pkgconfig/cairo-script.pc
%{_darwinx_libdir}/pkgconfig/cairo-pdf.pc
%{_darwinx_libdir}/pkgconfig/cairo-png.pc
%{_darwinx_libdir}/pkgconfig/cairo-ps.pc
%{_darwinx_libdir}/pkgconfig/cairo-quartz-font.pc
%{_darwinx_libdir}/pkgconfig/cairo-quartz-image.pc
%{_darwinx_libdir}/pkgconfig/cairo-quartz.pc
%{_darwinx_libdir}/pkgconfig/cairo-svg.pc
%{_darwinx_libdir}/pkgconfig/cairo.pc
%{_darwinx_libdir}/pkgconfig/cairo-fc.pc
%{_darwinx_libdir}/pkgconfig/cairo-tee.pc
%{_darwinx_libdir}/pkgconfig/cairo-script-interpreter.pc


%changelog
* Thu Jul  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.8-3
- Rebuild for universal binary support

* Sun Jun 21 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.8-2
- Added a workaround for Freedesktop bug #19655

* Sat Jun 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.8-1
- Update to 1.8.8

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.6-4
- Use macros instead of static paths

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.6-3
- Ported the mingw package to darwin

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

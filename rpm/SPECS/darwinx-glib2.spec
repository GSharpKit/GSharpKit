Name:           darwinx-glib2
Version:        2.58.3
Release:        2%{?dist}
Summary:        Darwin GLib2 library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/glib/2.50/glib-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Summary:        Cross compiled GLib2 library

Patch0:		glib-2.48.2-disable-assert.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=675516
Patch1:         0001-Don-t-start-a-DBus-server-when-built-as-static-lib.patch

Patch2:		remove-gcocoanotificationbackend.patch

Patch11:        glib-fix-compilation-on-osx.patch
Patch12:	glib-2.34.1-isreg.patch

Patch13:	glib-2.50.3-appkit.patch

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 109
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-odcctools
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-libffi
BuildRequires:  darwinx-pcre

BuildRequires:  pkgconfig
# Native version required for msgfmt use in build

# These are required for the glib-i386-atomic patch.
BuildRequires:  autoconf, automake, libtool

Provides:	import

%description
Darwin Glib2 library

%package static
Summary:        Static version of the Darwin GLib2 library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the Darwin GLib2 library.

%prep
%setup -q -n glib-%{version}
#patch0 -p1
%patch1 -p1
#patch2 -p1
%patch11 -p1
%patch12 -p1
#patch13 -p1

%build
NOCONFIGURE=1 sh autogen.sh

# GLib can't build static and shared libraries in one go, so we
# build GLib twice here
mkdir build_static
pushd build_static
        %{_darwinx_configure} --disable-shared --enable-static --disable-fam
        V=99 make %{?_smp_mflags}
popd

mkdir build_shared
pushd build_shared
        %{_darwinx_configure} --disable-static --disable-fam
        V=99 make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT

# First install all the files belonging to the shared build
make -C build_shared DESTDIR=$RPM_BUILD_ROOT install

# Install all the files from the static build in a seperate folder
# and move the static libraries to the right location
make -C build_static DESTDIR=$RPM_BUILD_ROOT/build_static install
mv $RPM_BUILD_ROOT/build_static%{_darwinx_libdir}/*.a $RPM_BUILD_ROOT%{_darwinx_libdir}

# Manually merge the libtool files
sed -i '' -e s/"old_library=''"/"old_library='libgio-2.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libgio-2.0.la
sed -i '' -e s/"old_library=''"/"old_library='libglib-2.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libglib-2.0.la
sed -i '' -e s/"old_library=''"/"old_library='libgobject-2.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libgobject-2.0.la
sed -i '' -e s/"old_library=''"/"old_library='libgmodule-2.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libgmodule-2.0.la
sed -i '' -e s/"old_library=''"/"old_library='libgthread-2.0.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libgthread-2.0.la

# Drop the folder which was temporary used for installing the static bits
rm -rf $RPM_BUILD_ROOT/build_static

# First install all the files belonging to the shared build
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/charset.alias

# Remove the gtk-doc documentation and manpages which duplicate Fedora native
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/man
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

# Drop some GDB files which aren't interesting for us
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gdb

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_darwinx_bindir}/gio
%{_darwinx_bindir}/gio-querymodules
%{_darwinx_bindir}/glib-genmarshal
%{_darwinx_bindir}/glib-gettextize
%{_darwinx_bindir}/glib-mkenums
%{_darwinx_bindir}/gobject-query
%{_darwinx_bindir}/gtester
%{_darwinx_bindir}/gtester-report
%{_darwinx_bindir}/gdbus
%{_darwinx_bindir}/gdbus-codegen
%{_darwinx_bindir}/glib-compile-resources
%{_darwinx_bindir}/glib-compile-schemas
%{_darwinx_bindir}/gresource
%{_darwinx_bindir}/gsettings
%{_darwinx_bindir}/gio-launch-desktop
%{_darwinx_includedir}/gio-unix-2.0/
%{_darwinx_includedir}/glib-2.0/
%{_darwinx_libdir}/glib-2.0/
#%{_darwinx_libdir}/gdbus-2.0/
%{_darwinx_libdir}/libgio-2.0.0.dylib
%{_darwinx_libdir}/libgio-2.0.dylib
%{_darwinx_libdir}/libgio-2.0.la
%{_darwinx_libdir}/libglib-2.0.0.dylib
%{_darwinx_libdir}/libglib-2.0.dylib
%{_darwinx_libdir}/libglib-2.0.la
%{_darwinx_libdir}/libgmodule-2.0.0.dylib
%{_darwinx_libdir}/libgmodule-2.0.dylib
%{_darwinx_libdir}/libgmodule-2.0.la
%{_darwinx_libdir}/libgobject-2.0.0.dylib
%{_darwinx_libdir}/libgobject-2.0.dylib
%{_darwinx_libdir}/libgobject-2.0.la
%{_darwinx_libdir}/libgthread-2.0.0.dylib
%{_darwinx_libdir}/libgthread-2.0.dylib
%{_darwinx_libdir}/libgthread-2.0.la
%{_darwinx_libdir}/pkgconfig/gio-2.0.pc
%{_darwinx_libdir}/pkgconfig/gio-unix-2.0.pc
%{_darwinx_libdir}/pkgconfig/glib-2.0.pc
%{_darwinx_libdir}/pkgconfig/gmodule-2.0.pc
%{_darwinx_libdir}/pkgconfig/gmodule-export-2.0.pc
%{_darwinx_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{_darwinx_libdir}/pkgconfig/gobject-2.0.pc
%{_darwinx_libdir}/pkgconfig/gthread-2.0.pc
%{_darwinx_datadir}/aclocal/glib-2.0.m4
%{_darwinx_datadir}/aclocal/glib-gettext.m4
%{_darwinx_datadir}/aclocal/gsettings.m4
%{_darwinx_datadir}/glib-2.0/
%{_darwinx_datadir}/locale/
%{_darwinx_datadir}/bash-completion/completions/gdbus
%{_darwinx_datadir}/bash-completion/completions/gresource
%{_darwinx_datadir}/bash-completion/completions/gsettings
%{_darwinx_datadir}/bash-completion/completions/gapplication
%{_darwinx_datadir}/bash-completion/completions/gio
%{_darwinx_datadir}/gettext/its/gschema.its
%{_darwinx_datadir}/gettext/its/gschema.loc

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libgio-2.0.a
%{_darwinx_libdir}/libgio-2.0.la
%{_darwinx_libdir}/libglib-2.0.a
%{_darwinx_libdir}/libgmodule-2.0.a
%{_darwinx_libdir}/libgobject-2.0.a
%{_darwinx_libdir}/libgthread-2.0.a


%changelog
* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.1-1
- Update to 2.24.1
- Fixed a byte-ordering issue on PPC environments which was introduced in the previous release

* Sat Mar 20 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.5-1
- Update to 2.23.5
- Disabled the 'growing stack pointer' option as it needs to be set to 'no' on OSX
- Patch the autogenerated config.h and glibconfig.h files instead of replacing them

* Sat Feb  6 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.2-2
- Rebuild for stabs debug symbols

* Fri Jan 29 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.2-1
- Update to 2.23.2
- Dropped upstreamed patches

* Thu Jan 28 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.2-3
- Rebuild for x86_64 support

* Thu Jan 21 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.2-2
- Fixed the version mentioned in the patches

* Sun Oct 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.2-1
- Update to 2.22.2
- Added two patches from the native GLib2 package to fix MIME-detection issues

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Sun Sep  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.6-1
- Update to 2.21.6

* Fri Jul 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.3-1
- Update to 2.21.3
- Rebuild for universal binary support

* Thu Jun 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.1-2
- Add BR: darwinx-fam because of GNOME BZ #543148

* Sun Jun 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.1-1
- Update to 2.21.1

* Fri Jun 12 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-5
- Use macros instead of static paths

* Tue Jun  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-4
- Prepare support for universal binaries

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-3
- Prefix all the binaries with 'i686-apple-darwin9' to avoid conflicts
  with native binaries

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.20.1-2
- Ported the mingw32 package to darwin

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.20.1-1
- Update to 2.20.1

* Thu Mar 5 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.19.10-1
- Update to 2.19.10
- Dropped the gtk-doc documentation as it's identical to the base glib2 package

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 2.19.5-4
- Added -static subpackage
- Developers using the static build of GLib need to add
  -DGLIB_STATIC_COMPILATION and -DGOBJECT_STATIC_COMPILATION to
  their CFLAGS to avoid compile failures
- Fixed the %%defattr line
- Rebuild for mingw32-gcc 4.4 (RWMJ)

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.5-3
- Requires pkgconfig.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.5-2
- Rebase to native Fedora version 2.19.5.
- Use _smp_mflags.
- Use find_lang.
- Don't build static libraries.
- +BR dlfcn.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.1-1
- Update to 2.18.1 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-3
- Remove manpages which duplicate Fedora native.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.0-2
- Add BR on pkgconfig, gettext and glib2 (native)

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.0-1
- Initial RPM release

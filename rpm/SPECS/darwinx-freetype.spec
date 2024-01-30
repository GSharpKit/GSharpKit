Name:           darwinx-freetype
Version:        2.13.2
Release:        1%{?dist}
Summary:        Darwin A free and portable font rendering engine

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.freetype.org
Source0:        http://sourceforge.net/projects/freetype/files/freetype2/2.12.1/freetype-%{version}.tar.xz
Source1:	freetype2.pc
Patch0:		freetype-2.5.0-freetype-config.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 4
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-odcctools

BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-libpng
BuildRequires:  pkgconfig

Requires:  	darwinx-glib2


%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%prep
%setup -q -n freetype-%{version}
#patch0 -p1

%build
%{_darwinx_configure} \
	--disable-static		\
	--with-old-mac-font	\
	--with-fsspec		\
	--with-fsref		\
	--with-quickdraw-toolbox \
	--with-quickdraw-carbon \
	--with-ats

%install
rm -rf $RPM_BUILD_ROOT

# First install all the files belonging to the shared build
make DESTDIR=$RPM_BUILD_ROOT install

cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_darwinx_prefix}/lib/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel,-)
%doc README ChangeLog
#{_darwinx_bindir}/freetype-config
%{_darwinx_includedir}/freetype2
%{_darwinx_libdir}/libfreetype.6.dylib
%{_darwinx_libdir}/libfreetype.dylib
%{_darwinx_libdir}/pkgconfig/freetype2.pc
%{_darwinx_datadir}/aclocal/freetype2.m4
#{_darwinx_mandir}/man1/freetype-config.1
 

%changelog
* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-5
- Rebuild for PPC fix in GLib

* Sat Mar 20 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-4
- Rebuild for GLib changes
- Don't build with x86_64 support because some API isn't available on OSX x86_64

* Sat Feb  6 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-3
- Rebuild for x86_64 support
- Rebuild for stabs debug symbols

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-2
- Revert GIT commit 01783de926a as it introduced unwanted side-effects

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Sun Sep  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25.5-1
- Update to 1.25.5

* Fri Jul 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.24.2-2
- Rebuild for universal binary support

* Sun Jun 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.24.2-1
- Update to 1.24.2

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-4
- Use macros instead of static paths

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-3
- Ported the mingw package to darwin

* Thu Apr  2 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.23.0-2
- This package cannot be compiled both static and shared in one go, so
  perform the build twice

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.23.0-1
- Remove man page which duplicates what is in base Fedora.
- Rebase to 1.23.0 to match Fedora.
- +BR mingw32-dlfcn.

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 1.22.1-6
- Added -static subpackage

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-5
- Rebuild for mingw32-gcc 4.4

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-4
- Requires pkgconfig.

* Tue Jan 27 2009 Levente Farkas <lfarkas@lfarkas.org> - 1.22.1-3
- Include license file in documentation section.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-2
- Disable static libraries.
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.22.1-1
- New upstream version 1.22.1.
- BR cairo >= 1.8.0 because of important fixes.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-6
- Rename mingw -> mingw32.

* Tue Sep 23 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-5
- Remove use of wine in %-post.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-4
- Add dep on pkgconfig

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-3
- post/preun scripts to update the pango.modules list.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.21.6-2
- Run the correct glib-mkenums.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.21.6-1
- Initial RPM release

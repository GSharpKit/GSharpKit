Name:		darwinx-libsoup
Version:	2.74.3
Release:	1%{?dist}
Summary:	Darwin for HTTP and XML-RPC functionality

License:	LGPLv2
Group:		Development/Libraries
URL:		http://live.gnome.org/LibSoup
Source0:	http://download.gnome.org/sources/libsoup/2.74/libsoup-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	darwinx-filesystem-base >= 102
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gnutls
BuildRequires:	darwinx-glib-networking
BuildRequires:	darwinx-sqlite
BuildRequires:	darwinx-libpsl

Requires:	pkgconfig

Requires:	darwinx-filesystem >= 102

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.
 
libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the Darwin build of Libsoup


%prep
%setup -q -n libsoup-%{version}

%build
%darwinx_meson \
	-Dgtk_doc=false \
	-Dgnome=true \
	-Dgssapi=disabled \
	-Dintrospection=disabled \
	-Dtests=false \
	-Dtls_check=false \
	-Dvapi=disabled \
	-Dbrotli=disabled \
	-Dntlm=disabled \
	-Dsysprof=disabled

%darwinx_meson_build

%install
%darwinx_meson_install

# Strip all the GTK-Doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,wheel,-)
%{_darwinx_includedir}/libsoup-2.4/
%{_darwinx_includedir}/libsoup-gnome-2.4/
%{_darwinx_libdir}/libsoup-2.4.1.dylib
%{_darwinx_libdir}/libsoup-gnome-2.4.1.dylib
%{_darwinx_libdir}/libsoup-2.4.dylib
%{_darwinx_libdir}/libsoup-gnome-2.4.dylib
%{_darwinx_libdir}/pkgconfig/libsoup-2.4.pc
%{_darwinx_libdir}/pkgconfig/libsoup-gnome-2.4.pc
%{_darwinx_datadir}/locale

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.42.2-1
- Updated to 2.42.1

* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.30.1-1
- Update to 2.30.1
- Rebuild for PPC bug in GLib

* Sat Feb  6 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.29.6-2
- Rebuild for stabs debug symbols

* Sat Jan 30 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.29.6-1
- Update to 2.29.6
- Rebuild for x86_64 support

* Sun Oct 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.1-1
- Update to 2.28.1

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.0-1
- Update to 2.28.0

* Sun Sep  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.91-1
- Update to 2.27.91

* Sat Jul 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.2-1
- Rebuild for universal binary support

* Fri Jun 19 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.2-1
- Update to 2.27.2

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-4
- Use macros instead of static paths

* Sun Jun  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-3
- Ported mingw package to darwin

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-2
- Fixed license typo
- Use %%global instead of %%define
- Fixed mixed-use-of-spaces-and-tabs rpmlint warning

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.1-1
- Update to 2.26.1

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-2
- Added -static subpackage

* Fri Mar 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0

* Sat Feb 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.5-1
- Initial release


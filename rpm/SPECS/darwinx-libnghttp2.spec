Name:		darwinx-libnghttp2
Version:	1.55.1
Release:	1%{?dist}
Summary:	nghttp2 is an implementation of HTTP/2

License:	LGPLv2
Group:		Development/Libraries
URL:		https://nghttp2.org/
Source0:	nghttp2-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	darwinx-filesystem-base >= 102
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gnutls
BuildRequires:	darwinx-glib-networking
BuildRequires:	darwinx-sqlite
BuildRequires:	darwinx-libpsl
BuildRequires:	darwinx-zlib

Requires:	pkgconfig

Requires:	darwinx-filesystem >= 102

%description
nghttp2 is an implementation of HTTP/2

%prep
%setup -q -n nghttp2-%{version}

%build
%darwinx_cmake
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Strip all the GTK-Doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,wheel,-)
%dir %{_darwinx_includedir}/nghttp2/
%{_darwinx_includedir}/nghttp2/*.h
%{_darwinx_libdir}/libnghttp2.*.dylib
%{_darwinx_libdir}/libnghttp2.dylib
%{_darwinx_libdir}/pkgconfig/*.pc

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


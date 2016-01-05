Name:		darwinx-libsoup
Version:	2.52.2
Release:	1%{?dist}
Summary:	Darwin for HTTP and XML-RPC functionality

License:	LGPLv2
Group:		Development/Libraries
URL:		http://live.gnome.org/LibSoup
Source0:	http://download.gnome.org/sources/libsoup/2.52/libsoup-%{version}.tar.xz
Patch0:		libsoup-2.44.2-literal.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gnutls
BuildRequires:	darwinx-glib-networking
#BuildRequires:	darwinx-sqlite3

Requires:	pkgconfig

Requires:	darwinx-filesystem >= 18

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


%package static
Summary:	Static version of the Darin Libsoup library
Requires:	%{name} = %{version}-%{release}
Group:		Development/Libraries

%description static
Static version of the Darwin Libsoup library.


%prep
%setup -q -n libsoup-%{version}
#%patch0 -p1

#ln -s /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk/usr/lib/system/libdnsinfo.dylib /usr/lib/system/libdnsinfo.dylib

%build
# Libsoup can't build static and shared libraries in one go, so we build the package twice here
mkdir build_static
pushd build_static
	%{_darwinx_configure} \
		--without-apache-httpd			\
		--enable-static				\
		--disable-shared			\
		--without-gnome				\
		--enable-vala=no			\
		CFLAGS="$CFLAGS -DGLIB_STATIC_COMPILATION -DGOBJECT_STATIC_COMPILATION -DLIBXML_STATIC"
	make %{?_smp_mflags} V=99
popd

mkdir build_shared
pushd build_shared
	%{_darwinx_configure} \
		--without-apache-httpd			\
		--disable-static			\
		--enable-shared				\
		--without-gnome				\
		--enable-vala=no
	make %{?_smp_mflags} V=99
popd


%install
rm -rf $RPM_BUILD_ROOT

# First install all the files belonging to the shared build
make -C build_shared DESTDIR=$RPM_BUILD_ROOT install

# Install all the files from the static build in a seperate folder
# and move the static libraries to the right location
make -C build_static DESTDIR=$RPM_BUILD_ROOT/build_static install
mv $RPM_BUILD_ROOT/build_static%{_darwinx_libdir}/*.a $RPM_BUILD_ROOT%{_darwinx_libdir}/

# Manually merge the libtool files
sed -i '' s/"old_library=''"/"old_library='libsoup-2.4.a'"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libsoup-2.4.la

# Drop the folder which was temporary used for installing the static bits
rm -rf $RPM_BUILD_ROOT/build_static

# Strip all the GTK-Doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

# Move locale
mkdir $RPM_BUILD_ROOT%{_darwinx_datadir}
mv $RPM_BUILD_ROOT%{_darwinx_libdir}/locale $RPM_BUILD_ROOT%{_darwinx_datadir}/

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%{_darwinx_includedir}/libsoup-2.4/
%{_darwinx_libdir}/libsoup-2.4.1.dylib
%{_darwinx_libdir}/libsoup-2.4.dylib
%{_darwinx_libdir}/libsoup-2.4.la
%{_darwinx_libdir}/pkgconfig/libsoup-2.4.pc
%{_darwinx_datadir}/locale

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libsoup-2.4.a


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


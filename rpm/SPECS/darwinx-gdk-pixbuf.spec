Name:           darwinx-gdk-pixbuf
Version:        2.42.6
Release:        1%{?dist}
Summary:        Cross compiled GDK Pixbuf library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/2.40/gdk-pixbuf-%{version}.tar.xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 109
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-gcc

BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-jasper
BuildRequires:  darwinx-libjpeg-turbo
BuildRequires:  darwinx-libpng
BuildRequires:  darwinx-libtiff

BuildRequires:  pkgconfig

Requires:       darwinx-filesystem >= 109
Requires:  	darwinx-glib2
Requires:  	darwinx-jasper
Requires:  	darwinx-libjpeg-turbo
Requires:  	darwinx-libpng
Requires:  	darwinx-libtiff


%description
Cross compiled GDK Pixbuf library.

%package static
Summary:        Static version of the cross compiled %{name} library
Requires:       %{name} = %{version}-%{release}

%description static
Static version of the cross compiled %{name} library.


%prep
%setup -q -n gdk-pixbuf-%{version}

%build
%darwinx_meson \
    --default-library=both \
    -Ddocs=false \
    -Dman=false \
    -Dinstalled_tests=false \
    -Dgio_sniffing=false \
    -Dbuiltin_loaders=all \
    -Dnative_windows_loaders=false

%darwinx_meson_build

%install
%darwinx_meson_install

# The same also applies to the .la files for the individual loaders
rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.la

# The gtk-doc documentation and man pages can also be dropped as they're
# already provided by the native package
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Prevent other packages from using the cross-compiled version of gdk-pixbuf-csource
rm -f $RPM_BUILD_ROOT%{_darwinx_bindir}/gdk-pixbuf-csource


%clean
rm -rf $RPM_BUILD_ROOT

# Darwinx
%files
%defattr(-,root,root,-)
%{_darwinx_bindir}/gdk-pixbuf-pixdata
%{_darwinx_bindir}/gdk-pixbuf-query-loaders
%{_darwinx_bindir}/gdk-pixbuf-thumbnailer
%{_darwinx_libdir}/libgdk_pixbuf-2.0.0.dylib
%{_darwinx_libdir}/libgdk_pixbuf-2.0.dylib
%{_darwinx_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_darwinx_includedir}/gdk-pixbuf-2.0/
%{_darwinx_datadir}/locale/
%{_darwinx_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
%{_darwinx_libdir}/girepository-1.0/GdkPixdata-2.0.typelib
%{_darwinx_libdir}/girepository-1.0/GdkPixbuf-2.0.typelib
%{_darwinx_datadir}/gir-1.0/GdkPixbuf-2.0.gir
%{_darwinx_datadir}/gir-1.0/GdkPixdata-2.0.gir

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libgdk_pixbuf-2.0.a

%changelog
* Fri Nov  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.4-1
- Update to 2.26.4

* Tue Jul  7 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.5-1
- Update to 2.23.5

* Sun Jan 23 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.0-2
- Added support for darwinx

* Thu Jan 20 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.0-1
- Update to 2.23.0
- Generate per-target RPMs
- Drop upstreamed gdk-pixbuf-2.21.7-fix-loaders-cache-path-on-win32.patch

* Thu Oct  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-2
- Renamed the package to cross-gdk-pixbuf
- Obsoletes mingw32-gdk-pixbuf

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


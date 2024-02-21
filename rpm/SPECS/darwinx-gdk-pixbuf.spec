Name:           darwinx-gdk-pixbuf
Version:        2.42.10
Release:        1%{?dist}
Summary:        Cross compiled GDK Pixbuf library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdk-pixbuf/2.42/gdk-pixbuf-%{version}.tar.xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 109
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-gcc

BuildRequires:  darwinx-zlib
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

%prep
%setup -q -n gdk-pixbuf-%{version}

%build
%darwinx_meson \
	-Dbuiltin_loaders=all \
	-Dgio_sniffing=true \
	-Dpng=enabled \
	-Dtiff=enabled \
	-Djpeg=enabled \
	-Ddocs=false \
	-Dgtk_doc=false \
	-Dman=false \
	-Drelocatable=false \
	-Dinstalled_tests=false \
	-Dintrospection=disabled \
	-Dnative_windows_loaders=false

%darwinx_meson_build

%install
%darwinx_meson_install

%find_lang gdk-pixbuf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

# Darwinx
%files -f gdk-pixbuf.lang
%defattr(-,root,wheel,-)
%{_darwinx_bindir}/gdk-pixbuf-pixdata
%{_darwinx_bindir}/gdk-pixbuf-query-loaders
%{_darwinx_bindir}/gdk-pixbuf-thumbnailer
%{_darwinx_bindir}/gdk-pixbuf-csource
%{_darwinx_libdir}/libgdk_pixbuf-2.0.0.dylib
%{_darwinx_libdir}/libgdk_pixbuf-2.0.dylib
%{_darwinx_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_darwinx_includedir}/gdk-pixbuf-2.0/
%{_darwinx_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer

%changelog
* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.7-1
- Initial release (split off from the mingw32-gtk2 package)


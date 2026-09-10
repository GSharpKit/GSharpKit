%?ucrt_package_header

%define release_version 3.40

Name:           ucrt-libgdl
Version:        3.40.0
Release:        1%{?dist}
Summary:        MinGW Windows GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdl/%{release_version}/gdl-%{version}.tar.xz
Patch0:		gdl-3.40.0-cast.patch

BuildArch:      noarch

BuildRequires:  ucrt64-filesystem >= 98
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils

BuildRequires:  ucrt64-atk
BuildRequires:  ucrt64-cairo
BuildRequires:  ucrt64-gdk-pixbuf
BuildRequires:  ucrt64-gettext
BuildRequires:  ucrt64-glib2
BuildRequires:  ucrt64-gtk3
BuildRequires:  ucrt64-win-iconv
BuildRequires:  ucrt64-pango
BuildRequires:  ucrt64-pixman
BuildRequires:  ucrt64-zlib
BuildRequires:  ucrt64-libxml2

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.

%package -n ucrt64-libgdl
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig
Provides:       ucrt64-gdl

%description -n ucrt64-libgdl
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.

%?ucrt_debug_package


%prep
%setup -q -n gdl-%{version}
%patch 0 -p1

%build
%global ucrt64_cflags %(echo %{ucrt64_cflags}) -Wincompatible-pointer-types
%ucrt64_configure

%ucrt64_make %{?_smp_mflags} V=1


%install
%ucrt64_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/*.la

%files -n ucrt64-libgdl
%doc COPYING
%{ucrt64_bindir}/libgdl-3-5.dll
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-bar.h
%dir %{ucrt64_includedir}/libgdl-3.0
%dir %{ucrt64_includedir}/libgdl-3.0/gdl
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-item-grip.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-item.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-layout.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-master.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-object.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl-dock-placeholder.h
%{ucrt64_includedir}/libgdl-3.0/gdl/gdl.h
%{ucrt64_includedir}/libgdl-3.0/gdl/libgdltypebuiltins.h
%{ucrt64_libdir}/libgdl-3.dll.a
%{ucrt64_libdir}/pkgconfig/gdl-3.0.pc
%{ucrt64_datadir}/locale/
%{ucrt64_datadir}/gtk-doc/

%changelog
* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to ucrt-libgdl
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

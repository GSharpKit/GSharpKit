%?mingw_package_header

%define release_version 3.40

Name:           mingw-libgdl
Version:        3.40.0
Release:        1%{?dist}
Summary:        MinGW Windows GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/gdl/%{release_version}/gdl-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw32-libgdl
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig
Obsoletes:	mingw32-gdl
Provides:	mingw32-gdl

%description -n mingw32-libgdl
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.


%package -n mingw64-libgdl
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig
Obsoletes:      mingw64-gdl
Provides:       mingw64-gdl

%description -n mingw64-libgdl
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.

%?mingw_debug_package


%prep
%setup -q -n gdl-%{version}

%build
%mingw_configure

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

%mingw_find_lang %{name} --all-name

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

%files -n mingw32-libgdl -f mingw32-%{name}.lang
%doc COPYING
%{mingw32_bindir}/libgdl-3-5.dll
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-bar.h
%dir %{mingw32_includedir}/libgdl-3.0
%dir %{mingw32_includedir}/libgdl-3.0/gdl
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-item-grip.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-item.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-layout.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-master.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-object.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl-dock-placeholder.h
%{mingw32_includedir}/libgdl-3.0/gdl/gdl.h
%{mingw32_includedir}/libgdl-3.0/gdl/libgdltypebuiltins.h
%{mingw32_libdir}/libgdl-3.dll.a
%{mingw32_libdir}/pkgconfig/gdl-3.0.pc

%files -n mingw64-libgdl -f mingw64-%{name}.lang
%doc COPYING
%{mingw64_bindir}/libgdl-3-5.dll
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-bar.h
%dir %{mingw64_includedir}/libgdl-3.0
%dir %{mingw64_includedir}/libgdl-3.0/gdl
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-item-grip.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-item.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-layout.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-master.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-object.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl-dock-placeholder.h
%{mingw64_includedir}/libgdl-3.0/gdl/gdl.h
%{mingw64_includedir}/libgdl-3.0/gdl/libgdltypebuiltins.h
%{mingw64_libdir}/libgdl-3.dll.a
%{mingw64_libdir}/pkgconfig/gdl-3.0.pc

%changelog
* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to mingw-libgdl
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

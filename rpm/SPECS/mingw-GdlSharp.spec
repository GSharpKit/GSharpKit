%?mingw_package_header

%global mingw_pkg_name GdlSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define gtk_version 3.22.6

Name:           mingw-GdlSharp
Version:        3.26.0
Release:        3%{?dist}
Summary:        MinGW Windows GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/gsharpkit/GdlSharp
Source0:        GdlSharp-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-mono-core
BuildRequires:  mingw64-mono-core
BuildRequires:	mingw32-gtk3 >= %{gtk_version}
BuildRequires:	mingw64-gtk3 >= %{gtk_version}
BuildRequires:  mingw32-libgdl >= %{version}
BuildRequires:  mingw64-libgdl >= %{version}

BuildRequires:  mingw32-GtkSharp >= %{gtk_version}
BuildRequires:  mingw64-GtkSharp >= %{gtk_version}


%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw32-GdlSharp
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig
Requires:	mingw32-gtk3 >= %{gtk_version}
Requires:	mingw32-libgdl >= %{version}

Obsoletes:	mingw32-gdl-sharp
Provides:	mingw32-gdl-sharp

%description -n mingw32-GdlSharp
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.


%package -n mingw64-GdlSharp
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig
Requires:       mingw64-gtk3 >= %{gtk_version}
Requires:       mingw64-libgdl >= %{version}

Obsoletes:      mingw64-gdl-sharp
Provides:       mingw64-gdl-sharp

%description -n mingw64-GdlSharp
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.

%prep
%setup -q -n GdlSharp-%{version}

%build
sh autogen.sh --prefix=/usr
make distclean
%mingw_configure

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw32_libdir}/mono/gac/gdl-sharp/*/*.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

sed -i -e 's!/lib!/bin!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc
sed -i -e 's!/mono/gdl-sharp!!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc

rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw64_libdir}/mono/gac/gdl-sharp/*/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

sed -i -e 's!/lib!/bin!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc
sed -i -e 's!/mono/gdl-sharp!!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc

rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}


%files -n mingw32-GdlSharp
%{mingw64_prefix}%{libdir}/*.dll
%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc

%files -n mingw64-GdlSharp
%{mingw32_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to mingw-GdlSharp
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

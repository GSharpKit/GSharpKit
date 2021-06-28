%?mingw_package_header

%global mingw_pkg_name GdlSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define gtk_version 3.24.20

Name:           mingw-GdlSharp
Version:        3.34.0
Release:        2%{?dist}
Summary:        MinGW Windows GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/gsharpkit/GdlSharp
Source0:        GdlSharp-%{version}.tar.xz
Patch0:		gdl-sharp-ref.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
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

rm out/gdl-sharp.dll
patch -p0 build_win64/sources/generated/Gdl/Dock.cs < %{PATCH0}
patch -p0 build_win32/sources/generated/Gdl/Dock.cs < %{PATCH0}
%mingw_make %{?_smp_mflags} V=1

mv out/gdl-sharp.dll.config.in out/gdl-sharp.dll.config

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Mingw32
mv $RPM_BUILD_ROOT%{mingw32_prefix}/lib $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
rm $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/gdl-sharp.dll.config
sed -i -e 's!/lib!/bin!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc

# Mingw64
mv $RPM_BUILD_ROOT%{mingw64_prefix}/lib $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
rm $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/gdl-sharp.dll.config
sed -i -e 's!/lib!/bin!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc

%files -n mingw32-GdlSharp
%{mingw32_prefix}%{libdir}/*.dll
%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc

%files -n mingw64-GdlSharp
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.26.0-1
- Renamed to mingw-GdlSharp
- Updated to 3.26.0

* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

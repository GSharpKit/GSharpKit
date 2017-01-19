%?mingw_package_header

%global mingw_pkg_name gdl-sharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:           mingw-gdl-sharp
Version:        3.22.0
Release:        1%{?dist}
Summary:        MinGW Windows GDL library

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/openmedicus/gdl-sharp
Source0:        gdl-sharp-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-mono
BuildRequires:  mingw64-mono
BuildRequires:  mingw32-gdl >= %{version}
BuildRequires:  mingw64-gdl >= %{version}

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 3 library.


%package -n mingw32-gdl-sharp
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig

%description -n mingw32-gdl-sharp
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.


%package -n mingw64-gdl-sharp
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig

%description -n mingw64-gdl-sharp
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

This package contains the MinGW Windows cross compiled Gdl 3 library.

%prep
%setup -q -n gdl-sharp-%{version}

%build
sh autogen.sh --prefix=/usr
make distclean
%mingw_configure

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

%files -n mingw32-gdl-sharp
%{mingw32_libdir}/mono
%{mingw32_datadir}/pkgconfig/gdl-sharp-3.pc

%files -n mingw64-gdl-sharp
%{mingw64_libdir}/mono
%{mingw64_datadir}/pkgconfig/gdl-sharp-3.pc

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

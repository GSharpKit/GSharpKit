%global apiver  1
%global gtk_version 4.17.5
%global glib_version 2.80.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           ucrt-libadwaita
Version:        1.9.4
Release:        %autorelease
Summary:        Building blocks for modern GNOME applications

# part of src/adw-spring-animation.c is MIT
License:        LGPL-2.1-or-later AND MIT
URL:            https://gitlab.gnome.org/GNOME/libadwaita
Source0:        https://download.gnome.org/sources/libadwaita/1.9/libadwaita-%{tarball_version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
#BuildRequires:  gi-docgen
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.63.0
BuildRequires:  vala
#BuildRequires:  /usr/bin/sassc
#BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk_version}

Requires:       ucrt64-gtk4%{?_isa} >= %{gtk_version}

%description
Building blocks for modern GNOME applications.


%package -n ucrt64-libadwaita
Summary:        Building blocks for modern GNOME applications

%description -n ucrt64-libadwaita
Building blocks for modern GNOME applications.

{?%ucrt64_debug_package}

%prep
%autosetup -p1 -n libadwaita-%{tarball_version}


%build
mkdir build_ucrt
pushd build_ucrt
%ucrt64_meson \
	-Dappstream=false \
	-Ddocumentation=true \
	%{nil}
%ucrt64_meson build
popd


%install
pushd build_ucrt
%ucrt64_meson install
popd


%files -n ucrt64-libadwaita 
%license COPYING
%doc README.md AUTHORS NEWS
%{ucrt64_bindir}/adwaita-%{apiver}-demo
%{ucrt64_libdir}/%{name}-%{apiver}.so.0
%{ucrt64_libdir}/girepository-1.0/*.typelib

%changelog
* Fri Oct 16 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.6.6-1
- Initial import.


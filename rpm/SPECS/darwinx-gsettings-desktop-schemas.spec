Name:           darwinx-gsettings-desktop-schemas
Version:        44.0
Release:        1%{?dist}
Summary:        GSettings Desktop Schemas Mac OS X icon theme

License:        LGPLv3+ or CC-BY-SA
URL:            https://github.com/GNOME/gsettings-desktop-schemas
Source0:        https://github.com/GNOME/gsettings-desktop-schemas/archive/refs/tags/gsettings-desktop-schemas-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains the GSettings Desktop Schemas Mac OS X GNOME desktop.

%prep
%setup -q -n gsettings-desktop-schemas-%{version}

%build
%darwinx_meson \
    -Dintrospection=false

%darwinx_meson_build

%install
%darwinx_meson_install

%files
%defattr(-,root,wheel)
%{_darwinx_datadir}

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

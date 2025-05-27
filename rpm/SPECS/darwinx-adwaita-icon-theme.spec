Name:           darwinx-adwaita-icon-theme
Version:        48.0
Release:        1%{?dist}
Summary:        Adwaita Mac OS X icon theme

License:        LGPLv3+ or CC-BY-SA
URL:            https://github.com/GNOME/adwaita-icon-theme
Source0:        https://github.com/GNOME/adwaita-icon-theme/archive/refs/tags/adwaita-icon-theme-%{version}.tar.gz
#Source1:	adwaita-scalable.tar.xz
#Source2:	pan-down-symbolic-ltr.png
#Patch0:		osx-index.patch
BuildArch:      noarch

%description
This package contains the Adwaita Mac OS X icon theme used by the GNOME desktop.

%prep
%setup -q -n adwaita-icon-theme-%{version}

%build
%darwinx_meson

%darwinx_meson_build

%install
%darwinx_meson_install

%files
%defattr(-,root,wheel)
%{_darwinx_datadir}/licenses/adwaita-icon-theme
%{_darwinx_datadir}/icons/Adwaita
%{_darwinx_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

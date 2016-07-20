Name:           darwinx-adwaita-icon-theme
Version:        3.20.0
Release:        1%{?dist}
Summary:        Adwaita Mac OS X icon theme

License:        LGPLv3+ or CC-BY-SA
URL:            http://n00b-un-2.deviantart.com/art/OSX-Icon-Theme-for-Gnome-279284710
Source0:        http://www.deviantart.com/download/279284710/osx_icon_theme_for_gnome_by_n00b_un_2-d4ma1gm.zip
Source1:	adwaita-scalable.tar.xz
Source2:	pan-down-symbolic-ltr.png
Patch0:		osx-index.patch
BuildArch:      noarch

%description
This package contains the Adwaita Mac OS X icon theme used by the GNOME desktop.

%prep
%setup -q -n osx -b 1 
%patch0 -p1

%build


%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita

cp -rf . $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/actions/scalable
cp -rf ../adwaita-scalable/scalable/actions/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/actions/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/apps/scalable
cp -rf ../adwaita-scalable/scalable/apps/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/apps/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/categories/scalable
cp -rf ../adwaita-scalable/scalable/categories/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/categories/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/devices/scalable
cp -rf ../adwaita-scalable/scalable/devices/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/devices/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/emblems/scalable
cp -rf ../adwaita-scalable/scalable/emblems/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/emblems/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/mimes/scalable
cp -rf ../adwaita-scalable/scalable/mimetypes/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/mimes/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/places/scalable
cp -rf ../adwaita-scalable/scalable/places/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/places/scalable/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/status/scalable
cp -rf ../adwaita-scalable/scalable/status/* $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/status/scalable/

cp %{SOURCE2} $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/actions/16/pan-down-symbolic-ltr.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/actions/16/pan-up-symbolic-ltr.png

touch $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/icon-theme.cache

%files
%{_darwinx_datadir}/icons/Adwaita

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

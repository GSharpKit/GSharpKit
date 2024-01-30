Name:           darwinx-adwaita-icon-theme
Version:        44.0
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
NOCONFIGURE=yes sh autogen.sh
%{_darwinx_configure}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,wheel)
%{_darwinx_datadir}/icons/Adwaita

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

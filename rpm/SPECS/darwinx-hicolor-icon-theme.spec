Name:           darwinx-hicolor-icon-theme
Version:        0.17
Release:        1%{?dist}
Summary:        Adwaita Mac OS X icon theme

License:        LGPLv3+ or CC-BY-SA
URL:            https://www.freedesktop.org/wiki/Software/icon-theme/
Source0:        http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz
BuildArch:      noarch

%description
This package contains the Adwaita Mac OS X icon theme used by the GNOME desktop.

%prep
%setup -q -n hicolor-icon-theme-%{version}

%build
NOCONFIGURE=yes sh autogen.sh
%{_darwinx_configure}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,wheel)
%{_darwinx_datadir}/icons/hicolor

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

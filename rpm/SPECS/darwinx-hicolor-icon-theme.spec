Name:           darwinx-hicolor-icon-theme
Version:        0.17
Release:        1%{?dist}
Summary:        icon-theme contains the standard also references the default icon theme called hicolor.

License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/icon-theme
Source0:        https://www.freedesktop.org/wiki/Software/icon-theme/hicolor-icon-theme-%{version}.tar.xz
BuildArch:      noarch

%description
Icon-theme contains the standard also references the default icon theme called hicolor. 

%prep
%setup -q -n hicolor-icon-theme-%{version}

%build
%{_darwinx_configure}
make %{?_smp_mflags} || make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_darwinx_datadir}/icons/hicolor

%changelog
* Thu Jul 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.17-1
- Initial RPM

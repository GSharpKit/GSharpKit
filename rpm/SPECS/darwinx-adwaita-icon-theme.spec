%global bootstrap 0

Name:           darwinx-adwaita-icon-theme
Version:        3.14.1
Release:        1%{?dist}
Summary:        Adwaita icon theme

License:        LGPLv3+ or CC-BY-SA
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/adwaita-icon-theme/3.14/adwaita-icon-theme-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:	darwinx-librsvg2

%description
This package contains the Adwaita icon theme used by the GNOME desktop.

%prep
%setup -q -n adwaita-icon-theme-%{version}


%build
%{_darwinx_configure}
sed -i '' 's!SUBDIRS = fullcolor symbolic spinner!SUBDIRS = fullcolor spinner!g' src/Makefile
%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} install DESTDIR=%{buildroot}

touch $RPM_BUILD_ROOT%{_darwinx_datadir}/icons/Adwaita/icon-theme.cache

rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}

%files
%{_darwinx_datadir}

%changelog
* Wed Feb 25 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.14.1-1
- Initial RPM

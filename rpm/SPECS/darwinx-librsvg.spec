Name:           darwinx-librsvg2
Version:        2.40.9
Release:        1%{?dist}
Summary:        Librsvg

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.40/librsvg-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:	darwinx-libcroco

%description
An SVG library based on cairo

%prep
%setup -q -n librsvg-%{version}

%build
%{_darwinx_configure} --disable-Bsymbolic --enable-introspection=no
%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} install DESTDIR=%{buildroot}

%files
%{_darwinx_bindir}
%{_darwinx_libdir}
%{_darwinx_includedir}
%{_darwinx_datadir}

%changelog
* Tue Oct 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-3
- Split out adwaita-cursor-theme subpackage for alternate desktop spins
  (#1157324)

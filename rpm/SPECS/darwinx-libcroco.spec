Name:           darwinx-libcroco
Version:        0.6.8
Release:        1%{?dist}
Summary:        Libcroco

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/libcroco-%{version}.tar.xz

BuildArch:      noarch

%description
CSS2 parsing and manipulation library for GNOME

%prep
%setup -q -n libcroco-%{version}

%build
%{_darwinx_configure} --disable-Bsymbolic
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

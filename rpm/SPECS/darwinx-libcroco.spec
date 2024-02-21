Name:           darwinx-libcroco
Version:        0.6.13
Release:        1%{?dist}
Summary:        Libcroco

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/libcroco-%{version}.tar.xz

BuildRequires:  darwinx-filesystem-base >= 18

Requires:  	darwinx-filesystem >= 18

%description
CSS2 parsing and manipulation library for GNOME

%prep
%setup -q -n libcroco-%{version}

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-Bsymbolic \
	--disable-gtk-doc-htm
%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} install DESTDIR=%{buildroot}

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/croco-0.6-config
%{_darwinx_bindir}/csslint-0.6
%{_darwinx_libdir}/libcroco-0.6.3.dylib
%{_darwinx_libdir}/libcroco-0.6.dylib
%{_darwinx_includedir}/libcroco-0.6
%{_darwinx_libdir}/pkgconfig/libcroco-0.6.pc

%changelog
* Tue Oct 28 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.6.8-1
- First build

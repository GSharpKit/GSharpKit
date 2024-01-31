Name:           darwinx-librsvg2
Version:        2.57.1
Release:        1%{?dist}
Summary:        Librsvg

License:        LGPLv2+
URL:            http://www.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.56/librsvg-%{version}.tar.xz

BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-zlib
BuildRequires:	darwinx-libcroco

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-libcroco

%description
An SVG library based on cairo

%prep
%setup -q -n librsvg-%{version}

%build
%{_darwinx_configure} \
	--disable-gtk-doc \
	--disable-Bsymbolic \
	--enable-introspection=no \
	--enable-vala=no
%{_darwinx_make} V=1

#{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} install DESTDIR=%{buildroot}

%post
%{_darwinx_bindir}/gdk-pixbuf-query-loaders > %{_darwinx_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

%files
%defattr(-,root,wheel,-)
%{_darwinx_bindir}
%{_darwinx_libdir}
%{_darwinx_includedir}
#{_darwinx_datadir}

%changelog
* Tue Oct 28 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.40.12-1
- First build

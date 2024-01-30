Name:           darwinx-pixman
Version:        0.43.0
Release:        1%{?dist}
Summary:        Pixman is a low-level software library for pixel manipulation

License:        MIT
Group:          Development/Libraries
URL:            http://cairographics.org/releases/
Source0:        http://cairographics.org/releases/pixman-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-libpng


%description
Pixman is a low-level software library for pixel manipulation, providing 
features such as image compositing and trapezoid rasterization. Important 
users of pixman are the cairo graphics library and the X server.

%prep
%setup -q -n pixman-%{version}


%build
%darwinx_meson \
	-Dgtk=disabled \
	-Dloongson-mmi=disabled \
	-Dmmx=disabled \
	-Dsse2=disabled \
	-Dssse3=disabled \
	-Dvmx=disabled \
	-Darm-simd=disabled \
	-Dneon=disabled \
	-Diwmmxt=disabled \
	-Diwmmxt2=true \
	-Dmips-dspr2=disabled \
	-Dopenmp=disabled

%darwinx_meson_build

%install
%darwinx_meson_install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libpixman-1.dylib
%{_darwinx_libdir}/libpixman-1.*.dylib
%{_darwinx_includedir}/pixman-1/pixman-version.h
%{_darwinx_includedir}/pixman-1/pixman.h
%{_darwinx_libdir}/pkgconfig/pixman-1.pc

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.32.4-1
- Initial RPM release

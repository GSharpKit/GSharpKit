Name:           darwinx-pixman
Version:        0.33.6
Release:        1%{?dist}
Summary:        Pixman is a low-level software library for pixel manipulation

License:        MIT
Group:          Development/Libraries
URL:            http://cairographics.org/releases/
Source0:        http://cairographics.org/releases/pixman-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
Pixman is a low-level software library for pixel manipulation, providing 
features such as image compositing and trapezoid rasterization. Important 
users of pixman are the cairo graphics library and the X server.

%package static
Summary:        Pixman is a low-level software library for pixel manipulationy 
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the pixman library.

%prep
%setup -q -n pixman-%{version}


%build
%{_darwinx_configure}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_libdir}/libpixman-1.dylib
%{_darwinx_libdir}/libpixman-1.*.dylib
%{_darwinx_libdir}/libpixman-1.la
%{_darwinx_includedir}/pixman-1/pixman-version.h
%{_darwinx_includedir}/pixman-1/pixman.h
%{_darwinx_libdir}/pkgconfig/pixman-1.pc

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libpixman-1.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.32.4-1
- Initial RPM release

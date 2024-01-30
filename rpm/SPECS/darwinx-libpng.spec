Name:           darwinx-libpng
Version:        1.6.37
Release:        1%{?dist}
Summary:        libpng is the official PNG reference library.

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://prdownloads.sourceforge.net/libpng/
Source0:        libpng-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
libpng is the official PNG reference library.

%prep
%setup -q -n libpng-%{version}


%build
%{_darwinx_configure} \
	--disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/libpng-config
%{_darwinx_bindir}/libpng16-config
%{_darwinx_bindir}/png-fix-itxt
%{_darwinx_bindir}/pngfix
%{_darwinx_libdir}/libpng.dylib
%{_darwinx_libdir}/libpng16.dylib
%{_darwinx_libdir}/libpng16.*.dylib
%{_darwinx_libdir}/pkgconfig/libpng.pc
%{_darwinx_libdir}/pkgconfig/libpng16.pc
%{_darwinx_includedir}/libpng16
%{_darwinx_includedir}/png.h
%{_darwinx_includedir}/pngconf.h
%{_darwinx_includedir}/pnglibconf.h

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.13-1
- Initial RPM release

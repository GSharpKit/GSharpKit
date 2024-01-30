Name: 		darwinx-fribidi
Summary: 	Library implementing the Unicode Bidirectional Algorithm
Version: 	1.0.13
Release: 	1%{?dist}
URL: 		http://fribidi.org
Source: 	https://github.com/fribidi/fribidi/releases/fribidi-%{version}.tar.gz
License: 	LGPLv2+ and UCD
Group: 		System Environment/Libraries

BuildRequires:  darwinx-filesystem >= 6


%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%prep
%setup -q -n fribidi-%{version}

%build
%darwinx_meson \
        -Dtests=false \
        -Ddocs=false \
        -Dbin=false

%darwinx_meson_build

%install
%darwinx_meson_install

rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libfribidi.0.dylib
%{_darwinx_libdir}/libfribidi.dylib
%{_darwinx_includedir}/fribidi
%{_darwinx_libdir}/pkgconfig/*.pc

%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> 0.19.7-1
- Initial build


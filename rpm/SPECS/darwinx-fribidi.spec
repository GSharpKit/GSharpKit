Name: 		darwinx-fribidi
Summary: 	Library implementing the Unicode Bidirectional Algorithm
Version: 	1.0.12
Release: 	1%{?dist}
URL: 		http://fribidi.org
Source: 	https://github.com/fribidi/fribidi/releases/fribidi-%{version}.tar.xz
License: 	LGPLv2+ and UCD
Group: 		System Environment/Libraries
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 6


%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%prep
%setup -q -n fribidi-%{version}

%build
%{_darwinx_configure}
%{_darwinx_make}

%install
%{_darwinx_makeinstall}

rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

%files
%defattr(-,root,root)
%{_darwinx_bindir}/fribidi
%{_darwinx_libdir}/libfribidi.0.dylib
%{_darwinx_libdir}/libfribidi.dylib
%{_darwinx_libdir}/libfribidi.la
%{_darwinx_includedir}/fribidi
%{_darwinx_libdir}/pkgconfig/*.pc

%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> 0.19.7-1
- Initial build


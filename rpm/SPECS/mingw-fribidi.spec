%{?mingw_package_header}
%define debug_package %{nil}

Name: 		mingw-fribidi
Summary: 	Library implementing the Unicode Bidirectional Algorithm
Version: 	1.0.5
Release: 	1%{?dist}
URL: 		http://fribidi.org
Source: 	http://fribidi.org/download/fribidi-%{version}.tar.bz2
License: 	LGPLv2+ and UCD
Group: 		System Environment/Libraries

%description
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package -n mingw32-fribidi
Summary:        Library implementing the Unicode Bidirectional Algorithm
Requires:       pkgconfig

%description -n mingw32-fribidi
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%package -n mingw64-fribidi
Summary:        Library implementing the Unicode Bidirectional Algorithm
Requires:       pkgconfig

%description -n mingw64-fribidi
A library to handle bidirectional scripts (for example Hebrew, Arabic),
so that the display is done in the proper way; while the text data itself
is always written in logical order.

%prep
%setup -q -n fribidi-%{version}

%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

%files -n mingw32-fribidi
%doc README AUTHORS COPYING ChangeLog THANKS NEWS TODO
%{mingw32_bindir}/fribidi.exe
%{mingw32_bindir}/libfribidi-0.dll
%{mingw32_libdir}/libfribidi.dll.a
%{mingw32_includedir}/fribidi
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw64-fribidi
%doc README AUTHORS COPYING ChangeLog THANKS NEWS TODO
%{mingw64_bindir}/fribidi.exe
%{mingw64_bindir}/libfribidi-0.dll
%{mingw64_libdir}/libfribidi.dll.a
%{mingw64_includedir}/fribidi
%{mingw64_libdir}/pkgconfig/*.pc

%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> 0.19.7-1
- Initial build


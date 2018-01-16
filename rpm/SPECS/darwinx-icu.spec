%define debug_package %{nil}

%global underscore_version 57_1

Name:           darwinx-icu
Version:        57.1
Release:        1%{?dist}
Summary:        International Components for Unicode Tools

License:        MIT and UCD and Public Domain
Group:          Development/Libraries
URL:            http://icu-project.org
Source0:        http://download.icu-project.org/files/icu4c/%{version}/icu4c-%{underscore_version}-src.tgz

BuildArch:      noarch

#Patch1:	icu4c-4_8_1_1-following.patch

BuildRequires:  darwinx-filesystem >= 5
BuildRequires:  darwinx-gcc

BuildRequires:  autoconf

# Some build error in libicudata.50.1.2dylib is not linking to libicudata.50.dylib
# So we provide it here
Provides:	libicudata.50.dylib

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

%package static
Summary:        International Components for Unicode Tools
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the ICU library.


%prep
%setup -q -n icu

#%patch1 -p1 -b .following

# Needed for patch1
#pushd source
#autoconf --force
#popd


%build
pushd source
%{_darwinx_configure} \
        --enable-shared --enable-static \
        --with-data-packaging=library

%{_darwinx_make} %{?_smp_mflags}
popd

%install
pushd source
%{_darwinx_make} DESTDIR=$RPM_BUILD_ROOT install
popd

#sed -i '' -e s/"name ../lib/libicudata.50.1.2.dylib"/"name libicudata.50.dylib"/ $RPM_BUILD_ROOT%{_darwinx_libdir}/libicudata.50.1.2.dylib

rm -fr $RPM_BUILD_ROOT%{_darwinx_mandir}

# remove dangling pointers
rm -fr $RPM_BUILD_ROOT%{_darwinx_libdir}/icu/Makefile.inc
rm -fr $RPM_BUILD_ROOT%{_darwinx_libdir}/icu/pkgdata.inc

%clean
#rm -rf $RPM_BUILD_ROOT


%files
#%doc license.html unicode-license.txt

%{_darwinx_bindir}/derb
%{_darwinx_bindir}/genrb
%{_darwinx_bindir}/gendict
%{_darwinx_bindir}/gencnval
%{_darwinx_bindir}/uconv
%{_darwinx_bindir}/makeconv
%{_darwinx_bindir}/genbrk
%{_darwinx_bindir}/pkgdata
%{_darwinx_bindir}/gencfu
%{_darwinx_bindir}/icuinfo
%{_darwinx_bindir}/icu-config

%{_darwinx_sbindir}/genccode
%{_darwinx_sbindir}/gencmn
%{_darwinx_sbindir}/gennorm2
%{_darwinx_sbindir}/gensprep
%{_darwinx_sbindir}/icupkg

%{_darwinx_libdir}/libicuio*.dylib
%{_darwinx_libdir}/libicuuc*.dylib
%{_darwinx_libdir}/libicule*.dylib
%{_darwinx_libdir}/libicui18n*.dylib
%{_darwinx_libdir}/libicutu*.dylib
%{_darwinx_libdir}/libicudata*.dylib
%{_darwinx_libdir}/libiculx*.dylib
%{_darwinx_libdir}/libicutest*.dylib

%{_darwinx_libdir}/pkgconfig/icu-i18n.pc
%{_darwinx_libdir}/pkgconfig/icu-io.pc
%{_darwinx_libdir}/pkgconfig/icu-le.pc
%{_darwinx_libdir}/pkgconfig/icu-lx.pc
%{_darwinx_libdir}/pkgconfig/icu-uc.pc
%{_darwinx_includedir}/layout
%{_darwinx_includedir}/unicode
%{_darwinx_libdir}/icu
%{_darwinx_datadir}/icu

%files static
%{_darwinx_libdir}/libicudata.a
%{_darwinx_libdir}/libicui18n.a
%{_darwinx_libdir}/libicuio.a
%{_darwinx_libdir}/libicule.a
%{_darwinx_libdir}/libiculx.a
%{_darwinx_libdir}/libicutest.a
%{_darwinx_libdir}/libicutu.a
%{_darwinx_libdir}/libicuuc.a

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.8.1.1-5
- Added win64 support
- Use mingw macros without leading underscore
- Use %%global instead of %%define

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 4.8.1.1-4
- Added Erik van Pienbroek's patches to fix build with the mingw-w64 toolchain

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.8.1.1-3
- Rebuild against the mingw-w64 toolchain

* Tue Feb 07 2012 Forysiuk Paweł <tuxator@o2.pl> - 4.8.1.1-2
- Fix icu4c-4_6_1-crossbuild.patch to compile cleanly
- Minor packaging cleanup

* Tue Feb 07 2012 Forysiuk Paweł <tuxator@o2.pl> - 4.8.1.1-1
- Initial release based on openSUSE _darwinx-icu package

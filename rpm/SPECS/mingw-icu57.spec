%?mingw_package_header

%global mingw_build_win32 0
%global mingw_build_win64 1

%global underscore_version %(echo %{version} | sed 's/\\./_/g')
%global lib_version %(echo %{version} | cut -d \. -f 1)

Name:           mingw-icu57
Version:        57.1
Release:        4%{?dist}
Summary:        MinGW compilation of International Components for Unicode Tools

License:        MIT and UCD and Public Domain
URL:            http://icu-project.org
Source0:        http://download.icu-project.org/files/icu4c/%{version}/icu4c-%{underscore_version}-src.tgz

# Patch to fix the build from
# https://build.opensuse.org/package/show/windows:mingw:win32/mingw32-icu
Patch0:         icu4c-56_1-crossbuild.patch

BuildArch:      noarch

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.


# Win64
%package -n mingw64-icu57
Summary:        MinGW compilation of International Components for Unicode Tools

%description -n mingw64-icu57
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

%package -n mingw64-icu57-devel
Summary:        MinGW compilation of International Components for Unicode Tools

%description -n mingw64-icu57-devel
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.


%?mingw_debug_package


%prep
%setup -q -n icu

%patch0 -p1 -b .crossbuild


%build
pushd source

mkdir -p nativebuild
pushd nativebuild
../configure --enable-static --disable-shared
make %{?_smp_mflags} || make
popd

%mingw_configure \
        --enable-shared --disable-static \
        --with-cross-build=$(pwd)/nativebuild \
        --with-data-packaging=library

%mingw_make %{?_smp_mflags}

popd

%install
pushd source
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
popd

find $RPM_BUILD_ROOT -name "*.dll" -type l -delete

for i in $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll ; \
        do mv $i $RPM_BUILD_ROOT%{mingw64_bindir}/; done

# remove unneded files
rm -fr $RPM_BUILD_ROOT%{mingw64_mandir}

rm -fr $RPM_BUILD_ROOT%{mingw64_bindir}/icu-config
rm -fr $RPM_BUILD_ROOT%{mingw64_libdir}/icu/Makefile.inc
rm -fr $RPM_BUILD_ROOT%{mingw64_libdir}/icu/pkgdata.inc

# Win64
%files -n mingw64-icu57

%{mingw64_bindir}/icuio%{lib_version}.dll
%{mingw64_bindir}/icuuc%{lib_version}.dll
%{mingw64_bindir}/icule%{lib_version}.dll
%{mingw64_bindir}/icui18n%{lib_version}.dll
%{mingw64_bindir}/icutu%{lib_version}.dll
%{mingw64_bindir}/icudata%{lib_version}.dll
%{mingw64_bindir}/iculx%{lib_version}.dll
%{mingw64_bindir}/icutest%{lib_version}.dll

%files -n mingw64-icu57-devel
%{mingw64_bindir}/*.exe
%{mingw64_includedir}
%{mingw64_libdir}
%{mingw64_datadir}

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 57.1-1
- Update to 57.1
- Don't set group tags
- Use license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 50.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 50.1.2-3
- Fix CVE-2013-2924 (RHBZ #1015595)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Paweł Forysiuk <tuxator@o2.pl> - 50.1.2-1
- Update to 50.1.2 to match native version
- Drop icu-config script

* Sun Jan 27 2013 Paweł Forysiuk <tuxator@o2.pl> - 49.1.2-2
- Properly package icudata library

* Sun Dec 30 2012 Pawel Forysiuk <tuxator@o2.pl> - 49.1.2-1
- Update to new upstream version

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
- Initial release based on openSUSE mingw32-icu package

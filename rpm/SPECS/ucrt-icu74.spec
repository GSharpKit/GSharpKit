%{?ucrt_package_header}

%global underscore_version %(echo %{version} | sed 's/\\./_/g')
%global dash_version %(echo %{version} | sed 's/\\./-/g')
%global lib_version 74

Name:           ucrt-icu74
Version:        74.2
Release:        3%{?dist}
Summary:        MinGW compilation of International Components for Unicode Tools

License:        Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://icu-project.org
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{dash_version}/icu4c-%{underscore_version}-src.tgz

# Patch to fix the build from
# https://build.opensuse.org/package/show/windows:ucrt:win32/ucrt32-icu
Patch0:         icu4c_mingwbuild.patch

# Set standard to gnu++11 instead of c++11
# Fixes: /usr/i686-w64-ucrt32/sys-root/ucrt/include/c++/limits:2100:30: error: unable to find numeric literal operator 'operator""Q'
# (Numeric literals are a gcc extension)
Patch1:         icu-stdgnu11.patch

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-binutils

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.


# Win64
%package -n ucrt64-icu74
Summary:        MinGW compilation of International Components for Unicode Tools

%description -n ucrt64-icu74
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

%package -n ucrt64-icu74-devel
Summary:        MinGW compilation of International Components for Unicode Tools

%description -n ucrt64-icu74-devel
Devel


%{?ucrt_debug_package}


%prep
%autosetup -p1 -n icu


%build
pushd source

mkdir -p nativebuild
pushd nativebuild
../configure --enable-static --disable-shared
# Parallel build occasionally broken
%make_build || make
popd

%ucrt64_configure \
        --enable-shared --disable-static \
        --with-cross-build=$(pwd)/nativebuild \
        --with-data-packaging=library

%ucrt64_make

popd

%install
pushd source
%ucrt64_make install DESTDIR=%{buildroot}
popd

# remove unneded files
rm -fr %{buildroot}%{ucrt64_mandir}

rm %{buildroot}%{ucrt64_bindir}/icu-config
rm %{buildroot}%{ucrt64_libdir}/icu/Makefile.inc
rm %{buildroot}%{ucrt64_libdir}/icu/pkgdata.inc

rm %{buildroot}%{ucrt64_bindir}/*.exe

# Win64
%files -n ucrt64-icu74

%{ucrt64_sbindir}/escapesrc.exe
%{ucrt64_sbindir}/genccode.exe
%{ucrt64_sbindir}/gencmn.exe
%{ucrt64_sbindir}/gennorm2.exe
%{ucrt64_sbindir}/gensprep.exe
%{ucrt64_sbindir}/icupkg.exe

%{ucrt64_bindir}/icuio%{lib_version}.dll
%{ucrt64_bindir}/icuuc%{lib_version}.dll
%{ucrt64_bindir}/icui18n%{lib_version}.dll
%{ucrt64_bindir}/icutu%{lib_version}.dll
%{ucrt64_bindir}/icudata%{lib_version}.dll
%{ucrt64_bindir}/icutest%{lib_version}.dll

%files -n ucrt64-icu74-devel
%{ucrt64_libdir}/libicudata.dll.a
%{ucrt64_libdir}/libicui18n.dll.a
%{ucrt64_libdir}/libicuuc.dll.a
%{ucrt64_libdir}/libicuio.dll.a
%{ucrt64_libdir}/libicutest.dll.a
%{ucrt64_libdir}/libicutu.dll.a
%{ucrt64_libdir}/pkgconfig/icu-i18n.pc
%{ucrt64_libdir}/pkgconfig/icu-io.pc
%{ucrt64_libdir}/pkgconfig/icu-uc.pc
%{ucrt64_includedir}/unicode
%{ucrt64_libdir}/icu
%{ucrt64_datadir}/icu


%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 74.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Sandro Mani <manisandro@gmail.com> - 74.2-1
- Update to 74.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 73.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 73.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 73.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 73.2-1
- Update to 73.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 72.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 72.1-1
- Update to 72.1

* Thu Aug 04 2022 Sandro Mani <manisandro@gmail.com> - 71.1-1
- Update to 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 69.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 69.1-4
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 69.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 69.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Sandro Mani <manisandro@gmail.com> - 69.1-1
- Update to 69.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 67.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 67.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 67.1-1
- Update to 67.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 65.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 65.1-1
- Update to 65.1

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 64.2-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 23 2019 Richard W.M. Jones <rjones@redhat.com> - 64.2-2
- Bump and rebuild for RHBZ#1736119.

* Tue Aug 13 2019 Sandro Mani <manisandro@gmail.com> - 64.2-1
- Update to 64.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 57.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
- Use ucrt macros without leading underscore
- Use %%global instead of %%define

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 4.8.1.1-4
- Added Erik van Pienbroek's patches to fix build with the ucrt-w64 toolchain

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 4.8.1.1-3
- Rebuild against the ucrt-w64 toolchain

* Tue Feb 07 2012 Forysiuk Paweł <tuxator@o2.pl> - 4.8.1.1-2
- Fix icu4c-4_6_1-crossbuild.patch to compile cleanly
- Minor packaging cleanup

* Tue Feb 07 2012 Forysiuk Paweł <tuxator@o2.pl> - 4.8.1.1-1
- Initial release based on openSUSE ucrt32-icu package

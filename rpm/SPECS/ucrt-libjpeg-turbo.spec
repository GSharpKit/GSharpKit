%{?ucrt_package_header}

# Build the programs like cjpeg, etc.
# https://bugzilla.redhat.com/show_bug.cgi?id=467401#c7
%global build_programs 0

Name:           ucrt-libjpeg-turbo
Version:        3.1.2
Release:        2%{?dist}
Summary:        MinGW Windows Libjpeg-turbo library

License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/libjpeg-turbo/libjpeg-turbo
Source0:        %{url}/releases/download/%{version}/libjpeg-turbo-%{version}.tar.gz
#Patch1:         libjpeg-turbo-CET.patch

BuildArch:      noarch

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-binutils

BuildRequires:  nasm
BuildRequires:  cmake
BuildRequires:  make


%description
MinGW Windows cross compiled Libjpeg-turbo library.


# Win64
%package -n ucrt64-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      ucrt64-libjpeg < 8a-2%{?dist}
Provides:       ucrt64-libjpeg = 8a-2%{?dist}

%description -n ucrt64-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.


%package -n ucrt64-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       ucrt64-libjpeg-turbo = %{version}-%{release}
Obsoletes:      ucrt64-libjpeg-static < 8a-2%{?dist}
Provides:       ucrt64-libjpeg-static = 8a-2%{?dist}

%description -n ucrt64-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.


%package -n ucrt64-turbojpeg
Summary:        MinGW Windows turbojpeg library

%description -n ucrt64-turbojpeg
MinGW Windows cross compiled turbojpeg library.


%package -n ucrt64-turbojpeg-static
Summary:        Static version of the MinGW Windows turbojpeg library
Requires:       ucrt64-turbojpeg = %{version}-%{release}

%description -n ucrt64-turbojpeg-static
Static version of the MinGW Windows turbojpeg library.


%{?ucrt_debug_package}


%prep
%autosetup -n libjpeg-turbo-%{version} -p1


%build
%ucrt64_cmake
%ucrt64_make


%install
make install DESTDIR=%{buildroot}

# Remove manual pages and docs which duplicate Fedora native.
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{ucrt64_docdir}

# The CMake build system also installed some docs
rm -rf %{buildroot}%{ucrt64_prefix}/doc

# Remove win32 native binaries if wanted
%if %build_programs == 0
rm -f %{buildroot}%{ucrt64_bindir}/*.exe
%endif

# Fix perms
chmod -x README.md


# Win64
%files -n ucrt64-libjpeg-turbo
%license LICENSE.md
%doc README.* ChangeLog.md
%if %build_programs
%{ucrt64_bindir}/*.exe
%endif
%{ucrt64_bindir}/libjpeg-62.dll
%{ucrt64_includedir}/jconfig.h
%{ucrt64_includedir}/jerror.h
%{ucrt64_includedir}/jmorecfg.h
%{ucrt64_includedir}/jpeglib.h
%{ucrt64_libdir}/cmake/libjpeg-turbo/
%{ucrt64_libdir}/libjpeg.dll.a
%{ucrt64_libdir}/pkgconfig/libjpeg.pc

%files -n ucrt64-libjpeg-turbo-static
%{ucrt64_libdir}/libjpeg.a

%files -n ucrt64-turbojpeg
%{ucrt64_bindir}/libturbojpeg.dll
%{ucrt64_includedir}/turbojpeg.h
%{ucrt64_libdir}/libturbojpeg.dll.a
%{ucrt64_libdir}/pkgconfig/libturbojpeg.pc

%files -n ucrt64-turbojpeg-static
%{ucrt64_libdir}/libturbojpeg.a


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Sep 04 2025 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 18 2025 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Wed Sep 18 2024 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Sandro Mani <manisandro@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.1.3-2
- Rebuild with ucrt-gcc-12

* Mon Feb 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Wed Aug 11 2021 Sandro Mani <manisandro@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-3
- Fix files packaged twice

* Mon May 10 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-2
- Split off turbojpeg library

* Mon Apr 26 2021 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Apr 12 2021 Sandro Mani <manisandro@gmail.com> - 2.0.90-2
- Backport patch for CVE-2021-20205

* Thu Jan 28 2021 Sandro Mani <manisandro@gmail.com> - 2.0.90-1
- Update to 2.0.90

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Sandro Mani <manisandro@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Tue Jun 16 2020 Kalev Lember <klember@redhat.com> - 2.0.4-3
- Fix CVE-2020-13790 (#1847160)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Sandro Mani <manisandro@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Kalev Lember <klember@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Kalev Lember <klember@redhat.com> - 2.0.0-2
- Fix CVE-2018-19664 and CVE-2018-20330

* Wed Aug 01 2018 Sandro Mani <manisandro@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Kalev Lember <klember@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 1.5.0-1
- Update to 1.5.0
- Include license files
- Don't set group tags

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-4
- Fix CVE-2014-9092 (RHBZ #1169851 #1169853)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-2
- Fix compatibility with older CMake versions (as used on RHEL7)

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
- Fixes CVE-2013-6629 and CVE-2013-6630 (RHBZ #1031740)

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0
- Make jconfig.h more autoconf friendly (RHBZ #843193)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.90-1
- Update to 1.2.90

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Nicola Fontana <ntd@entidi.it> - 1.2.1-2
- Dropped phantom dependency on libpng and zlib (RHBZ #866185)

* Sun Oct 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Dropped upstreamed int32 patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-8
- Added win64 support
- Use ucrt macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-7
- Rebuild against the ucrt-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-5
- Updated the INT32 patch so that both the ucrt.org and the ucrt-w64
  toolchains are supported

* Fri Jun  3 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-4
- Fix a conflict between w32api's basetsd.h and jmorecfg.h (conflicting
  declarations for INT32)

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-3
- Moved the obsoletes/provides to the right location
- Bundle the licence and other %%doc's
- Fixed a small rpmlint warning

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-2
- Use CMake to build this package as it creates a more ucrt-friendly
  version of the library

* Thu Jun  2 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
- Temporary made the package compliant to the old guidelines as the new
  ucrt-w64 based toolchain isn't approved for inclusion in Fedora yet

* Fri Apr 15 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Made the package compliant with the new approved packaging guidelines

* Tue Feb 15 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-3
- Bumped the obsoletes ucrt32-libjpeg

* Wed Jan 19 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-2
- Generate per-target RPMs

* Sun Oct  3 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1-1
- Initial release (based on ucrt32-libjpeg)
- Dropped the BR: ucrt32-dlfcn
- Obsoletes/provides ucrt32-libjpeg and ucrt32-libjpeg-static
- Disable SIMD support for now because libtool doesn't recognize nasm


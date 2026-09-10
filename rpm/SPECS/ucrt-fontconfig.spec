%{?ucrt_package_header}

Name:           ucrt-fontconfig
Version:        2.17.1
Release:        3%{?dist}
Summary:        MinGW Windows Fontconfig library

License:        MIT
URL:            http://fontconfig.org
Source0:        https://gitlab.freedesktop.org/fontconfig/fontconfig/-/archive/%{version}/fontconfig-%{version}.tar.bz2

# Allow disabling tests (do not build)
Patch0:         fontconfig_tests.patch

BuildArch:      noarch

BuildRequires: make

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-expat
BuildRequires:  ucrt64-freetype
BuildRequires:  ucrt64-win-iconv

BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  python3

BuildRequires:  automake autoconf libtool gettext-devel


%description
MinGW Windows Fontconfig library.


# Win64
%package -n ucrt64-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig

%description -n ucrt64-fontconfig
MinGW Windows Fontconfig library.

%package -n ucrt64-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      ucrt64-fontconfig = %{version}-%{release}

%description -n ucrt64-fontconfig-static
Static version of the cross compiled Fontconfig library.


%?ucrt_debug_package


%prep
%autosetup -p1 -n fontconfig-%{version}


%build
autoreconf -ifv
%ucrt64_configure --disable-docs --disable-tests --enable-static --enable-shared --with-arch=x86_64
%ucrt64_make


%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}/%{ucrt64_libdir}/charset.alias

# Remove the .def file
rm -f %{buildroot}%{ucrt64_libdir}/fontconfig.def

# Remove .la files
rm -f %{buildroot}%{ucrt64_libdir}/*.la

# Remove duplicate manpages.
rm -rf %{buildroot}%{ucrt64_mandir}

# Remove the docs
rm -rf %{buildroot}%{ucrt64_datadir}/doc


# Win64
%files -n ucrt64-fontconfig
%license COPYING
%{ucrt64_bindir}/fc-cache.exe
%{ucrt64_bindir}/fc-cat.exe
%{ucrt64_bindir}/fc-conflist.exe
%{ucrt64_bindir}/fc-list.exe
%{ucrt64_bindir}/fc-match.exe
%{ucrt64_bindir}/fc-pattern.exe
%{ucrt64_bindir}/fc-query.exe
%{ucrt64_bindir}/fc-scan.exe
%{ucrt64_bindir}/fc-validate.exe
%{ucrt64_bindir}/libfontconfig-1.dll
%{ucrt64_libdir}/libfontconfig.dll.a
%{ucrt64_libdir}/pkgconfig/fontconfig.pc
%{ucrt64_includedir}/fontconfig/
%{ucrt64_sysconfdir}/fonts/
%{ucrt64_datadir}/fontconfig/
%dir %{ucrt64_datadir}/gettext
%dir %{ucrt64_datadir}/gettext/its
%{ucrt64_datadir}/gettext/its/fontconfig.its
%{ucrt64_datadir}/gettext/its/fontconfig.loc
%{ucrt64_datadir}/xml/fontconfig/
%{ucrt64_datadir}/locale/

%files -n ucrt64-fontconfig-static
%{ucrt64_libdir}/libfontconfig.a


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 12 2025 Sandro Mani <manisandro@gmail.com> - 2.17.1-1
- Update to 2.17.1

* Mon Jan 27 2025 Sandro Mani <manisandro@gmail.com> - 2.16.0-1
- Update to 2.16.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 2.15.0-1
- Update to 2.15.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Sandro Mani <manisandro@gmail.com> - 2.14.2-1
- Update to 2.14.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Sandro Mani <manisandro@gmail.com> - 2.14.1-1
- Update to 2.14.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 06 2022 Sandro Mani <manisandro@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.13.1-8
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.13.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.13.1-1
- Update to 2.13.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 2.12.6-1
- Update to 2.12.6

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Kalev Lember <klember@redhat.com> - 2.12.1-1
- Update to 2.12.1
- Don't set group tags

* Sat May 07 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.11.95-1
- Update to 2.11.95
- Add BuildRequires: python3 to fix FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 2.11.94-1
- Update to 2.11.94
- Use license macro for COPYING files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.11.1-1
- Update to 2.11.1

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.11.0-1
- Update to 2.11.0

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.10.95-1
- Update to 2.10.95

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.10.93-2
- Rebuild to avoid strnlen dependency which causes runtime issues on Windows XP

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.10.93-1
- Update to 2.10.93

* Sat May  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.10.92-1
- Update to 2.10.92

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.10.91-1
- Update to 2.10.91 (required by pango 1.32.6)

* Sat Oct 13 2012 Nicola Fontana <ntd@entidi.it> - 2.10.1-2
- Dropped libxml2 dependency

* Sun Oct 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0
- Dropped the autoreconf call

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-7
- Added win64 support
- Added static subpackage
- Dropped .def files

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.8.0-6
- Remove .la files

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-5
- Renamed the source package to ucrt-fontconfig (RHBZ #800379)
- Use ucrt macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-4
- Rebuild against the ucrt-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.8.0-2
- Rebuilt against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.8.0-1
- Update to 2.8.0
- Spec cleanup
- Split debug symbols in -debuginfo subpackage

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.6.0-12
- Don't install html documentation which duplicates what is in Fedora native

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-9
- Rebuild for ucrt32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-8
- Include license.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-7
- Requires pkgconfig.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-6
- Use _smp_mflags.
- Rebuild libtool configuration.
- More BRs suggested by auto-buildrequires.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-5
- Rename ucrt -> ucrt32.

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-4
- Remove duplicate manpages.
- Patch to delete logfile left when building (unused) manpages.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.6.0-3
- Add ucrt_bindir to $PATH for freetype-config script

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- Remove static library.
- +BR ucrt-libxml2.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.6.0-1
- Initial RPM release

%{?ucrt_package_header}

Name:      ucrt-gettext
Version:   0.26
Release:   2%{?dist}
Summary:   GNU libraries and utilities for producing multi-lingual messages

License:   GPL-2.0-or-later AND LGPL-2.0-or-later
URL:       http://www.gnu.org/software/gettext/
Source0:   https://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.xz
Patch0:	   ucrt-gettext-0.26-countof.patch

BuildArch: noarch

BuildRequires: make

BuildRequires: ucrt64-filesystem >= 95
BuildRequires: ucrt64-gcc
BuildRequires: ucrt64-gcc-c++
BuildRequires: ucrt64-binutils
BuildRequires: ucrt64-win-iconv
BuildRequires: ucrt64-termcap

%description
MinGW Windows Gettext library


# Win64
%package -n ucrt64-gettext
Summary:         GNU libraries and utilities for producing multi-lingual messages

%description -n ucrt64-gettext
MinGW Windows Gettext library

%package -n ucrt64-gettext-static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       ucrt64-gettext = %{version}-%{release}

%description -n ucrt64-gettext-static
Static version of the MinGW Windows Gettext library.


%{?ucrt_debug_package}


%prep
%autosetup -p1 -n gettext-%{version}

%build
export UCRT64_CFLAGS="-O2 -g -fno-optimize-strlen"
%ucrt64_configure            \
    --disable-java          \
    --disable-native-java   \
    --disable-csharp        \
    --enable-static         \
    --enable-threads=win32  \
    --without-emacs         \
    --disable-openmp

%ucrt64_make


%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{ucrt64_datadir}/locale/locale.alias
rm -f %{buildroot}%{ucrt64_libdir}/charset.alias

# Remove documentation - already available in base gettext-devel.
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{ucrt64_docdir}
rm -rf %{buildroot}%{ucrt64_infodir}

# Drop some useless tools
rm -rf %{buildroot}%{ucrt64_libdir}/gettext

# Drop all .la files and .a files
find %{buildroot} -name "*.la" -delete
rm %{buildroot}%{ucrt64_libdir}/libgettextlib.a
rm %{buildroot}%{ucrt64_libdir}/libgettextsrc.a

# Drop javaversion.class since it's a binary blob (RHBZ#2294881)
rm %{buildroot}%{ucrt64_datadir}/gettext/javaversion.class

# Win64
%files -n ucrt64-gettext
%license COPYING
%{ucrt64_bindir}/autopoint
%{ucrt64_bindir}/envsubst.exe
%{ucrt64_bindir}/gettext.exe
%{ucrt64_bindir}/gettext.sh
%{ucrt64_bindir}/gettextize
%{ucrt64_bindir}/libasprintf-0.dll
%{ucrt64_bindir}/libgettextlib-0-26.dll
%{ucrt64_bindir}/libgettextpo-0.dll
%{ucrt64_bindir}/libgettextsrc-0-26.dll
%{ucrt64_bindir}/libintl-8.dll
%{ucrt64_bindir}/libtextstyle-0.dll
%{ucrt64_bindir}/msg*.exe
%{ucrt64_bindir}/ngettext.exe
%{ucrt64_bindir}/printf_gettext.exe
%{ucrt64_bindir}/printf_ngettext.exe
%{ucrt64_bindir}/recode-sr-latin.exe
%{ucrt64_bindir}/xgettext.exe
%{ucrt64_includedir}/autosprintf.h
%{ucrt64_includedir}/gettext-po.h
%{ucrt64_includedir}/libintl.h
%{ucrt64_includedir}/textstyle.h
%{ucrt64_includedir}/textstyle/stdbool.h
%{ucrt64_includedir}/textstyle/version.h
%{ucrt64_includedir}/textstyle/woe32dll.h
%{ucrt64_libdir}/libasprintf.dll.a
%{ucrt64_libdir}/libgettextlib.dll.a
%{ucrt64_libdir}/libgettextpo.dll.a
%{ucrt64_libdir}/libgettextsrc.dll.a
%{ucrt64_libdir}/libintl.dll.a
%{ucrt64_libdir}/libtextstyle.dll.a
%dir %{ucrt64_libexecdir}/gettext/
%{ucrt64_libexecdir}/gettext/cldr-plurals.exe
%{ucrt64_libexecdir}/gettext/hostname.exe
%{ucrt64_libexecdir}/gettext/project-id
%{ucrt64_libexecdir}/gettext/urlget.exe
%{ucrt64_libexecdir}/gettext/user-email
%{ucrt64_datadir}/gettext/
%{ucrt64_datadir}/gettext-%{version}/
%{ucrt64_datadir}/aclocal/nls.m4
%{ucrt64_datadir}/locale/

%files -n ucrt64-gettext-static
%{ucrt64_libdir}/libasprintf.a
%{ucrt64_libdir}/libgettextpo.a
%{ucrt64_libdir}/libintl.a
%{ucrt64_libdir}/libtextstyle.a


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Aug 27 2025 Sandro Mani <manisandro@gmail.com> - 0.26-1
- Update to 0.26

* Sun Jul 27 2025 Sandro Mani <manisandro@gmail.com> - 0.25.1-1
- Update to 0.25.1

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 16 2025 Sandro Mani <manisandro@gmail.com> - 0.25-1
- Update to 0.25

* Tue Mar 11 2025 Sandro Mani <manisandro@gmail.com> - 0.24-1
- Update to 0.24

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Sandro Mani <manisandro@gmail.com> - 0.23.1-1
- Update to 0.23.1

* Wed Dec 18 2024 Sandro Mani <manisandro@gmail.com> - 0.23-1
- Update to 0.23

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Richard W.M. Jones <rjones@redhat.com> - 0.22.5-2
- Drop javaversion.class files (RHBZ#2294881)

* Mon Mar 04 2024 Sandro Mani <manisandro@gmail.com> - 0.22.5-1
- Update to 0.22.5

* Thu Feb 15 2024 Sandro Mani <manisandro@gmail.com> - 0.22.4-1
- Update to 0.22.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Sandro Mani <manisandro@gmail.com> - 0.22-1
- Update to 0.22

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Sandro Mani <manisandro@gmail.com> - 0.21.1-1
- Update to 0.21.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.21-5
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Sandro Mani <manisandro@gmail.com> - 0.21.0-1
- Update to 0.21.0

* Tue Jul 28 2020 Sandro Mani <manisandro@gmail.com> - 0.20.2-3
- Add gettext-printf_collision.patch

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Sandro Mani <manisandro@gmail.com> - 0.20.2-1
- Update to 0.20.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.20.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 13 2019 Fabiano Fidêncio <fidencio@redhat.com> - 0.20.1-1
- Update the sources accordingly to its native counter part, rhbz#1740721

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 0.19.7-1
- Update to 0.19.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.19.4-1
- Update to 0.19.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 0.18.3.2-1
- Update to 0.18.3.2

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.3.1-1
- Update to 0.18.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.3-1
- Update to 0.18.3
- Dropped upstreamed patch

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2.1-3
- Fix FTBFS due to invalid use of cdecl

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2.1-2
- Rebuild to resolve InterlockedCompareExchange regression in ucrt32 libraries

* Sat May  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2.1-1
- Update to 0.18.2.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2
- Removed all hacks as they're not needed any more

* Thu Dec  6 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-11
- Fix the build on RHEL6 (too old libtool)
- Minor cleanup

* Sun Jul 22 2012 Kalev Lember <kalevlember@gmail.com> - 0.18.1.1-10
- Fix message catalog split to subpackages (#842166)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-8
- Added win64 support

* Thu Mar 08 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-7
- Dropped .la files

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-6
- Renamed the source package to ucrt-gettext (RHBZ #800387)
- Use ucrt macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-5
- Rebuild against the ucrt-w64 toolchain
- Added a patch to fix compatibility with ucrt-w64

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul  6 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-3
- Rebuild again to fix incomplete dependencies

* Wed Jul  6 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.18.1.1-2
- Rebuild against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 0.18.1.1-1
- Update to 0.18.1.1
- Spec cleanup
- Split debug symbols in -debuginfo subpackage

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 0.17-16
- Removed html documentation and info pages

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.17.15
- Dropped the proxy-libintl pieces as the upstream gtk+ win32 maintainers
  also decided to drop it and it's causing more harm than good

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.17-13
- Replaced the libintl import library with a small wrapper library in order
  to let other binaries have a soft-dependency on libintl-8.dll as proposed
  on the fedora-ucrt mailing list

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.17-11
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-9
- Rebuild for ucrt32-gcc 4.4

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-8
- Use find_lang macro.

* Fri Jan 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.17-7
- Remove the manpages - already available in base Fedora gettext-devel.
- Use _smp_mflags for build.
- Added list of potential BRs.
- Added license file to doc section.

* Fri Oct 31 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-6
- Add fix for undefined Gnulib symbols (Farkas Levente).
- Rebuild against ucrt32-termcap / libtermcap.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-5
- Rename ucrt -> ucrt32.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 0.17-4
- Disable emacs lisp file install

* Thu Sep 11 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-3
- Remove static libraries.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-2
- Use RPM macros from ucrt-filesystem.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 0.17-1
- Initial RPM release, largely based on earlier work from several sources.

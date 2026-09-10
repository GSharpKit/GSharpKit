%?ucrt_package_header

Name:           ucrt-libgpg-error
Version:        1.61
Release:        1%{?dist}
Summary:        MinGW Windows GnuPGP error library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
Patch0:		ucrt-w32.patch
BuildArch:      noarch

BuildRequires: make

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-win-iconv
BuildRequires:  ucrt64-gettext

BuildRequires:  gettext

# See comment in %%prep for details
BuildRequires:  libtool autoconf automake gettext-devel


%description
MinGW Windows GnuPGP error library.


%package -n ucrt64-libgpg-error
Summary:        MinGW Windows libgpg-error compression library for the win64 target

%description -n ucrt64-libgpg-error
MinGW Windows GnuPGP error library.

%package -n ucrt64-libgpg-error-static
Summary:        Static library for ucrt64-libgpg-error development
Requires:       ucrt64-libgpg-error = %{version}-%{release}

%description -n ucrt64-libgpg-error-static
Static library for ucrt64-libgpg-error development.


%?ucrt_debug_package


%prep
%setup -q -n libgpg-error-%{version}
%patch 0 -p1

# Upstream has applied a libtool hack in libgpg-error 1.12
# which automatically gives the libgpg-error library a
# different filename for the win64 target so that
# the libgpg-error DLL's for both the win32 and win64
# targets can be installed in the same folder.
#
# As installing both win32 and win64 libraries in the same
# folder is bad practice and breaks earlier behavior undo
# this libtool hack here by re-running libtoolize
#autoreconf -i --force


%build
cp src/syscfg/lock-obj-pub.mingw32.h src/syscfg/lock-obj-pub.mingw32ucrt.h
%ucrt64_configure --enable-shared --enable-static
%ucrt64_make %{?_smp_mflags}


%install
%ucrt64_make install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Drop info and man pages as they're already provided by the native package
rm -rf $RPM_BUILD_ROOT%{ucrt64_infodir} $RPM_BUILD_ROOT%{ucrt64_mandir}

%files -n ucrt64-libgpg-error
%{ucrt64_bindir}/gpgrt-config
%{ucrt64_bindir}/gpg-error.exe
%{ucrt64_bindir}/yat2m.exe
%{ucrt64_bindir}/libgpg-error-0.dll
%{ucrt64_libdir}/libgpg-error.dll.a
%{ucrt64_libdir}/pkgconfig/gpg-error.pc
%{ucrt64_includedir}/gpg-error.h
%{ucrt64_includedir}/gpgrt.h
%{ucrt64_datadir}/aclocal/gpg-error.m4
%{ucrt64_datadir}/aclocal/gpgrt.m4
%{ucrt64_datadir}/common-lisp/source/gpg-error/*
%{ucrt64_datadir}/libgpg-error
%{ucrt64_datadir}/locale/

%files -n ucrt64-libgpg-error-static
%{ucrt64_libdir}/libgpg-error.a


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.55-1
- new version, fixes: rhbz#2385186

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.36-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.36-8
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.36-2
- Fix FTBFS errors due to new gawk, rhbz#1734862

* Tue Aug 13 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.36-1
- Update the sources accordingly to its native counter part, rhbz#1740717

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.31-1
- Update to 1.31

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 07 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.22-1
- Update to 1.22
- Fixes FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12-1
- Update to 1.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.11-1
- Update to 1.11
- Minor cleanups

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 1.10-3
- Add static libraries.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10-1
- Update to 1.10
- Added win64 support

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6-17
- Renamed the source package to ucrt-libgpg-error (RHBZ #800913)
- Use ucrt macros without leading underscore
- Dropped unneeded RPM tags
- Dropped .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6-16
- Rebuild against the ucrt-w64 toolchain
- Use correct .def file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6-13
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6-10
- Rebuild for ucrt32-gcc 4.4

* Thu Jan 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6-9
- Verify that we are still matching current native package.
- Use auto-buildrequires to identify more accurate list of BRs:
    + BR gettext (for /usr/bin/msgfmt etc)
    + BR ucrt32-dlfcn
    + BR ucrt32-iconv
- Use _smp_mflags.
- Use find_lang.

* Mon Sep 22 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-8
- Rename ucrt -> ucrt32.
- Depends on ucrt-filesystem 27.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-6
- Added signature source file & correct URLs

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-5
- Remove static libraries.

* Fri Sep  5 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-4
- Add gettext support

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-3
- Use ucrt-filesystem RPM macros.
- BuildArch is noarch.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-2
- List files explicitly and use custom CFLAGS

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- Initial RPM release, largely based on earlier work from several sources.

%{?mingw_package_header}

Name:           mingw-fontconfig
Version:        2.12.6
Release:        5%{?dist}
Summary:        MinGW Windows Fontconfig library

License:        MIT
URL:            http://fontconfig.org
Source0:        http://fontconfig.org/release/fontconfig-%{version}.tar.bz2
Patch0:         fontconfig-no-load-glyph.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-win-iconv

BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  python3


%description
MinGW Windows Fontconfig library.


# Win32
%package -n mingw32-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig

%description -n mingw32-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw32-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw32-fontconfig = %{version}-%{release}

%description -n mingw32-fontconfig-static
Static version of the cross compiled Fontconfig library.

# Win64
%package -n mingw64-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig

%description -n mingw64-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw64-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw64-fontconfig = %{version}-%{release}

%description -n mingw64-fontconfig-static
Static version of the cross compiled Fontconfig library.


%?mingw_debug_package


%prep
%setup -q -n fontconfig-%{version}
%patch0 -p1


%build
export MINGW32_CONFIGURE_ARGS="--with-arch=i686"
export MINGW64_CONFIGURE_ARGS="--with-arch=x86_64"
%mingw_configure --disable-docs --enable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{mingw32_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/charset.alias

# Remove the .def file
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/fontconfig.def
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/fontconfig.def

# Remove .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Remove duplicate manpages.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Remove the docs
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc


# Win32
%files -n mingw32-fontconfig
%license COPYING
%{mingw32_bindir}/fc-cache.exe
%{mingw32_bindir}/fc-cat.exe
%{mingw32_bindir}/fc-list.exe
%{mingw32_bindir}/fc-match.exe
%{mingw32_bindir}/fc-pattern.exe
%{mingw32_bindir}/fc-query.exe
%{mingw32_bindir}/fc-scan.exe
%{mingw32_bindir}/fc-validate.exe
%{mingw32_bindir}/libfontconfig-1.dll
%{mingw32_libdir}/libfontconfig.dll.a
%{mingw32_libdir}/pkgconfig/fontconfig.pc
%{mingw32_includedir}/fontconfig/
%{mingw32_sysconfdir}/fonts/
%{mingw32_datadir}/fontconfig/
%{mingw32_datadir}/xml/fontconfig/

%files -n mingw32-fontconfig-static
%{mingw32_libdir}/libfontconfig.a

# Win64
%files -n mingw64-fontconfig
%license COPYING
%{mingw64_bindir}/fc-cache.exe
%{mingw64_bindir}/fc-cat.exe
%{mingw64_bindir}/fc-list.exe
%{mingw64_bindir}/fc-match.exe
%{mingw64_bindir}/fc-pattern.exe
%{mingw64_bindir}/fc-query.exe
%{mingw64_bindir}/fc-scan.exe
%{mingw64_bindir}/fc-validate.exe
%{mingw64_bindir}/libfontconfig-1.dll
%{mingw64_libdir}/libfontconfig.dll.a
%{mingw64_libdir}/pkgconfig/fontconfig.pc
%{mingw64_includedir}/fontconfig/
%{mingw64_sysconfdir}/fonts/
%{mingw64_datadir}/fontconfig/
%{mingw64_datadir}/xml/fontconfig/

%files -n mingw64-fontconfig-static
%{mingw64_libdir}/libfontconfig.a


%changelog
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
- Renamed the source package to mingw-fontconfig (RHBZ #800379)
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-4
- Rebuild against the mingw-w64 toolchain

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
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-8
- Include license.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-7
- Requires pkgconfig.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-6
- Use _smp_mflags.
- Rebuild libtool configuration.
- More BRs suggested by auto-buildrequires.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-5
- Rename mingw -> mingw32.

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-4
- Remove duplicate manpages.
- Patch to delete logfile left when building (unused) manpages.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.6.0-3
- Add mingw_bindir to $PATH for freetype-config script

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- Remove static library.
- +BR mingw-libxml2.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.6.0-1
- Initial RPM release

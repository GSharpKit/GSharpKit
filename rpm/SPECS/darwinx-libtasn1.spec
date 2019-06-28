Name:           darwinx-libtasn1
Version:        4.13
Release:        1%{?dist}
Summary:        The ASN.1 library used in GNUTLS
License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/libtasn1/
Source0:        libtasn1-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libgpg-error
BuildRequires:  darwinx-libgcrypt >= 1.2.2
BuildRequires:  darwinx-gettext

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

Requires:  darwinx-filesystem >= 18

%description
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.


%prep
%setup -q -n libtasn1-%{version}

%build
%{_darwinx_configure} \
  --disable-static \
  --disable-gtk-doc
%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/asn1Coding
%{_darwinx_bindir}/asn1Decoding
%{_darwinx_bindir}/asn1Parser
%{_darwinx_includedir}/libtasn1.h
%{_darwinx_libdir}/libtasn1.6.dylib
%{_darwinx_libdir}/libtasn1.dylib
%{_darwinx_libdir}/libtasn1.la
%{_darwinx_libdir}/pkgconfig/libtasn1.pc

%changelog
* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.4-3
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.4-1
- New Fedora native version 2.6.4.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-5
- Rebuild for darwinx-gcc 4.4

* Thu Feb 19 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-4
- +BR darwinx-gcc-c++

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-3
- Include license.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-2
- Rebase to native Fedora version 2.6.3.
- Enable C++ library.
- Use find_lang macro.
- Don't build static library.
- Rebase MinGW patch to 2.6.3.
- +BR darwinx-dlfcn.
- +BR darwinx-readline.
- Force rebuild of libtool.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-4
- Requires pkgconfig.

* Thu Nov 13 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-3
- fix chain verification issue CVE-2008-4989 (#470079)
- separate out the MinGW-specific patch from the others

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-2
- Rename mingw -> darwinx.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.2-1
- New native version.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-9
- Switch to source tar.bz2 with SRP stuff removed

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-8
- Remove duplicate manpages and info files.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-7
- Add BR on autoconf, automake and libtool

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-6
- Need to run autoreconf after patching src/Makefile.am.
- Remove static libs.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-5
- Add patch to build certtool.exe because of missing dep of gnulib on intl.
- BuildArch is noarch.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-3
- Use mingw-filesystem RPM macros.
- Depends on mingw-iconv, mingw-gettext.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 2.4.1-2
- List files explicitly and use custom CFLAGS

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-1
- Initial RPM release, largely based on earlier work from several sources.

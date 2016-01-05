Name:           darwinx-libgpg-error
Version:        1.12
Release:        1%{?dist}
Summary:        Darwin Windows GnuPGP error library

License:        LGPLv2+
Group:          Development/Libraries
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext

Requires:  	darwinx-filesystem >= 18

%description
Darwin Windows GnuPGP error library.


%prep
%setup -q -n libgpg-error-%{version}


%build
%{_darwinx_configure}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_darwinx_bindir}/gpg-error-config
%{_darwinx_bindir}/gpg-error
%{_darwinx_libdir}/libgpg-error.*.dylib
%{_darwinx_libdir}/libgpg-error.dylib
%{_darwinx_libdir}/libgpg-error.la
%{_darwinx_includedir}/gpg-error.h
%{_darwinx_datadir}/aclocal/gpg-error.m4
%{_darwinx_datadir}/common-lisp/source/gpg-error/*
%{_darwinx_datadir}/locale


%changelog
* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6-13
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6-10
- Rebuild for darwinx-gcc 4.4

* Thu Jan 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6-9
- Verify that we are still matching current native package.
- Use auto-buildrequires to identify more accurate list of BRs:
    + BR gettext (for /usr/bin/msgfmt etc)
    + BR darwinx-dlfcn
    + BR darwinx-iconv
- Use _smp_mflags.
- Use find_lang.

* Mon Sep 22 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-8
- Rename mingw -> darwinx.
- Depends on mingw-filesystem 27.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-6
- Added signature source file & correct URLs

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-5
- Remove static libraries.

* Fri Sep  5 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-4
- Add gettext support

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-3
- Use mingw-filesystem RPM macros.
- BuildArch is noarch.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 1.6-2
- List files explicitly and use custom CFLAGS

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- Initial RPM release, largely based on earlier work from several sources.

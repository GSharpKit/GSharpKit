Name:           darwinx-p11-kit
Version:        0.23.20
Release:        1%{?dist}
Summary:        Library for loading and sharing PKCS#11 modules

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/p11-glue/p11-kit/releases/download/0.23.20/
Source0:        p11-kit-%{version}.tar.xz
Patch0:		p11-kit-0.18.1-free.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libgpg-error
BuildRequires:  darwinx-libgcrypt >= 1.2.2
BuildRequires:  darwinx-libtasn1 >= 3.3
BuildRequires:  darwinx-gettext

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig


%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.


%prep
%setup -q -n p11-kit-%{version}
#patch0 -p1

%build
%{_darwinx_configure} \
	--disable-static \
	--without-trust-paths \
	--disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_darwinx_sysconfdir}/pkcs11/pkcs11.conf.example
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_darwinx_bindir}/p11-kit
%{_darwinx_bindir}/trust
%{_darwinx_includedir}/p11-kit-1/p11-kit/pkcs11x.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/remote.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/p11-kit.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/pin.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/pkcs11.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/uri.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/iter.h
%{_darwinx_includedir}/p11-kit-1/p11-kit/deprecated.h
%{_darwinx_libdir}/libp11-kit.0.dylib
%{_darwinx_libdir}/libp11-kit.dylib
%{_darwinx_libdir}/libp11-kit.la
%{_darwinx_libdir}/pkcs11/p11-kit-trust.la
%{_darwinx_libdir}/pkcs11/p11-kit-trust.so
%{_darwinx_libdir}/pkgconfig/p11-kit-1.pc
%{_darwinx_datadir}/p11-kit/modules/p11-kit-trust.module
%{_darwinx_libdir}/p11-kit-proxy.dylib
%{_darwinx_libdir}/pkcs11/p11-kit-client.la
%{_darwinx_libdir}/pkcs11/p11-kit-client.so
%{_darwinx_libexecdir}/p11-kit/p11-kit-remote
%{_darwinx_libexecdir}/p11-kit/p11-kit-server
%{_darwinx_libexecdir}/p11-kit/trust-extract-compat


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

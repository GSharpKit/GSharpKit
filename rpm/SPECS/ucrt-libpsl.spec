%{?ucrt_package_header}

Name: ucrt-libpsl
Version: 0.21.0
Release: 17%{?dist}
Summary: MinGW port of C library for the Publix Suffix List
License: MIT
URL: https://rockdaboot.github.io/libpsl
Source0: https://github.com/rockdaboot/libpsl/releases/download/libpsl-%{version}/libpsl-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: python3

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc
BuildRequires: ucrt64-win-iconv
BuildRequires: ucrt64-icu
BuildRequires: ucrt64-libidn2
BuildRequires: ucrt64-libunistring

BuildRequires: publicsuffix-list

Requires: publicsuffix-list-dafsa

%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package -n ucrt64-libpsl
Summary: %{summary}
Requires: publicsuffix-list

%description -n ucrt64-libpsl
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%{?ucrt_debug_package}

%prep
%setup -q -n libpsl-%{version}
rm -frv list
ln -sv %{_datadir}/publicsuffix list
sed -i -e "1s|#!.*|#!%{__python3}|" src/psl-make-dafsa

%build
# Tarballs from github have 2 versions, one is raw files from repo, and
# the other one from CDN contains pre-generated autotools files.
# But makefile hack is not upstreamed yet so we continue reconfiguring these.
# [ -f configure ] || autoreconf -fiv
# autoreconf -fiv

# libicu does allow support for a newer IDN specification (IDN 2008) than
# libidn 1.x (IDN 2003). However, libpsl mostly relies on an internally
# compiled list, which is generated at buildtime and the testsuite thereof
# requires either libidn or libicu only at buildtime; the runtime
# requirement is only for loading external lists, which IIUC neither curl
# nor wget support. libidn2 supports IDN 2008 as well, and is *much* smaller
# than libicu.
#
# curl (as of 7.51.0-1.fc25) and wget (as of 1.19-1.fc26) now depend on libidn2.
# Therefore, we use libidn2 at runtime to help minimize core dependencies.
%ucrt64_configure --disable-silent-rules                                             \
           --disable-static                                                         \
           --disable-man                                                            \
           --disable-gtk-doc                                                        \
           --enable-builtin=libicu                                                  \
           --enable-runtime=libidn2                                                 \
           --with-psl-distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa    \
           --with-psl-file=%{_datadir}/publicsuffix/effective_tld_names.dat         \
           --with-psl-testfile=%{_datadir}/publicsuffix/test_psl.txt

# avoid using rpath
sed -i libtool \
    -e 's|^\(runpath_var=\).*$|\1|' \
    -e 's|^\(hardcode_libdir_flag_spec=\).*$|\1|'

%ucrt64_make %{?_smp_mflags}

%install
%ucrt64_make install DESTDIR=$RPM_BUILD_ROOT
install -m0755 src/psl-make-dafsa %{buildroot}%{ucrt64_bindir}/

find $RPM_BUILD_ROOT -name '*.la' -delete -print

rm -f $RPM_BUILD_ROOT%{ucrt64_libdir}/libpsl.a

rm -rf $RPM_BUILD_ROOT%{ucrt64_datadir}/man

%files -n ucrt64-libpsl
%license COPYING
%doc AUTHORS NEWS
%{ucrt64_bindir}/psl.exe
%{ucrt64_bindir}/psl-make-dafsa
%{ucrt64_bindir}/libpsl-5.dll
%{ucrt64_includedir}/libpsl.h
%{ucrt64_libdir}/libpsl.dll.a
%{ucrt64_libdir}/pkgconfig/libpsl.pc

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.21.0-8
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Fabiano Fidêncio <fidencio@redhat.com> - 0.21.0-3
- Add python as a build requirement - rhbz#1799649

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Fabiano Fidêncio <fidencio@redhat.com> - 0.21.0-1
- Initial package

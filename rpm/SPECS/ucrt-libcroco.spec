%{?ucrt_package_header}

Name:           ucrt-libcroco
Version:        0.6.12
Release:        23%{?dist}
Summary:        A CSS2 parsing library for MinGW

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://ftp.gnome.org/pub/GNOME/sources/libcroco/
Source:         http://download.gnome.org/sources/libcroco/0.6/libcroco-%{version}.tar.xz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-glib2
BuildRequires:  ucrt64-pkg-config
BuildRequires:  ucrt64-libxml2

%description
CSS2 parsing and manipulation library for GNOME

This is the MinGW version of this library.

%package -n ucrt64-libcroco
Summary:        MinGW A CSS2 parsing library
Requires:       pkgconfig

%description -n ucrt64-libcroco
This package contains the header files and libraries needed to develop MinGW
applications that use libcroco-0.6.

%package -n ucrt64-libcroco-static
Summary:        MinGW static A CSS2 parsing library
Requires:       ucrt64-libcroco = %{version}-%{release}

%description -n ucrt64-libcroco-static
This package contains the static libraries needed to develop MinGW
applications that use libcroco-0.6.

%{?ucrt_debug_package}


%prep
%setup -q -n libcroco-%{version}


%build
%ucrt64_configure --without-pic --disable-gtk-doc-html
%ucrt64_make %{?_smp_mflags} V=1


%install
%ucrt64_make install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

rm -rf %{buildroot}%{ucrt64_datadir}/gtk-doc

%files -n ucrt64-libcroco
%license COPYING
%doc AUTHORS README NEWS
%{ucrt64_bindir}/croco-0.6-config
%{ucrt64_bindir}/csslint-0.6.exe
%{ucrt64_bindir}/libcroco-0.6-3.dll
%{ucrt64_includedir}/libcroco-0.6
%{ucrt64_libdir}/libcroco-0.6.dll.a
%{ucrt64_libdir}/pkgconfig/*.pc

%files -n ucrt64-libcroco-static
%{ucrt64_libdir}/libcroco-0.6.a

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.12-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.6.12-13
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:41:48 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.6.12-9
- Rebuild (ucrt-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 0.6.12-1
- Update to 0.6.12

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 0.6.11-1
- Update to 0.6.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Kalev Lember <klember@redhat.com> - 0.6.9-1
- Update to 0.6.9
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Richard Hughes <richard@hughsie.com> - 0.6.8-1
- Initial packaging attempt

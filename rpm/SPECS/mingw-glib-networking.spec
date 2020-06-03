%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-glib-networking
Version:        2.64.3
Release:        1%{?dist}
Summary:        MinGW Windows glib-networking library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glib-networking/%{release_version}/glib-networking-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-gnutls >= 2.10
BuildRequires:  mingw64-gnutls >= 2.10
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  meson

%description
This package contains modules that extend the networking support in GIO.


%package -n mingw32-glib-networking
Summary:        MinGW Windows glib-networking library

%description -n mingw32-glib-networking
This package contains modules that extend the networking support in GIO.


%package -n mingw64-glib-networking
Summary:        MinGW Windows glib-networking library

%description -n mingw64-glib-networking
This package contains modules that extend the networking support in GIO.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n glib-networking-%{version}


%build
%mingw_meson -Dlibproxy_support=false -Dgnome_proxy_support=false
%mingw_ninja


%install
%mingw_ninja_install

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gio/modules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gio/modules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gio/modules/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gio/modules/*.la

%mingw_find_lang glib-networking


%files -n mingw32-glib-networking -f mingw32-glib-networking.lang
%license COPYING
%{mingw32_libdir}/gio/modules/libgiognutls.dll

%files -n mingw64-glib-networking -f mingw64-glib-networking.lang
%license COPYING
%{mingw64_libdir}/gio/modules/libgiognutls.dll


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.62.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Sandro Mani <manisandro@gmail.com> - 2.62.3-1
- Update to 2.62.3

* Tue Dec 10 2019 Sandro Mani <manisandro@gmail.com> - 2.62.2-1
- Update to 2.62.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.62.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.62.1-1
- Update to 2.62.1

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 2.62.0-1
- Update to 2.62.0

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.61.2-1
- Update to 2.61.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Christophe Fergeau <cfergeau@redhat.com> - 2.57.90-1
- Sync with native rawhide package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.54.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 2.54.0-1
- Update to 2.54.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Kalev Lember <klember@redhat.com> - 2.50.0-1
- Update to 2.50.0
- Don't set group tags

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.48.2-1
- Update to 2.48.2

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 2.48.1-1
- Update to 2.48.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.46.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.46.0-1
- Update to 2.46.0

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 2.45.1-1
- Update to 2.45.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-2
- Rebuilt for mingw-gnutls 3.4 ABI change

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-1
- Update to 2.44.0
- Use license macro for the COPYING file

* Fri Oct 17 2014 Kalev Lember <kalevlember@gmail.com> - 2.42.0-1
- Update to 2.42.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.38.2-1
- Update to 2.38.2

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.37.5-1
- Update to 2.37.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.27.4-1
- Update to 2.37.4

* Thu May  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.37.1-1
- Update to 2.37.1

* Fri Mar 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.36.0-1
- Update to 2.36.0

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.35.9-1
- Update to 2.35.9

* Fri Feb  8 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.35.6-1
- Update to 2.35.6

* Wed Nov 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.2-1
- Update to 2.34.2

* Sat Oct 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.0-1
- Update to 2.34.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.32.1-1
- Update to 2.32.1

* Mon Mar 26 2012 Kalev Lember <kalevlember@gmail.com> - 2.32.0-1
- Update to 2.32.0
- Dropped upstreamed patch

* Fri Mar 16 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.16-3
- Build 64 bit Windows binaries

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.31.16-2
- Renamed the source package to mingw-glib-networking (RHBZ #800391)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.31.16-1
- Update to 2.31.16
- Patch to fix linking against pkcs11-enabled gnutls

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.31.6-1
- Update to 2.31.6
- Dropped upstreamed patch
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Kalev Lember <kalevlember@gmail.com> - 2.30.1-1
- Update to 2.30.1
- Added a patch to fix build without gnome-proxy

* Sun Oct 02 2011 Kalev Lember <kalevlember@gmail.com> - 2.30.0-1
- Update to 2.30.0
- Use automatic mingw dep extraction
- Switch to .xz tarballs

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.6.1-2
- Dropped Requires: pkgconfig (#700348)

* Wed Apr 27 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.6.1-1
- Initial RPM release

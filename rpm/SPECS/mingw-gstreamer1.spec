%?mingw_package_header

%global api_version 1.0

Name:           mingw-gstreamer1
Version:        1.16.2
Release:        1%{?dist}
Summary:        MinGW Windows Streaming-Media Framework Runtime

License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2

BuildRequires:  bison flex
BuildRequires:  perl-interpreter
# use native glib-genmarshal and glib-mkenums
BuildRequires:  glib2-devel


%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win32
%package  -n mingw32-gstreamer1
Summary:        MinGW Windows Streaming-Media Framework Runtime

%description -n mingw32-gstreamer1
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.

# Win64
%package  -n mingw64-gstreamer1
Summary:        MinGW Windows Streaming-Media Framework Runtime

%description -n mingw64-gstreamer1
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plug-in-based architecture
means that new data types or processing capabilities can be added by
installing new plug-ins.


%?mingw_debug_package


%prep
%setup -q -n gstreamer-%{version}


%build
%mingw_configure                                                       \
    --with-package-name='Fedora MinGW GStreamer package'               \
    --with-package-origin='http://download.fedoraproject.org'          \
    --enable-shared                                                    \
    --disable-static                                                   \
    --disable-gtk-doc                                                  \
    --enable-debug                                                     \
    --disable-fatal-warnings                                           \
    --disable-silent-rules                                             \
    --disable-tests                                                    \
    --disable-examples

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gstreamer-%{api_version}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/*gst*
rm -fr $RPM_BUILD_ROOT%{mingw32_datadir}/gdb
rm -fr $RPM_BUILD_ROOT%{mingw32_datadir}/gstreamer-%{api_version}/gdb

rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gstreamer-%{api_version}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/*gst*
rm -fr $RPM_BUILD_ROOT%{mingw64_datadir}/gdb
rm -fr $RPM_BUILD_ROOT%{mingw64_datadir}/gstreamer-%{api_version}/gdb

# Remove silly target prefix from binaries
for prefixed_file in $RPM_BUILD_ROOT%{mingw32_bindir}/%{mingw32_target}-*.exe \
                     $RPM_BUILD_ROOT%{mingw64_bindir}/%{mingw64_target}-*.exe \
                     $RPM_BUILD_ROOT%{mingw32_libexecdir}/*/%{mingw32_target}-*.exe \
                     $RPM_BUILD_ROOT%{mingw64_libexecdir}/*/%{mingw64_target}-*.exe
do
    f=$(echo $prefixed_file | sed -e 's/%{mingw32_target}-//' \
                                  -e 's/%{mingw64_target}-//')
    mv $prefixed_file $f
done

%mingw_find_lang gstreamer-%{api_version}


# Win32
%files -n mingw32-gstreamer1 -f mingw32-gstreamer-%{api_version}.lang
%license COPYING

%dir %{mingw32_includedir}/gstreamer-%{api_version}
%{mingw32_includedir}/gstreamer-%{api_version}/gst

%dir %{mingw32_libexecdir}/gstreamer-%{api_version}
%{mingw32_libexecdir}/gstreamer-%{api_version}/gst-completion-helper.exe
%{mingw32_libexecdir}/gstreamer-%{api_version}/gst-plugin-scanner.exe

%dir %{mingw32_libdir}/gstreamer-%{api_version}/
%{mingw32_libdir}/gstreamer-%{api_version}/*.dll
%{mingw32_libdir}/libgstbase-%{api_version}.dll.a
%{mingw32_libdir}/libgstcontroller-%{api_version}.dll.a
%{mingw32_libdir}/libgstnet-%{api_version}.dll.a
%{mingw32_libdir}/libgstreamer-%{api_version}.dll.a
%{mingw32_libdir}/pkgconfig/gstreamer-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-base-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-controller-%{api_version}.pc
%{mingw32_libdir}/pkgconfig/gstreamer-net-%{api_version}.pc

%{mingw32_bindir}/gst-inspect-%{api_version}.exe
%{mingw32_bindir}/gst-launch-%{api_version}.exe
%{mingw32_bindir}/gst-stats-%{api_version}.exe
%{mingw32_bindir}/gst-typefind-%{api_version}.exe

%{mingw32_bindir}/libgstbase-%{api_version}-0.dll
%{mingw32_bindir}/libgstcontroller-%{api_version}-0.dll
%{mingw32_bindir}/libgstnet-%{api_version}-0.dll
%{mingw32_bindir}/libgstreamer-%{api_version}-0.dll

%{mingw32_datadir}/aclocal/gst-element-check-%{api_version}.m4
%{mingw32_datadir}/bash-completion/


# Win64
%files -n mingw64-gstreamer1 -f mingw64-gstreamer-%{api_version}.lang
%license COPYING

%dir %{mingw64_includedir}/gstreamer-%{api_version}
%{mingw64_includedir}/gstreamer-%{api_version}/gst

%dir %{mingw64_libexecdir}/gstreamer-%{api_version}
%{mingw64_libexecdir}/gstreamer-%{api_version}/gst-completion-helper.exe
%{mingw64_libexecdir}/gstreamer-%{api_version}/gst-plugin-scanner.exe

%dir %{mingw64_libdir}/gstreamer-%{api_version}/
%{mingw64_libdir}/gstreamer-%{api_version}/*.dll
%{mingw64_libdir}/libgstbase-%{api_version}.dll.a
%{mingw64_libdir}/libgstcontroller-%{api_version}.dll.a
%{mingw64_libdir}/libgstnet-%{api_version}.dll.a
%{mingw64_libdir}/libgstreamer-%{api_version}.dll.a
%{mingw64_libdir}/pkgconfig/gstreamer-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-base-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-controller-%{api_version}.pc
%{mingw64_libdir}/pkgconfig/gstreamer-net-%{api_version}.pc

%{mingw64_bindir}/gst-inspect-%{api_version}.exe
%{mingw64_bindir}/gst-launch-%{api_version}.exe
%{mingw64_bindir}/gst-stats-%{api_version}.exe
%{mingw64_bindir}/gst-typefind-%{api_version}.exe

%{mingw64_bindir}/libgstbase-%{api_version}-0.dll
%{mingw64_bindir}/libgstcontroller-%{api_version}-0.dll
%{mingw64_bindir}/libgstnet-%{api_version}-0.dll
%{mingw64_bindir}/libgstreamer-%{api_version}-0.dll

%{mingw64_datadir}/aclocal/gst-element-check-%{api_version}.m4
%{mingw64_datadir}/bash-completion/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.2-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.14.2-1
- Update to 1.14.2

* Mon Jul 16 2018 Victor Toso <victortoso@redhat.com> - 1.14.1-1
- Update to 1.14.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.12.3-1
- Update to 1.12.3

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.12.1-3
- Fix debug files in main package
- Fix FTBFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Tue Feb  7 2017 Victor Toso <victortoso@redhat.com> - 1.11.1-1
- Update to 1.11.1

* Fri Nov  4 2016 Victor Toso <victortoso@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Paweł Forysiuk <tuxator@o2.pl> - 1.4.5-1
- Update to 1.4.5

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Wed Dec  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4
- Fixes FTBFS when winpthreads is available

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Paweł Forysiuk <tuxator@o2.pl> - 1.0.6-1
- Initial packaging

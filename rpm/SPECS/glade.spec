Name:           glade
Version:        3.21.0
Release:        1%{?dist}
Summary:        User Interface Designer for GTK+

# - /usr/bin/glade is GPLv2+
# - /usr/bin/glade-previewer is LGPLv2+
# - libgladeui-2.so, libgladegtk.so, and libgladepython.so all combine
#   GPLv2+ and LGPLv2+ code, so the resulting binaries are GPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://glade.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glade/3.20/glade-%{version}.tar.xz

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxml2-devel
BuildRequires:  pygobject3-devel
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# The gtk3 version of glade was packaged under the name of 'glade3' for a
# while. However, following upstream naming, 'glade3' package is now the gtk2
# version and 'glade' package is the gtk3 one. The obsoletes are here to
# provide seamless upgrade path from the gtk3 based 'glade3'.
Obsoletes:      glade3 < 1:3.11.0-3

%description
Glade is a RAD tool to enable quick and easy development of user interfaces for
the GTK+ toolkit and the GNOME desktop environment.

The user interfaces designed in Glade are saved as XML, which can be used in
numerous programming languages including C, C++, C#, Vala, Java, Perl, Python,
and others.


%package libs
Summary:        Widget library for Glade UI designer
Obsoletes:      glade3-libgladeui < 1:3.11.0-3

%description    libs
The %{name}-libs package consists of the widgets that compose the Glade GUI as
a separate library to ease the integration of Glade into other applications.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      glade3-libgladeui-devel < 1:3.11.0-3

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use Glade widget library.


%prep
%setup -q

%build
export PYTHON=%{__python3}
%configure --disable-static

# Omit unused direct shared library dependencies.
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

# Remove rpaths.
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/glade*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/glade/modules/*.so

%find_lang glade --with-gnome


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/glade.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/glade.desktop


%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files -f glade.lang
%license COPYING*
%doc AUTHORS NEWS README
%{_bindir}/glade
%{_bindir}/glade-previewer
%{_datadir}/applications/glade.desktop
%{_datadir}/icons/hicolor/*/apps/glade.png
%{_datadir}/icons/hicolor/scalable/apps/glade-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/glade-brand-symbolic.svg
%{_datadir}/metainfo/glade.appdata.xml
%{_mandir}/man1/glade.1*
%{_mandir}/man1/glade-previewer*

%files libs
%license COPYING*
%{_libdir}/girepository-1.0/Gladeui-2.0.typelib
%dir %{_libdir}/glade/
%dir %{_libdir}/glade/modules/
%{_libdir}/glade/modules/libgladegtk.so
%{_libdir}/glade/modules/libgladepython.so
%{_libdir}/libgladeui-2.so.*
%{_datadir}/glade/

%files devel
%{_includedir}/libgladeui-2.0/
%{_libdir}/libgladeui-2.so
%{_libdir}/pkgconfig/gladeui-2.0.pc
%{_datadir}/gir-1.0/Gladeui-2.0.gir
%doc %{_datadir}/gtk-doc/

%changelog
* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Robert Kuska <rkuska@redhat.com> - 3.19.0-4
- Rebuilt for Python3.5 rebuild

* Fri Jul 03 2015 Kalev Lember <klember@redhat.com> - 3.19.0-3
- Switch to Python 3 (#1238957)
- Use the make_install macro
- Use upstream screenshots for appdata
- Validate appdata file
- Tighten deps with the _isa macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Kalev Lember <kalevlember@gmail.com> - 3.19.0-1
- Update to 3.19.0
- Use license macro for COPYING files

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.18.3-5
- Use better AppData screenshots

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.18.3-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.18.3-1
- Update to 3.18.3

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.18.2-1
- Update to 3.18.2

* Wed Mar 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.18.1-1
- Update to 3.18.1

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Wed Jan 08 2014 Richard Hughes <rhughes@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Wed Sep 25 2013 Richard Hughes <rhughes@redhat.com> - 3.16.0-1
- Update to 3.16.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.15.4-1
- Update to 3.15.4

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.15.3-1
- Update to 3.15.3

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.15.2-3.git9d3b3b3
- Update to git snapshot to adapt to API changes in GTK+ 3.9.10
- Add man pages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Fri May 10 2013 Richard Hughes <rhughes@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.15.0-1
- Update to 3.15.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.14.2-2
- Revise the summary for consistency with the parallel installable
  glade2/glade3 packages (#882557)

* Mon Nov 26 2012 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0
- Remove the unrecognized --disable-scrollkeeper option

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Thu Apr 12 2012 Kalev Lember <kalevlember@gmail.com> - 3.12.0-3
- Update the spec file comments about licensing and simplify the License tag
- Install the typelib in -libs subpackage

* Fri Apr 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Review fixes (#806093)
- Use find_lang --with-gnome for including help files
- Include license files also in the main package in addition to -libs

* Wed Apr 04 2012 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Thu Mar 22 2012 Kalev Lember <kalevlember@gmail.com> - 3.11.0-1
- Initial packaging based on Fedora glade3
- Rename the package to glade; added obsoletes for upgrade path
- Spec clean up for review

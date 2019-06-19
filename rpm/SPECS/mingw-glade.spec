%?mingw_package_header

Name:           mingw-glade
Version:        3.22.1
Release:        1%{?dist}
Summary:        User Interface Designer for GTK+

# - /usr/bin/glade is GPLv2+
# - /usr/bin/glade-previewer is LGPLv2+
# - libgladeui-2.so, libgladegtk.so, and libgladepython.so all combine
#   GPLv2+ and LGPLv2+ code, so the resulting binaries are GPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://glade.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glade/3.22/glade-%{version}.tar.xz

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

%description
Glade is a RAD tool to enable quick and easy development of user interfaces for
the GTK+ toolkit and the GNOME desktop environment.

The user interfaces designed in Glade are saved as XML, which can be used in
numerous programming languages including C, C++, C#, Vala, Java, Perl, Python,
and others.

%package -n mingw32-glade
Summary:        User Interface Designer for GTK+

%description -n mingw32-glade
Glade is a RAD tool to enable quick and easy development of user interfaces for
the GTK+ toolkit and the GNOME desktop environment.

The user interfaces designed in Glade are saved as XML, which can be used in
numerous programming languages including C, C++, C#, Vala, Java, Perl, Python,
and others.

%package -n mingw64-glade
Summary:        User Interface Designer for GTK+

%description -n mingw64-glade
Glade is a RAD tool to enable quick and easy development of user interfaces for
the GTK+ toolkit and the GNOME desktop environment.

The user interfaces designed in Glade are saved as XML, which can be used in
numerous programming languages including C, C++, C#, Vala, Java, Perl, Python,
and others.

%prep
%setup -q -n glade-%{version}

%build
%mingw_configure

#mingw_make %{?_smp_mflags} V=1
%mingw_make

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

%files -n mingw32-glade
%{mingw32_bindir}/glade
%{mingw32_bindir}/glade-previewer

%files -n mingw64-glade
%{mingw64_bindir}/glade
%{mingw64_bindir}/glade-previewer

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

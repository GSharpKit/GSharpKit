%define debug_package %{nil}

%define libdir /lib

Name:           darwinx-GtkSharp
Version:        3.24.24.34
Release:        1%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://github.com/GSharpKit/GtkSharp/releases 
Source0:        GtkSharp-%{version}.tar.gz
Source1:        darwinx-gdk-sharp-3.0.pc
Source2:        darwinx-glib-sharp-3.0.pc
Source3:        darwinx-gio-sharp-3.0.pc
Source4:        darwinx-gtk-sharp-3.0.pc
Source5:        GtkSharp.snk
Source100:      darwinx-gapi3-codegen
Source101:      darwinx-gapi3-fixup
Source102:      darwinx-gapi3-parser
Source103:      gapi-fixup.exe
Source104:      gapi-parser.exe
Source105:      gapi2xml.pl
Source106:      gapi_codegen.exe
Source107:      gapi_pp.pl
Source108:      gapi-3.0.pc

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-gtk3 >= %{version}

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-mono-core >= 4.8
BuildRequires:  automake, libtool
BuildRequires:	darwinx-gtk3 >= %{version}

BuildArch:	noarch

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

%package gapi
Group:        Development/Languages
Summary:      Glib and GObject C source parser and C generator for the creation and maintenance of managed bindings for Mono and .NET

%description gapi
This package provides developer tools for the creation and
maintenance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk.

%prep
%setup -q -n GtkSharp-%{version}

sed -i -e 's!netcoreapp3.1!netcoreapp5.0!g' Source/Samples/Samples.csproj

%build
CAKE_SETTINGS_SKIPVERIFICATION=true sh build.sh

%install
%{__rm} -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -m 644 BuildOutput/Release/AtkSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/CairoSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/GdkSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/GioSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/GLibSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/GtkSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 BuildOutput/Release/PangoSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

mkdir -p %{buildroot}%{_darwinx_prefix}/share/pkgconfig
install -m 644 %{SOURCE1} %{buildroot}%{_darwinx_prefix}/share/pkgconfig/gdk-sharp-3.0.pc
install -m 644 %{SOURCE2} %{buildroot}%{_darwinx_prefix}/share/pkgconfig/glib-sharp-3.0.pc
install -m 644 %{SOURCE3} %{buildroot}%{_darwinx_prefix}/share/pkgconfig/gio-sharp-3.0.pc
install -m 644 %{SOURCE4} %{buildroot}%{_darwinx_prefix}/share/pkgconfig/gtk-sharp-3.0.pc
install -m 644 %{SOURCE108} %{buildroot}%{_darwinx_prefix}/share/pkgconfig/

sed -i '' 's!@PREFIX@!%{_darwinx_prefix}!g' %{buildroot}%{_darwinx_prefix}/share/pkgconfig/*.pc

mkdir -p %{buildroot}%{_darwinx_prefix}/share/gapi-3.0
cp Source/Libs/*/*Sharp-api.xml %{buildroot}%{_darwinx_prefix}/share/gapi-3.0/

mkdir -p %{buildroot}%{_darwinx_prefix}/bin
install -m 755 %{SOURCE100} %{buildroot}%{_darwinx_prefix}/bin/gapi3-codegen
install -m 755 %{SOURCE101} %{buildroot}%{_darwinx_prefix}/bin/gapi3-fixup
install -m 755 %{SOURCE102} %{buildroot}%{_darwinx_prefix}/bin/gapi3-parser

sed -i '' 's!@PREFIX@!%{_darwinx_prefix}!g' %{buildroot}%{_darwinx_prefix}/bin/gapi3-codegen
sed -i '' 's!@PREFIX@!%{_darwinx_prefix}!g' %{buildroot}%{_darwinx_prefix}/bin/gapi3-fixup
sed -i '' 's!@PREFIX@!%{_darwinx_prefix}!g' %{buildroot}%{_darwinx_prefix}/bin/gapi3-parser

mkdir -p %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0
install -m 755 %{SOURCE103} %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE104} %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE105} %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE106} %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE107} %{buildroot}%{_darwinx_prefix}/lib/gapi-3.0/

%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*Sharp.dll
%{_darwinx_datadir}/pkgconfig/*-sharp-3.0.pc

%files gapi
%defattr(-,root,root,-)
%dir %{_darwinx_prefix}/lib/gapi-3.0
%{_darwinx_bindir}/gapi3-codegen
%{_darwinx_bindir}/gapi3-fixup
%{_darwinx_bindir}/gapi3-parser
%{_darwinx_prefix}/lib/gapi-3.0/gapi_codegen.exe
%{_darwinx_prefix}/lib/gapi-3.0/gapi-fixup.exe
%{_darwinx_prefix}/lib/gapi-3.0/gapi-parser.exe
%{_darwinx_prefix}/lib/gapi-3.0/gapi_pp.pl
%{_darwinx_prefix}/lib/gapi-3.0/gapi2xml.pl
%{_darwinx_datadir}/gapi-3.0
%{_darwinx_prefix}/share/pkgconfig/gapi-3.0.pc

%changelog
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Dennis Gilmore <dennis@ausil.us> - 2.12.7-3
- build 32 bit sparc sparcv9

* Sat Dec 20 2008 Xavier lamien <lxtnow[at]gmail.com> - 2.12.7-2
- Rebuild.

* Fri Dec 12 2008 Xavier lamien <lxtnow[at]gmail.com> - 2.12.7-1
- Update release.

* Mon Dec 8 2008 Matthias Clasen <mclasen@redhat.com> - 2.12.5-2
- Rebuild to fix pkg-config autoprovides

* Sat Nov 08 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.5-1
- Update release.

* Wed Oct 22 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.4-1
- Update release.

* Thu Sep 18 2008 Nigel Jones <dev@nigelj.com> - 2.12.3-1
- New minor release (.3)

* Mon Jul 14 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.1-3
- Fix/Update libdir on GACUTIL & monodoc.

* Mon Jul 14 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.12.1-2
- Rebuild for fixed RPM for mono provides.

* Sun Jul 13 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.1-1
- Update release.

* Sat May 31 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.0-2
- Fixed monodoc libdir.

* Fri May 23 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.12.0-1
- Updated Release.

* Mon Mar 03 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.10.3-2
- Fixed Assembly_dir on Rawhide (bug #434286).

* Wed Feb 27 2008 Xavier Lamien	<lxtnow[at]gmail.com> - 2.10.3-1
- Updated Release.
- Updated -libdir.patch against new release.

* Tue Jan 01 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.10.2-1
- Updated Release.
- Fixed lisence tag.
- Fixed source0 path.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.10.0-6
- Rebuild for selinux ppc32 issue.

* Thu Jul 26 2007 Matthias Clasen  <mclasen@redhat.com> - 2.10.4-5
- Add alpha to ExclusiveArch (#246206)

* Tue Apr 17 2007 Alexander Larsson <alexl@redhat.com> 2.10.0-4
- Rebuild (#236295)

* Tue Sep 12 2006 Alexander Larsson <alexl@redhat.com> - 2.10.0-3
- Add -doc subpackage with the monodoc docs (#205561)

* Mon Sep 11 2006 Alexander Larsson <alexl@redhat.com> - 2.10.0-2
- Fix pc files for gapidir (#205979)

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1.fc6
- Update to 2.10.0

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.9.0-2.fc6
- Fix pkgconfig requires

* Mon Aug 14 2006 Alexander Larsson <alexl@redhat.com> - 2.9.0-1
- update to 2.9.0, which splits out gnome stuff to gnome-sharp
- Split out devel package

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Jun  9 2006 Alexander Larsson <alexl@redhat.com> - 2.8.2-2
- Disable on s390* as mono doesn't build on s390 atm

* Fri Mar  3 2006 Christopher Aillon <caillon@redhat.com> - 2.8.2-1
- Update to 2.8.2 to fix an issue with marshalling on x86-64

* Fri Feb 10 2006 Christopher Aillon <caillon@redhat.com> - 2.8.1-1
- Update to 2.8.1

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.8.0-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Christopher Aillon <caillon@redhat.com> 2.8.0-1
- Update to 2.8.0

* Thu Jan 19 2006 Alexander Larsson <alexl@redhat.com> 2.4.0-3
- Mono now builds on s390x

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 2.4.0-2
- Fix vte build

* Tue Nov 15 2005 Alexander Larsson <alexl@redhat.com> - 2.4.0-1
- Initial version

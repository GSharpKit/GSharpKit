%define debug_package %{nil}

Name:           darwinx-gtk-sharp3
Version:        3.18.5
Release:        1%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtk-sharp.sf.net
Source0:        gtk-sharp-%{version}.tar.xz
Patch0:		gtk-sharp-2.99.3-marshaller.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-gtk3 >= 3.18.5
Requires: 	darwinx-mono >= 4.0

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-mono >= 4.0
BuildRequires:  automake, libtool
BuildRequires:	darwinx-gtk3 >= 3.18.5

BuildArch:	noarch

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

%prep
%setup -q -n gtk-sharp-%{version}
%patch0 -p1

%build
autoreconf --verbose --install -I /usr/darwinx/usr/share/aclocal
%{_darwinx_configure} --disable-static

%{_darwinx_make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{_darwinx_makeinstall} program_transform_name=""

%{__rm} -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/monodoc

%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/libatksharpglue-3.so
%{_darwinx_libdir}/libgtksharpglue-3.so
%{_darwinx_libdir}/libgiosharpglue-3.so
%{_darwinx_libdir}/libpangosharpglue-3.so
%{_darwinx_libdir}/mono/gac
%{_darwinx_libdir}/mono/gtk-sharp-3.0
%{_darwinx_bindir}/gapi3-codegen
%{_darwinx_bindir}/gapi3-fixup
%{_darwinx_bindir}/gapi3-parser
%dir %{_darwinx_libdir}/gapi-3.0
%{_darwinx_libdir}/gapi-3.0/gapi-fixup.exe
%{_darwinx_libdir}/gapi-3.0/gapi-parser.exe
%{_darwinx_libdir}/gapi-3.0/gapi2xml.pl
%{_darwinx_libdir}/gapi-3.0/gapi_codegen.exe
%{_darwinx_libdir}/gapi-3.0/gapi_pp.pl
%{_darwinx_datadir}/gapi-3.0/
%{_darwinx_libdir}/pkgconfig/gapi-3.0.pc
%{_darwinx_libdir}/pkgconfig/*-sharp-3.0.pc
%{_darwinx_libdir}/pkgconfig/gtk-dotnet-3.0.pc
%{_darwinx_libdir}/libatksharpglue-3.la
%{_darwinx_libdir}/libgtksharpglue-3.la
%{_darwinx_libdir}/libgiosharpglue-3.la
%{_darwinx_libdir}/libpangosharpglue-3.la
%{_darwinx_libdir}/libmono-profiler-gui-thread-check.0.dylib
%{_darwinx_libdir}/libmono-profiler-gui-thread-check.dylib
%{_darwinx_libdir}/libmono-profiler-gui-thread-check.la

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

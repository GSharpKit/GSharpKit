%{?mingw_package_header}

%global mingw_pkg_name gtk-sharp3
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:           mingw-gtk-sharp3
Version:        3.22.6
Release:        1%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtk-sharp.sf.net
Source0:        gtk-sharp-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  redhat-rpm-config
BuildRequires:  automake, libtool

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:	mingw32-gtk3
BuildRequires:	mingw64-gtk3
BuildRequires:  mingw32-mono >= 3.12
BuildRequires:  mingw64-mono >= 3.12

BuildRequires:  mono-devel >= 3.12

BuildArch:	noarch

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:	%{summary}
Requires:	mingw32-glib2
Requires:	mingw32-mono >= 3.12

%description -n mingw32-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

%package -n mingw32-%{mingw_pkg_name}-static
Summary:	Files needed for developing with gtk-sharp3
Group:		Development/Libraries
Requires:	mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-%{mingw_pkg_name}-static
This package provides the necessary development libraries and headers
for writing gtk-sharp3 applications.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-mono >= 3.12

%description -n mingw64-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        Files needed for developing with gtk-sharp3
Group:          Development/Libraries
Requires:       mingw64-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-%{mingw_pkg_name}-static
This package provides the necessary development libraries and headers
for writing gtk-sharp3 applications.



%prep
%setup -q -n gtk-sharp-%{version}


%build
sh autogen.sh --prefix=/usr
make distclean

sed -i -e 's!-define:WIN64LONGS!!g' configure
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}

#libtoolize --force --copy --install
#aclocal --install --force
#autoheader
#automake --add-missing --foreign
#autoconf --force --verbose -I /usr/i686-w64-mingw32/sys-root/mingw/share/aclocal/

%mingw_configure
%mingw_make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT

%mingw_make_install DESTDIR="$RPM_BUILD_ROOT" program_transform_name=""

# Libtool files don't need to be bundled
# Mingw32
find $RPM_BUILD_ROOT -name "*.la" -delete
find $RPM_BUILD_ROOT%{mingw32_libdir}/mono/gac/ -iname "*.dll.config" -delete

# Mingw64
find $RPM_BUILD_ROOT -name "*.la" -delete
find $RPM_BUILD_ROOT%{mingw64_libdir}/mono/gac/ -iname "*.dll.config" -delete


# Move dll to bin dir
# Mingw32
%{__mv} $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}/

%{__rm} -f $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-codegen
%{__rm} -f $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-fixup
%{__rm} -f $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-parser

%{__cp} $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0/gapi_codegen.exe $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-codegen.exe
%{__cp} $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0/gapi-fixup.exe $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-fixup.exe
%{__cp} $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0/gapi-parser.exe $RPM_BUILD_ROOT%{mingw32_bindir}/gapi3-parser.exe
%{__cp} $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0/gapi2xml.pl $RPM_BUILD_ROOT%{mingw32_bindir}/gapi2xml.pl
%{__cp} $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0/gapi_pp.pl $RPM_BUILD_ROOT%{mingw32_bindir}/gapi_pp.pl

%{__rm} -rf $RPM_BUILD_ROOT%{mingw32_libdir}/gapi-3.0
%{__rm} -rf $RPM_BUILD_ROOT%{mingw32_libdir}/monodoc

# Mingw64
%{__mv} $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}/

%{__rm} -f $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-codegen
%{__rm} -f $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-fixup
%{__rm} -f $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-parser

%{__cp} $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0/gapi_codegen.exe $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-codegen.exe
%{__cp} $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0/gapi-fixup.exe $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-fixup.exe
%{__cp} $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0/gapi-parser.exe $RPM_BUILD_ROOT%{mingw64_bindir}/gapi3-parser.exe
%{__cp} $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0/gapi2xml.pl $RPM_BUILD_ROOT%{mingw64_bindir}/gapi2xml.pl
%{__cp} $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0/gapi_pp.pl $RPM_BUILD_ROOT%{mingw64_bindir}/gapi_pp.pl

%{__rm} -rf $RPM_BUILD_ROOT%{mingw64_libdir}/gapi-3.0
%{__rm} -rf $RPM_BUILD_ROOT%{mingw64_libdir}/monodoc


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_bindir}/libatksharpglue-3.dll
%{mingw32_bindir}/libgtksharpglue-3.dll
%{mingw32_bindir}/libpangosharpglue-3.dll
%{mingw32_bindir}/libgiosharpglue-3.dll
%{mingw32_libdir}/mono/gac
%{mingw32_libdir}/mono/gtk-sharp-3.0

%{mingw32_bindir}/gapi3-codegen.exe
%{mingw32_bindir}/gapi3-fixup.exe
%{mingw32_bindir}/gapi3-parser.exe
%{mingw32_bindir}/gapi_pp.pl
%{mingw32_bindir}/gapi2xml.pl
%{mingw32_datadir}/gapi-3.0
%{mingw32_libdir}/pkgconfig/gapi-3.0.pc

%{mingw32_libdir}/pkgconfig/*-sharp-3.0.pc
%{mingw32_libdir}/pkgconfig/gtk-dotnet-3.0.pc
%{mingw32_libdir}/libatksharpglue-3.dll.a
%{mingw32_libdir}/libgtksharpglue-3.dll.a
%{mingw32_libdir}/libpangosharpglue-3.dll.a
%{mingw32_libdir}/libgiosharpglue-3.dll.a

%files -n mingw32-%{mingw_pkg_name}-static
%defattr(-,root,root,-)
%{mingw32_libdir}/libatksharpglue-3.a
%{mingw32_libdir}/libgtksharpglue-3.a
%{mingw32_libdir}/libpangosharpglue-3.a
%{mingw32_libdir}/libgiosharpglue-3.a


%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_bindir}/libatksharpglue-3.dll
%{mingw64_bindir}/libgtksharpglue-3.dll
%{mingw64_bindir}/libpangosharpglue-3.dll
%{mingw64_bindir}/libgiosharpglue-3.dll
%{mingw64_libdir}/mono/gac
%{mingw64_libdir}/mono/gtk-sharp-3.0

%{mingw64_bindir}/gapi3-codegen.exe
%{mingw64_bindir}/gapi3-fixup.exe
%{mingw64_bindir}/gapi3-parser.exe
%{mingw64_bindir}/gapi_pp.pl
%{mingw64_bindir}/gapi2xml.pl
%{mingw64_datadir}/gapi-3.0
%{mingw64_libdir}/pkgconfig/gapi-3.0.pc

%{mingw64_libdir}/pkgconfig/*-sharp-3.0.pc
%{mingw64_libdir}/pkgconfig/gtk-dotnet-3.0.pc
%{mingw64_libdir}/libatksharpglue-3.dll.a
%{mingw64_libdir}/libgtksharpglue-3.dll.a
%{mingw64_libdir}/libpangosharpglue-3.dll.a
%{mingw64_libdir}/libgiosharpglue-3.dll.a

%files -n mingw64-%{mingw_pkg_name}-static
%defattr(-,root,root,-)
%{mingw64_libdir}/libatksharpglue-3.a
%{mingw64_libdir}/libgtksharpglue-3.a
%{mingw64_libdir}/libpangosharpglue-3.a
%{mingw64_libdir}/libgiosharpglue-3.a



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

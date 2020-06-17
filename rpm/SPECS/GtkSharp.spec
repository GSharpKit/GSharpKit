%global debug_package %{nil}

%define libdir /lib

Name:           GtkSharp
Version:        3.22.25.98
Release:        33%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.mono-project.com/GtkSharp
Source0:        GtkSharp-%{version}.tar.gz
Source1:        gdk-sharp-3.0.pc
Source2:        glib-sharp-3.0.pc
Source3:        gio-sharp-3.0.pc
Source4:        gtk-sharp-3.0.pc
Source5:	GtkSharp.snk
Source100:	gapi3-codegen
Source101:	gapi3-fixup
Source102:	gapi3-parser 
Source103:	gapi-fixup.exe 
Source104:	gapi-parser.exe 
Source105:	gapi2xml.pl 
Source106:	gapi_codegen.exe 
Source107:	gapi_pp.pl
Source108:	gapi-3.0.pc
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  dotnet-sdk-2.2, gtk3-devel, cairo-devel, perl-XML-LibXML
BuildRequires:  meson

Obsoletes:	gtk-sharp3
Obsoletes:	gtk-sharp3-gapi
Obsoletes:	gtk-sharp3-devel

Provides:	gtk-sharp3
Provides:	gtk-sharp3-gapi
Provides:	gtk-sharp3-devel

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 armv4l sparcv9 alpha s390 s390x

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

%package gapi
Group:        Development/Languages
Summary:      Glib and GObject C source parser and C generator for the creation and maintenance of managed bindings for Mono and .NET
Requires:     perl-XML-LibXML-Common perl-XML-LibXML perl-XML-SAX

%description gapi
This package provides developer tools for the creation and
maintenance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk.

%prep
%setup -q

cp %{SOURCE5} Source/

# Fix permissions of source files
#find -name '*.c' -exec chmod a-x {} \;

sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs/GtkSharp/GtkSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GdkSharp/GdkSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GioSharp/GioSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GLibSharp/GLibSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//PangoSharp/PangoSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//CairoSharp/CairoSharp.csproj
sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//AtkSharp/AtkSharp.csproj


%build
sh build.sh

#pushd Source/OldStuff/parser/
#meson --prefix=%{_prefix} --libdir=%{_prefix}/lib build
#ninja -C build/
#popd


%install
%{__rm} -rf $RPM_BUILD_ROOT

sn -R BuildOutput/Release/AtkSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/AtkSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/CairoSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/CairoSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/GdkSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/GdkSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/GioSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/GioSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/GLibSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/GLibSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/GtkSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/GtkSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

sn -R BuildOutput/Release/PangoSharp.dll Source/GtkSharp.snk
gacutil -i BuildOutput/Release/PangoSharp.dll -package %{name}-3.0 -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

mkdir -p %{buildroot}%{_prefix}/share/pkgconfig
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/share/pkgconfig/
install -m 644 %{SOURCE2} %{buildroot}%{_prefix}/share/pkgconfig/
install -m 644 %{SOURCE3} %{buildroot}%{_prefix}/share/pkgconfig/
install -m 644 %{SOURCE4} %{buildroot}%{_prefix}/share/pkgconfig/
install -m 644 %{SOURCE108} %{buildroot}%{_prefix}/share/pkgconfig/

mkdir -p %{buildroot}%{_prefix}/share/gapi-3.0
cp Source/Libs/*/*Sharp-api.xml %{buildroot}%{_prefix}/share/gapi-3.0/

mkdir -p %{buildroot}%{_prefix}/bin
install -m 755 %{SOURCE100} %{buildroot}%{_prefix}/bin/
install -m 755 %{SOURCE101} %{buildroot}%{_prefix}/bin/
install -m 755 %{SOURCE102} %{buildroot}%{_prefix}/bin/

mkdir -p %{buildroot}%{_prefix}/lib/gapi-3.0
install -m 755 %{SOURCE103} %{buildroot}%{_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE104} %{buildroot}%{_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE105} %{buildroot}%{_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE106} %{buildroot}%{_prefix}/lib/gapi-3.0/
install -m 755 %{SOURCE107} %{buildroot}%{_prefix}/lib/gapi-3.0/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_prefix}/lib/mono/gac
%{_prefix}/lib/mono/GtkSharp-3.0
%{_prefix}/lib/mono/gac/*Sharp/*/*.dll
%{_prefix}/lib/mono/gac/*Sharp/*/*.pdb
%{_prefix}/share/pkgconfig/*-sharp-3.0.pc

%files gapi
%defattr(-,root,root,-)
%dir %{_prefix}/lib/gapi-3.0
%{_bindir}/gapi3-codegen
%{_bindir}/gapi3-fixup
%{_bindir}/gapi3-parser
%{_prefix}/lib/gapi-3.0/gapi_codegen.exe
%{_prefix}/lib/gapi-3.0/gapi-fixup.exe
%{_prefix}/lib/gapi-3.0/gapi-parser.exe
%{_prefix}/lib/gapi-3.0/gapi_pp.pl
%{_prefix}/lib/gapi-3.0/gapi2xml.pl
%{_datadir}/gapi-3.0
%{_prefix}/share/pkgconfig/gapi-3.0.pc

%changelog
* Thu Oct 28 2010 Christian Krause <chkr@fedoraproject.org> - 2.12.10-4
- Rebuild again to create correct requires/provides capabilities

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.12.10-4
- Rebuild for new mono
- Alter exported CAIRO_LIB to 2.0

* Mon Apr 05 2010 Christian Krause <chkr@fedoraproject.org> - 2.12.10-3
- Add missing BR monodoc

* Mon Apr 05 2010 Christian Krause <chkr@fedoraproject.org> - 2.12.10-2
- Fix monodoc integration (#550144)

* Fri Apr 02 2010 Christian Krause <chkr@fedoraproject.org> - 2.12.10-1
- Update to new upstream version
- Minor spec file cleanup

* Wed Sep 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.12.9-1
- Bump to newer version
- Fixed doc patch
- Spec file cleanup

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Xavier lamien <laxathom@fedoraproject.org> - 2.12.7-5
- Build ppc64.

* Tue May 12 2009 Karsten Hopp <karsten@redhat.com> 2.12.7-4.1
- mono is available on s390(x)

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

* Wed Feb 27 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.10.3-1
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

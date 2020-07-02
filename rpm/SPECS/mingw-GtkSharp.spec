%{?mingw_package_header}

%global mingw_pkg_name GtkSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-GtkSharp
Version:        3.22.25.98
Release:        2%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://github.com/GtkSharp/GtkSharp
Source0:        GtkSharp-%{version}.tar.gz
Source1:        mingw-gdk-sharp-3.0.pc
Source2:        mingw-glib-sharp-3.0.pc
Source3:        mingw-gio-sharp-3.0.pc
Source4:        mingw-gtk-sharp-3.0.pc
Source5:	GtkSharp.snk

Patch0:		revert-cdecl.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  redhat-rpm-config
BuildRequires:  meson

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

BuildRequires: dotnet-sdk-2.2 

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
Requires:	mingw32-gtk3

Obsoletes:	mingw32-gtk-sharp3
Provides:	mingw32-gtk-sharp3

%description -n mingw32-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-gtk3

Obsoletes:      mingw64-gtk-sharp3
Provides:       mingw64-gtk-sharp3

%description -n mingw64-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

%prep
%setup -q -n GtkSharp-%{version}
%patch0 -p1

cp %{SOURCE5} Source/

#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs/GtkSharp/GtkSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GdkSharp/GdkSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GioSharp/GioSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//GLibSharp/GLibSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//PangoSharp/PangoSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//CairoSharp/CairoSharp.csproj
#sed -i -e 's!</PackageTags>!</PackageTags><SignAssembly>true</SignAssembly><AssemblyOriginatorKeyFile>../../GtkSharp.snk</AssemblyOriginatorKeyFile>!g' Source/Libs//AtkSharp/AtkSharp.csproj

%build
sh build.sh

%install
%{__rm} -rf $RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -m 644 BuildOutput/Release/AtkSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/CairoSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/GdkSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/GioSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/GLibSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/GtkSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 BuildOutput/Release/PangoSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

mkdir -p %{buildroot}%{mingw32_prefix}/share/pkgconfig
install -m 644 %{SOURCE1} %{buildroot}%{mingw32_prefix}/share/pkgconfig/gdk-sharp-3.0.pc
install -m 644 %{SOURCE2} %{buildroot}%{mingw32_prefix}/share/pkgconfig/glib-sharp-3.0.pc
install -m 644 %{SOURCE3} %{buildroot}%{mingw32_prefix}/share/pkgconfig/gio-sharp-3.0.pc
install -m 644 %{SOURCE4} %{buildroot}%{mingw32_prefix}/share/pkgconfig/gtk-sharp-3.0.pc

sed -i -e 's!@PREFIX@!%{mingw32_prefix}!g' %{buildroot}%{mingw32_prefix}/share/pkgconfig/*.pc

mkdir -p %{buildroot}%{mingw32_prefix}/share/gapi-3.0
cp Source/Libs/*/*Sharp-api.xml %{buildroot}%{mingw32_prefix}/share/gapi-3.0/


# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -m 644 BuildOutput/Release/AtkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/CairoSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/GdkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/GioSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/GLibSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/GtkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 BuildOutput/Release/PangoSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

mkdir -p %{buildroot}%{mingw64_prefix}/share/pkgconfig
install -m 644 %{SOURCE1} %{buildroot}%{mingw64_prefix}/share/pkgconfig/gdk-sharp-3.0.pc
install -m 644 %{SOURCE2} %{buildroot}%{mingw64_prefix}/share/pkgconfig/glib-sharp-3.0.pc
install -m 644 %{SOURCE3} %{buildroot}%{mingw64_prefix}/share/pkgconfig/gio-sharp-3.0.pc
install -m 644 %{SOURCE4} %{buildroot}%{mingw64_prefix}/share/pkgconfig/gtk-sharp-3.0.pc

sed -i -e 's!@PREFIX@!%{mingw64_prefix}!g' %{buildroot}%{mingw64_prefix}/share/pkgconfig/*.pc

mkdir -p %{buildroot}%{mingw64_prefix}/share/gapi-3.0
cp Source/Libs/*/*Sharp-api.xml %{buildroot}%{mingw64_prefix}/share/gapi-3.0/


%clean
#%{__rm} -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/*Sharp.dll
%{mingw32_datadir}/pkgconfig/*-sharp-3.0.pc
%{mingw32_datadir}/gapi-3.0

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*Sharp.dll
%{mingw64_datadir}/pkgconfig/*-sharp-3.0.pc
%{mingw64_datadir}/gapi-3.0


%changelog
* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.22.6-1
- Updated to Meson build system
 
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

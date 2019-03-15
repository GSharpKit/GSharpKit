%{?mingw_package_header}

%global mingw_pkg_name dbus-sharp-glib
%global mingw_build_win32 1
%global mingw_build_win64 1

%define libdir /bin

%define debug_package %{nil}

Name:		mingw-dbus-sharp-glib
URL:		http://www.ndesk.org/DBusSharp
License:	MIT
Group:		Development/Libraries
Version:	0.6.0
Release:	1%{?dist}
Summary:	Provides glib mainloop integration for dbus-sharp
Source0:	http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-glib-%{version}.tar.gz
Source1:	autogen.sh
Patch0:		ndesk-dbus-glib-0.4.2.patch
Patch1:         dbus-sharp-glib-0.6.0-mcs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch
BuildRequires:	mono-core 
BuildRequires:	mono-devel
BuildRequires:	mingw32-dbus-sharp

%description
dbus-sharp-glib provides glib mainloop integration for dbus-sharp

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2

%description -n mingw32-%{mingw_pkg_name}
dbus-sharp-glib provides glib mainloop integration for dbus-sharp

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2

%description -n mingw64-%{mingw_pkg_name}
dbus-sharp-glib provides glib mainloop integration for dbus-sharp

%prep
%setup -q -n dbus-sharp-glib-%{version}
%patch0 -p1
%patch1 -p1

%build
cp %{SOURCE1} .
sh autogen.sh
%mingw_configure

find . -name Makefile | while read f ;
         do
           sed -i -e 's!GMCS = /usr/x86_64-w64-mingw32/sys-root/mingw/bin/gmcs!GMCS = /usr/bin/mcs!' "$f"
           sed -i -e 's!GMCS = /usr/i686-w64-mingw32/sys-root/mingw/bin/gmcs!GMCS = /usr/bin/mcs!' "$f"
         done

%mingw_make

%install
rm -rf $RPM_BUILD_ROOT
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw32_libdir}/mono/gac/dbus-sharp-glib/*/*.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/dbus-sharp-glib-2.0.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
sed -i -e 's!/usr/i686-w64-mingw32/sys-root/mingw/lib!/usr/i686-w64-mingw32/sys-root/mingw/bin!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc
sed -i -e 's!/mono/dbus-sharp-glib-2.0!!' $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 $RPM_BUILD_ROOT%{mingw64_libdir}/mono/gac/dbus-sharp-glib/*/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/dbus-sharp-glib-2.0.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
sed -i -e 's!/usr/x86_64-w64-mingw32/sys-root/mingw/lib!/usr/x86_64-w64-mingw32/sys-root/mingw/bin!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc
sed -i -e 's!/mono/dbus-sharp-glib-2.0!!' $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/*.dll
%{mingw32_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc


%changelog
* Sat May 30 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.4.1-5
- Build arch ppc64.

* Thu Feb 26 2009 David Nielsen <dnielsen@fedoraproject.org> - 0.4.1-4
- Rebuild for stack update (#487155)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-3
- Autorebuild for GCC 4.3

* Sat Dec 29 2007 David Nielsen <david@lovesunix.net> - 0.4.1-2
- -devel now requires ndesk-dbus-devel

* Thu Nov  8 2007 David Nielsen <david@lovesunix.net> - 0.4.1-1
- bump to 0.4.1
- clean up spec
- remove review blockers

* Sun Oct 21 2007 David Nielsen <david@lovesunix.net> - 0.3-7
- revert noarch change accord to the guidelines to accommodate
- post packaging AOT.

* Tue Oct 16 2007 David Nielsen <david@lovesunix.net> - 0.3-6
- Make noarch

* Thu Jul  5 2007 David Nielsen <david@lovesunix.net> - 0.3-5
- Don't build on ppc64 due to mising deps, see bug 241850

* Wed Jul  4 2007 David Nielsen <david@lovesunix.net> - 0.3-4
- fix spaces vs. tabs
- fix %%defattr
- No longer build as noarch
- make setup quiet

* Mon Jun 25 2007 David Nielsen <david@lovesunix.net> - 0.3-3
- reduced amount of ugly hacks in the spec

* Mon Jun 25 2007 David Nielsen <david@lovesunix.net> - 0.3-2
- Let's not be stupid .mdb files don't go in -devel

* Sat Jun 23 2007 David Nielsen <david@lovesunix.net> - 0.3-1
- Initial package

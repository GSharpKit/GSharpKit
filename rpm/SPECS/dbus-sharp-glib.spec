%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

%define pkg_version 0.6

Name:		dbus-sharp-glib
URL:		http://www.ndesk.org/DBusSharp
License:	MIT
Group:		Development/Libraries
Version:	0.6.0
Release:	10%{?dist}
Summary:	Provides glib mainloop integration for dbus-sharp
Source0:	https://github.com/mono/dbus-sharp-glib/releases/dbus-sharp-glib-%{pkg_version}.tar.gz
#Patch0:	dbus-sharp-glib-0.6-nosystembus.patch
Patch1:		dbus-sharp-glib-0.6-mcs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch: 	noarch

BuildRequires:	mono-core 
BuildRequires:	mono-devel
BuildRequires:	dbus-sharp >= 2:0.9.1

Requires:       dbus-sharp >= 2:0.9.1

Obsoletes:      dbus-sharp-glib-devel
Provides:       dbus-sharp-glib-devel

Obsoletes:      ndesk-dbus-glib
Obsoletes:      ndesk-dbus-glib-devel

%description
dbus-sharp-glib provides glib mainloop integration for dbus-sharp

%prep
%setup -q -n dbus-sharp-glib-%{pkg_version}
#patch0 -p1
%patch1 -p1

sed -i -e 's!libglib-2.0-0.dll!libglib-2.0.so.0!g' src/GLib.IO.cs 

%build
sh autogen.sh
./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
mv $RPM_BUILD_ROOT%{prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
sed -i -e 's!mono/dbus-sharp-glib-2.0/!!g' $RPM_BUILD_ROOT%{_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc
rm -rf $RPM_BUILD_ROOT%{prefix}/lib/pkgconfig

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
mv $RPM_BUILD_ROOT%{prefix}/lib/mono/gac/dbus-sharp-glib/*/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
rm -rf $RPM_BUILD_ROOT%{prefix}/lib/mono

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{prefix}/lib/dbus-sharp-glib.dll
%{_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

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

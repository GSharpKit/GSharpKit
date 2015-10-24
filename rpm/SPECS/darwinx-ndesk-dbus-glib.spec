Name:		darwinx-ndesk-dbus-glib
URL:		http://www.ndesk.org/DBusSharp
License:	MIT
Group:		Development/Libraries
Version:	0.4.2
Release:	3%{?dist}
Summary:	Provides glib mainloop integration for ndesk-dbus
Source0:	http://www.ndesk.org/archive/dbus-sharp/ndesk-dbus-glib-%{version}.tar.bz2
Source1:        autogen.sh
Patch0:		ndesk-dbus-glib-0.4.2.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

BuildRequires:	darwinx-mono 
BuildRequires:	darwinx-ndesk-dbus

%description
ndesk-dbus-glib provides glib mainloop integration for ndesk-dbus

%prep
%setup -q -n ndesk-dbus-glib-%{version}
%patch0 -p1

# Fix dll.config
sed -i '' 's|libglib-2.0.so.0|libglib-2.0.0.dylib|g' src/NDesk.DBus.GLib.dll.config

%build
cp %{SOURCE1} .
sh autogen.sh
%{_darwinx_configure}
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT
%{_darwinx_makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_darwinx_libdir}/mono/gac/NDesk.DBus.GLib/*/*.dll
%{_darwinx_libdir}/mono/gac/NDesk.DBus.GLib/*/*.dll.config
%{_darwinx_libdir}/mono/ndesk-dbus-glib-1.0/
%{_darwinx_libdir}/mono/gac/NDesk.DBus.GLib/*/*.dll.mdb
%{_darwinx_libdir}/pkgconfig/ndesk-dbus-glib-1.0.pc

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

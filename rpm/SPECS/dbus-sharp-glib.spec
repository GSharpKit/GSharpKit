Name:		dbus-sharp-glib
URL:		http://www.ndesk.org/DBusSharp
License:	MIT
Group:		Development/Libraries
Version:	0.6.0
Release:	3%{?dist}
Summary:	Provides glib mainloop integration for dbus-sharp
Source0:	http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-glib-%{version}.tar.gz
Source1:	autogen.sh
Patch0:		ndesk-dbus-glib-0.4.2.patch
Patch1:		dbus-sharp-glib-0.6.0-mcs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch: 	noarch

BuildRequires:	mono-core 
BuildRequires:	mono-devel
BuildRequires:	dbus-sharp >= 1:0.8.0

Requires:       dbus-sharp >= 1:0.8.0

Obsoletes:      dbus-sharp-glib-devel
Provides:       dbus-sharp-glib-devel

Obsoletes:      ndesk-dbus-glib
Obsoletes:      ndesk-dbus-glib-devel

%description
dbus-sharp-glib provides glib mainloop integration for dbus-sharp

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp %{SOURCE1} .
sh autogen.sh
./configure --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pkgconfig
mv $RPM_BUILD_ROOT%{prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{prefix}/lib/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{prefix}/lib/mono/gac/dbus-sharp-glib/
%{prefix}/lib/mono/dbus-sharp-glib-2.0/
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

Name:		darwinx-dbus-sharp-glib
URL:		http://www.ndesk.org/DBusSharp
License:	MIT
Group:		Development/Libraries
Version:	0.6.0
Release:	3%{?dist}
Summary:	Provides glib mainloop integration for ndesk-dbus
Source0:	http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-glib-%{version}.tar.gz
Patch0:		ndesk-dbus-glib-0.4.2.patch
Patch1:		dbus-sharp-glib-0.6.0-mcs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

BuildRequires:	darwinx-dbus-sharp

Requires:  	darwinx-dbus-sharp


Obsoletes:	darwinx-ndes-dbus-glib

%description
ndesk-dbus-glib provides glib mainloop integration for ndesk-dbus

%prep
%setup -q -n dbus-sharp-glib-%{version}
%patch0 -p1
%patch1 -p1

# Fix dll.config
sed -i '' 's|libglib-2.0.so.0|libglib-2.0.0.dylib|g' src/dbus-sharp-glib.dll.config

%build
%{_darwinx_configure}
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT
#{_darwinx_makeinstall}

mkdir -p $RPM_BUILD_ROOT%{_darwinx_libdir}
cp src/dbus-sharp-glib.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/
cp src/dbus-sharp-glib.dll.config $RPM_BUILD_ROOT%{_darwinx_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
cp dbus-sharp-glib-2.0.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
sed -i '' 's!mono/dbus-sharp-glib-2.0/!!g' $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/dbus-sharp-glib.dll
%{_darwinx_libdir}/dbus-sharp-glib.dll.config
%{_darwinx_datadir}/pkgconfig/dbus-sharp-glib-2.0.pc

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

Name:			darwinx-dbus-sharp
Epoch:			2
Version:		0.9.2
Release:		3%{?dist}
Summary:		Managed C# implementation of DBus
License:		MIT
Group:			System Environment/Libraries
URL:			http://www.ndesk.org/DBusSharp
Source0:		http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 		noarch

BuildRequires:		darwinx-mono-core

Obsoletes:		darwinx-ndesk-dbus

%description
Managed C# implementation of DBus

%prep
%setup -q -n dbus-sharp-%{version}

%build
%{_darwinx_env} ; sh autogen.sh --prefix=%{_darwinx_prefix}
%{_darwinx_configure}
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT
#{_darwinx_makeinstall}

mkdir -p $RPM_BUILD_ROOT%{_darwinx_libdir}
cp src/dbus-sharp.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
cp dbus-sharp-2.0.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
sed -i '' 's!mono/dbus-sharp-2.0/!!g' $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/dbus-sharp-2.0.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/dbus-sharp.dll
%{_darwinx_datadir}/pkgconfig/dbus-sharp-2.0.pc

%changelog
* Sat May 30 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.6-1a-6
- Fix pkconfig.

* Fri May 29 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.6-1a-5
- Build arch ppc64.

* Thu Feb 26 2009 David Nielsen <dnielsen@fedoraproject.org> - 0.6.1a-4
- Rebuild for stack update (#487155)

* Tue Dec 30 2008 Caolán McNamara <caolanm@redhat.com> - 0.6.1a-3
- rebuild to get provides pkgconfig(ndesk-dbus-1.0)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.1a-2
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 David Nielsen <david@lovesunix.net> - 0.6.1a-1
- Bump to 0.6.1a

* Thu Nov  8 2007 David Nielsen <david@lovesunix.net> - 0.6.0-1
- bump to 0.6.0 
- clean up spec
- upstream is now officially renamed to ndesk-dbus as promised

* Sun Oct 21 2007 David Nielsen <david@lovesunix.net> - 0-5.2-12
- revert noarch change accord to the guidelines to accommodate
- post packaging AOT.

* Tue Oct 16 2007 David Nielsen <david@lovesunix.net> - 0.5.2-11
- Make noarch
- Don't obsolete dbus-sharp - they can coexist peacefully

* Sat Jul  7 2007 David Nielsen <david@lovesunix.net> - 0.5.2-10
- Obsolete dbus-sharp-devel as well, thanks Michael Schwendt

* Fri Jul  6 2007 David Nielsen <david@lovesunix.net> - 0.5.2-9
- And let's not be stupid and add the EVR for that provides

* Fri Jul  6 2007 David Nielsen <david@lovesunix.net> - 0.5.2-8
- Provide mono(dbus-sharp)

* Thu Jul  5 2007 David Nielsen <david@lovesunix.net> - 0.5.2-7
- Don't build on ppc64 due to mising deps, see bug 241850

* Wed Jul  4 2007 David Nielsen <david@lovesunix.net> - 0.5.2-6
- more provides, obsoletes adjustments
- %%defattr corrections
- Happy 4th of July America

* Sun Jul  1 2007 David Nielsen <david@lovesunix.net> - 0.5.2-5
- Remove mono-core from BR as it was not the cause of the mock breakage
- fix tab vs spaces
- Fix summeries
- don't use macros in changelog anymore.. upsie

* Fri Jun 29 2007 David Nielsen <david@lovesunix.net> - 0.5.2-4
- Add BuildRequires for mono-core to fix building in mock
- Fix Requires for the -devel package
- Make %%setup a bit quieter
- Made package no longer be noarch
- Added COPYING as documentation for the -devel package

* Mon Jun 26 2007 David Nielsen <david@lovesunix.net> - 0.5.2-3
- Make this significantly less hacky

* Mon Jun 25 2007 David Nielsen <david@lovesunix.net> - 0.5.2-2
- Don't be stupid .mdb files don't go in -devel

* Sat Jun 23 2007 David Nielsen <david@lovesunix.net> - 0.5.2-1
- Initial package

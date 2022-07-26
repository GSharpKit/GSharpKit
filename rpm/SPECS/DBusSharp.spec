%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:			DBusSharp
Epoch: 			3
Version:		0.11.0
Release:		1%{?dist}
Summary:		Managed C# implementation of DBus
License:		MIT
Group:			System Environment/Libraries
URL:			http://www.ndesk.org/DBusSharp
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:			/usr

BuildArch: 		noarch
AutoReqProv:    	no

BuildRequires:		nuget

Obsoletes:              dbus-sharp-devel
Obsoletes:		ndesk-dbus
Obsoletes:              ndesk-dbus-devel

Provides:		dbus-sharp dbus-sharp-devel

%description
Managed C# implementation of DBus

%prep
%setup -c %{name}-%{version} -T
nuget install Tmds.DBus -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Tmds.DBus.%{version}/lib/netstandard2.0/Tmds.DBus.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{prefix}/lib/Tmds.DBus.dll

%changelog
* Mon Dec 14 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.1-1
- Update to Tmds.DBus

* Wed Oct 04 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.1-1
- Updated to 0.9.1 with MSBuild

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

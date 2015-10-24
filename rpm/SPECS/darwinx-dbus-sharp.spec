Name:			darwinx-dbus-sharp
Version:		0.9.0
Release:		1%{?dist}
Summary:		Managed C# implementation of DBus
License:		MIT
Group:			System Environment/Libraries
URL:			http://www.ndesk.org/DBusSharp
Source0:		http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-%{version}.tar.xz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 		noarch

BuildRequires:		darwinx-mono
Requires:		darwinx-mono

Obsoletes:		darwinx-ndesk-dbus

%description
Managed C# implementation of DBus

%prep
%setup -q -n dbus-sharp-%{version}

%build
%{_darwinx_configure}
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT
%{_darwinx_makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/mono/dbus-sharp-2.0/
%{_darwinx_libdir}/mono/gac/dbus-sharp/
%{_darwinx_libdir}/pkgconfig/dbus-sharp-2.0.pc

%changelog
* Sat Jun 23 2007 David Nielsen <david@lovesunix.net> - 0.5.2-1
- Initial package

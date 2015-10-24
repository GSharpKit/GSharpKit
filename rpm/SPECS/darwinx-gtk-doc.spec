Name:		darwinx-gtk-doc
Version:	1.20
Release:	1%{?dist}
Summary:	Darwin API to integrate GTK+ OS X applications with the Mac desktop

License:	LGPLv2
Group:		Development/Libraries
URL:		https://download.gnome.org/sources/gtk-doc/1.20/
Source0:	gtk-doc-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-filesystem >= 13
BuildRequires:	darwinx-gtk3

Requires:       darwinx-gtk3

%description
API to integrate GTK+ OS X applications with the Mac desktop.


%prep
%setup -q -n gtk-doc-%{version}

%build
%{_darwinx_configure}
%{_darwinx_make} %{?_smp_mflags} V=99


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_makeinstall}


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%{_darwinx_includedir}/gtkmacintegration/
%{_darwinx_libdir}/libgtkmacintegration.2.dylib
%{_darwinx_libdir}/libgtkmacintegration.dylib
%{_darwinx_libdir}/libgtkmacintegration.la
%dir %{_darwinx_datadir}/strings
%{_darwinx_datadir}/strings/*
%{_darwinx_libdir}/pkgconfig/gtk-mac-integration.pc

%changelog
* Thu May 20 2014 Mikkel Kruse Johnsen <mikkel@linet.dk> - 1.20-1
- Initial release


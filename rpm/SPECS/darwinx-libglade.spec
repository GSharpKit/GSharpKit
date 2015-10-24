%define debug_package %{nil}

Name:           darwinx-libglade2
Version:        2.6.4
Release:        1%{?dist}
Summary:        GTK+ and GNOME bindings for Mono

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://libglade.sf.net
Source0:        libglade-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-gtk2
BuildRequires:	darwinx-gtk2

BuildArch:	noarch

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

%prep
%setup -q -n libglade-%{version}

%build
%{_darwinx_configure} --disable-static

%{_darwinx_make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{_darwinx_makeinstall} program_transform_name=""


%{__rm} -rf $RPM_BUILD_ROOT%{_darwinx_bindir}
%{__rm} -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_libdir}/libglade-2.0.0.0.7.dylib
%{_darwinx_libdir}/libglade-2.0.0.dylib
%{_darwinx_libdir}/libglade-2.0.dylib
%{_darwinx_libdir}/libglade-2.0.la
%{_darwinx_libdir}/pkgconfig/libglade-2.0.pc
%{_darwinx_includedir}/libglade-2.0

%changelog
* Thu Apr 17 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.6.4-1
- Initial version

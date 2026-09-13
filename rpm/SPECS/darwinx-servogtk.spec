%define version 0.5.0

Name:           darwinx-servogtk
License:        Mozilla Public License Version 2.0
Group:          System Environment/Base 
Version:        %{version}
Release:        2%{?dist}
Url:		https://github.com/GSharpKit/servo-gtk
Summary:        Servo Gtk3/4
Source0:        servogtk-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:	darwinx-gtk3 darwinx-gtk4
#Requires:	rust >= 1.96 cargo >= 1.96

%description
ServoGTK is the wrapping of the portable web rendering engine Servo written 
in Rust to the GTK platform.

%prep
%setup -qn "servogtk-%{version}"

%build
make clean
make darwinx

%install
rm -rf %{buildroot}
PREFIX=%{buildroot} make install-darwinx
#rm -f %{buildroot}%{darwinx_libdir}/libservogtk3.dll.a
#rm -f %{buildroot}%{darwinx_libdir}/libservogtk4.dll.a

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{darwinx_libdir}/libservoshell.0.dylib
%{darwinx_libdir}/libservoshell.0.5.0.dylib
%{darwinx_libdir}/libservoshell.dylib

%{darwinx_bindir}/servogtk3-demo
%{darwinx_libdir}/libservogtk3.dylib
%{darwinx_libdir}/libservogtk3.*.dylib
%dir %{darwinx_includedir}/servogtk3
%{darwinx_includedir}/servogtk3/servo-gtk3-view.h
%{darwinx_includedir}/servogtk3/servo-webview.h
%{darwinx_libdir}/pkgconfig/servogtk3.pc

%{darwinx_bindir}/servogtk4-demo
%{darwinx_libdir}/libservogtk4.dylib
%{darwinx_libdir}/libservogtk4.*.dylib
%dir %{darwinx_includedir}/servogtk4
%{darwinx_includedir}/servogtk4/servo-gtk4-view.h
%{darwinx_includedir}/servogtk4/servo-webview.h
%{darwinx_libdir}/pkgconfig/servogtk4.pc

%changelog
* Mon Aug 17 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- First RPM package


%undefine _hardened_build

Name:           servogtk
License:        Mozilla Public License Version 2.0
Group:          System Environment/Base 
Version:        0.3.0
Release:        1%{?dist}
Url:		https://github.com/GSharpKit/servo-gtk
Summary:        Servo Gtk3/4
Source0:        servogtk-0.3.0.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64

Requires:	gtk3 gtk3-devel gtk4 gtk4-devel
Requires:	rust >= 1.96 cargo >= 1.96

%description
ServoGTK is the wrapping of the portable web rendering engine Servo written 
in Rust to the GTK platform.

%prep
%setup -q

%build
export LDFLAGS="%{build_ldflags} -Wl,--no-as-needed"
make linux

%install
rm -rf %{buildroot}
PREFIX=%{buildroot} make install-linux

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/lib64/libservoshell.so*

/usr/lib64/libservogtk3.so*
%{_bindir}/servogtk3-demo
%dir %{_includedir}/servogtk3
%{_includedir}/servogtk3/servo-gtk3-view.h
%{_includedir}/servogtk3/servo-webview.h
%{_datadir}/gir-1.0/ServoGtk-3.0.gir
%{_libdir}/girepository-1.0/ServoGtk-3.0.typelib
/usr/lib64/pkgconfig/servogtk3.pc

/usr/lib64/libservogtk4.so*
%{_bindir}/servogtk4-demo
%dir %{_includedir}/servogtk4
%{_includedir}/servogtk4/servo-gtk4-view.h
%{_includedir}/servogtk4/servo-webview.h
%{_datadir}/gir-1.0/ServoGtk-4.0.gir
%{_libdir}/girepository-1.0/ServoGtk-4.0.typelib
/usr/lib64/pkgconfig/servogtk4.pc

%changelog
* Wed Jul 15 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- First RPM package


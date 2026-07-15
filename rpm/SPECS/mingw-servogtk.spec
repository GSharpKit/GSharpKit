%undefine _hardened_build

%{?mingw_package_header}

%global mingw_build_win32 0
%global mingw_build_win64 1
%global debug_package %{nil}

%define version 0.3.0

Name:           mingw-servogtk
License:        Mozilla Public License Version 2.0
Group:          System Environment/Base 
Version:        %{version}
Release:        1%{?dist}
Url:		https://github.com/GSharpKit/servo-gtk
Summary:        Servo Gtk3/4
Source0:        servogtk-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      x86_64

Requires:	gtk3 gtk3-devel gtk4 gtk4-devel
Requires:	rust >= 1.96 cargo >= 1.96

%description
ServoGTK is the wrapping of the portable web rendering engine Servo written 
in Rust to the GTK platform.

%package -n mingw64-servogtk
Summary:        Servo Gtk3/4

%description -n mingw64-servogtk
ServoGTK is the wrapping of the portable web rendering engine Servo written
in Rust to the GTK platform.

%prep
%setup -qn "servogtk-%{version}"

%build
unset CFLAGS
unset CXXFLAGS
unset CPPFLAGS
unset LDFLAGS
export LDFLAGS="%{build_ldflags} -Wl,--no-as-needed"
make mingw

%install
rm -rf %{buildroot}
PREFIX=%{buildroot} make install-mingw
rm -f %{buildroot}%{mingw64_libdir}/libservogtk3.dll.a
rm -f %{buildroot}%{mingw64_libdir}/libservogtk4.dll.a

%clean
rm -rf %{buildroot}

%files -n mingw64-servogtk
%defattr(-,root,root)
%{mingw64_bindir}/libservoshell.dll

%{mingw64_bindir}/libservogtk3.dll
%{mingw64_bindir}/servogtk3-demo.exe
%dir %{mingw64_includedir}/servogtk3
%{mingw64_includedir}/servogtk3/servo-gtk3-view.h
%{mingw64_includedir}/servogtk3/servo-webview.h
%{mingw64_libdir}/pkgconfig/servogtk3.pc

%{mingw64_bindir}/libservogtk4.dll
%{mingw64_bindir}/servogtk4-demo.exe
%dir %{mingw64_includedir}/servogtk4
%{mingw64_includedir}/servogtk4/servo-gtk4-view.h
%{mingw64_includedir}/servogtk4/servo-webview.h
%{mingw64_libdir}/pkgconfig/servogtk4.pc

%changelog
* Wed Jul 15 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- First RPM package


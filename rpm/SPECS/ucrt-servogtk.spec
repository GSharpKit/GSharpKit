%undefine _hardened_build

%{?ucrt_package_header}

%global debug_package %{nil}

%define version 0.5.0

Name:           ucrt-servogtk
License:        Mozilla Public License Version 2.0
Group:          System Environment/Base 
Version:        %{version}
Release:        2%{?dist}
Url:		https://github.com/GSharpKit/servo-gtk
Summary:        Servo Gtk3/4
Source0:        servogtk-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:	gtk3 gtk3-devel gtk4 gtk4-devel
Requires:	rust >= 1.96 cargo >= 1.96

%description
ServoGTK is the wrapping of the portable web rendering engine Servo written 
in Rust to the GTK platform.

%package -n ucrt64-servogtk
Summary:        Servo Gtk3/4

%description -n ucrt64-servogtk
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
unset RUSTFLAGS
unset CARGO_ENCODED_RUSTFLAGS
export CARGO_TARGET_X86_64_PC_WINDOWS_MSVC_RUSTFLAGS="-C opt-level=3 -C debuginfo=0 -C codegen-units=4 -C strip=debuginfo"
make clean
make ucrt

%install
rm -rf %{buildroot}
PREFIX=%{buildroot} make install-ucrt
rm -f %{buildroot}%{ucrt64_libdir}/libservogtk3.dll.a
rm -f %{buildroot}%{ucrt64_libdir}/libservogtk4.dll.a

%clean
rm -rf %{buildroot}

%files -n ucrt64-servogtk
%defattr(-,root,root)
%{ucrt64_bindir}/libservoshell.dll

%{ucrt64_bindir}/libservogtk3.dll
%{ucrt64_bindir}/servogtk3-demo.exe
%dir %{ucrt64_includedir}/servogtk3
%{ucrt64_includedir}/servogtk3/servo-gtk3-view.h
%{ucrt64_includedir}/servogtk3/servo-webview.h
%{ucrt64_libdir}/pkgconfig/servogtk3.pc

%{ucrt64_bindir}/libservogtk4.dll
%{ucrt64_bindir}/servogtk4-demo.exe
%dir %{ucrt64_includedir}/servogtk4
%{ucrt64_includedir}/servogtk4/servo-gtk4-view.h
%{ucrt64_includedir}/servogtk4/servo-webview.h
%{ucrt64_libdir}/pkgconfig/servogtk4.pc

%changelog
* Wed Jul 15 2026 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- First RPM package


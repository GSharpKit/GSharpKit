%define debug_package %{nil}

%define libdir /lib

Name:		GstSharp
Version: 	1.18.2
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		https://www.nuget.org/packages/GstSharp/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch
Source:		gstreamer-sharp-%{version}.tar.xz
BuildRequires:	nuget

Requires:       mono-core >= 6.12
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base

BuildRequires:	gst-editing-services-devel gstreamer1-plugins-bad-free-devel

Obsoletes:	gstreamer1-sharp
Provides:	gstreamer1-sharp

Obsoletes:	gstreamer1-sharp-devel
Provides:	gstreamer1-sharp-devel

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gstreamer-sharp-%{version}

cat > gstreamer-sharp-1.0.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -r:${libdir}/gstreamer-sharp.dll
Requires: glib-sharp-3.0
EOF

%build
meson . build

cp /usr/lib/AtkSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/CairoSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/GLibSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/GdkSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/GioSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/GtkSharp.dll build/subprojects/gtk-sharp/
cp /usr/lib/PangoSharp.dll build/subprojects/gtk-sharp/

ninja -C build || true

%install
%{__rm} -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 build/sources/gstreamer-sharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 build/sources/gstreamer-sharp.dll.config $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 %{buildroot}%{_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc %{buildroot}%{_prefix}/share/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/lib/gstreamer-sharp.dll
%{_prefix}/lib/gstreamer-sharp.dll.config
%{_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%changelog
* Wed Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.14.2-1
- Updated to use NuGet package

* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- Updated to 1.12.3
- Epoch 1

* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.9.1.2
- first draft of spec file


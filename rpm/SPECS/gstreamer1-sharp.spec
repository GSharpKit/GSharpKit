%define debug_package %{nil}

Name:		gstreamer1-sharp
Version: 	1.14.2
Release: 	1%{?dist}
Epoch:		1
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	https://github.com/GSharpKit/gstreamer-sharp/releases/gstreamer-sharp-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildRequires:	pkgconfig gstreamer1-devel gstreamer1-plugins-base-devel gst-editing-services-devel gstreamer1-plugins-bad-free-devel
BuildRequires:	mono-core

Requires:       gstreamer1
Requires:       gstreamer1-plugins-base

Obsoletes:	gstreamer1-sharp-devel
Provides:	gstreamer1-sharp-devel

Provides:	mono(gio-sharp) = 3.0.0.0 
Provides:	mono(glib-sharp) = 3.0.0.0

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gstreamer-sharp-%{version}

sed -i -e 's!1.14.2!1.14.1!g' meson.build

cat > gstreamer-sharp-1.0.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib/mono

Name: gstreamer1-sharp
Description: gstreamer1-sharp - gstreamer1 .NET Binding
Version: %{version}
Libs: -r:${libdir}/gstreamer-sharp-1.0/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF

%build
meson --prefix=%{_prefix} --libdir=%{_prefix}/lib build/
ninja -C build/

%install
%{__rm} -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i build/sources/gstreamer-sharp.dll -package gstreamer-sharp-1.0 -root $RPM_BUILD_ROOT%{_prefix}/lib -gacdir mono/gac

install -d -m 755 %{buildroot}%{_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc %{buildroot}%{_prefix}/share/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/lib/mono/gac
%{_prefix}/lib/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
%{_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%changelog
* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- Updated to 1.12.3
- Epoch 1

* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.9.1.2
- first draft of spec file


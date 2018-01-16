%define debug_package %{nil}

Name:		darwinx-gstreamer1-sharp
Version: 	1.12.3
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source: 	https://github.com/GSharpKit/gstreamer-sharp/releases/gstreamer-sharp-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:	darwinx-gstreamer1 >= 1.12

BuildRequires:	pkgconfig

BuildRequires:	darwinx-filesystem >= 14
BuildRequires:	darwinx-mono-core
BuildRequires:	darwinx-gstreamer1 >= 1.12

Obsoletes:	darwinx-gstreamer-sharp

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gstreamer-sharp-%{version}

sed -i '' 's!1.13.0.1!1.12.3!' meson.build

cat > gstreamer-sharp-1.0.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib

Name: gstreamer1-sharp
Description: gstreamer1-sharp - gstreamer1 .NET Binding
Version: %{version}
Libs: -r:${libdir}/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF

%build
%{_darwinx_env} ; meson --prefix=%{_darwinx_prefix} --libdir=%{_darwinx_prefix}/lib build/
ninja -C build/

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 %{buildroot}%{_darwinx_prefix}/lib/mono/gstreamer-sharp-1.0/
install -d -m 755 %{buildroot}%{_darwinx_prefix}/share/pkgconfig

install -m 644 build/sources/gstreamer-sharp.dll %{buildroot}%{_darwinx_prefix}/lib/mono/gstreamer-sharp-1.0/
install -m 644 gstreamer-sharp-1.0.pc %{buildroot}%{_darwinx_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
#{_darwinx_libdir}/mono/gac/gstreamer-sharp
%{_darwinx_libdir}/mono/gstreamer-sharp/gstreamer-sharp.dll
%{_darwinx_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%changelog
* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.9.1.2
- first draft of spec file


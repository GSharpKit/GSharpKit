%define debug_package %{nil}

%define libdir /lib

Name:		darwinx-GstSharp
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
Source2:	netstandard.dll
Requires:       darwinx-mono-core >= 6.12
Requires:       darwinx-gstreamer1
Requires:       darwinx-gstreamer1-plugins-base

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gstreamer-sharp-%{version}

sed -i '' 's!/usr/lib/mono/xbuild-frameworks/.NETStandard/netstandard2.0/netstandard.dll!netstandard.dll!g' sources/meson.build
sed -i '' 's!/usr/lib/mono/xbuild-frameworks/.NETStandard/netstandard2.0/netstandard.dll!netstandard.dll!g' ges/meson.build
sed -i '' 's!subdir('\''samples'\'')!!g' meson.build

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
%darwinx_meson \
	-Dtests=disabled

cp %{SOURCE2} x86_64-apple-darwin13/
cp /Library/Frameworks/GSharpKit/lib/GLibSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/GioSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/PangoSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/CairoSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/GdkSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/AtkSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/
cp /Library/Frameworks/GSharpKit/lib/GtkSharp.dll x86_64-apple-darwin13/subprojects/gtk-sharp/

%darwinx_meson_build

%install
%{__rm} -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
install -m 644 x86_64-apple-darwin13/sources/gstreamer-sharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
install -m 644 x86_64-apple-darwin13/sources/gstreamer-sharp.dll.config $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}

install -d -m 755 %{buildroot}%{darwinx_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc %{buildroot}%{darwinx_prefix}/share/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{darwinx_prefix}/lib/gstreamer-sharp.dll
%{darwinx_prefix}/lib/gstreamer-sharp.dll.config
%{darwinx_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%changelog
* Wed Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.14.2-1
- Updated to use NuGet package

* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- Updated to 1.12.3
- Epoch 1

* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.9.1.2
- first draft of spec file


%{?mingw_package_header}

%global mingw_pkg_name gstreamer1-sharp 
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:		mingw-gstreamer1-sharp
Version: 	1.12.3
Release: 	1%{?dist}
Epoch:		1
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	https://github.com/GSharpKit/gstreamer-sharp/releases/gstreamer-sharp-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildRequires:	pkgconfig gstreamer1-devel gstreamer1-plugins-base-devel gst-editing-services-devel
BuildRequires:	mono-core

Requires:       gstreamer1
Requires:       gstreamer1-plugins-base

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2
Requires:       mingw32-gtk3
Requires:       mingw32-gstreamer1
Requires:       mingw32-mono-core >= 3.12

%description -n mingw32-%{mingw_pkg_name}
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-gtk3
Requires:       mingw64-gstreamer1
Requires:       mingw64-mono-core >= 3.12

%description -n mingw64-%{mingw_pkg_name}
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%prep
%setup -q -n gstreamer-sharp-%{version}

sed -i -e 's!1.13.0.1!1.12.3!g' meson.build

cat > gstreamer-sharp-1.0.pc32 << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib

Name: gstreamer1-sharp
Description: gstreamer1-sharp - gstreamer1 .NET Binding
Version: %{version}
Libs: -r:${libdir}/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF

cat > gstreamer-sharp-1.0.pc64 << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib

Name: gstreamer1-sharp
Description: gstreamer1-sharp - gstreamer1 .NET Binding
Version: %{version}
Libs: -r:${libdir}/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF


%build
meson --prefix=%{_prefix} --libdir=%{_prefix}/lib build/
ninja -C build/

%install
%{__rm} -rf $RPM_BUILD_ROOT

# Mingw32
install -d -m 755 %{buildroot}%{mingw32_prefix}/lib/mono/gstreamer-sharp-1.0/
install -d -m 755 %{buildroot}%{mingw32_prefix}/share/pkgconfig

install -m 644 build/sources/gstreamer-sharp.dll %{buildroot}%{mingw32_prefix}/lib/mono/gstreamer-sharp-1.0/
install -m 644 gstreamer-sharp-1.0.pc32 %{buildroot}%{mingw32_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc

# Mingw64
install -d -m 755 %{buildroot}%{mingw64_prefix}/lib/mono/gstreamer-sharp-1.0/
install -d -m 755 %{buildroot}%{mingw64_prefix}/share/pkgconfig

install -m 644 build/sources/gstreamer-sharp.dll %{buildroot}%{mingw64_prefix}/lib/mono/gstreamer-sharp-1.0/
install -m 644 gstreamer-sharp-1.0.pc64 %{buildroot}%{mingw64_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root)
%{mingw32_prefix}/lib/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
%{mingw32_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root)
%{mingw64_prefix}/lib/mono/gstreamer-sharp-1.0/gstreamer-sharp.dll
%{mingw64_datadir}/pkgconfig/gstreamer-sharp-1.0.pc


%changelog
* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- first draft of spec file


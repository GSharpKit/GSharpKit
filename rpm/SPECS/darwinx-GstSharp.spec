%global darwinx_pkg_name GstSharp 

%define libdir /lib

Name:		darwinx-GstSharp
Version: 	1.16.0
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -c %{name}-%{version} -T
nuget install %{darwinx_pkg_name} -Version %{version}

cat > gstreamer-sharp-1.0.pc << \EOF
prefix=%{darwinx_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}%{libdir}

Name: %{darwinx_pkg_name}
Description: %{summary} 
Version: %{version}
Libs: -r:${libdir}/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net45/gstreamer-sharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}%{libdir}

install -d -m 755 %{buildroot}%{darwinx_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc %{buildroot}%{darwinx_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{darwinx_prefix}%{libdir}/gstreamer-sharp.dll
%{darwinx_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%changelog
* Wed Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.14.2-1
- Updated to use NuGet package

* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- first draft of spec file


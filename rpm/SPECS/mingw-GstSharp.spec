%{?mingw_package_header}

%global mingw_pkg_name GstSharp 
%global mingw_build_win32 1
%global mingw_build_win64 1

%define libdir /bin
%define debug_package %{nil}

Name:		mingw-GstSharp
Version: 	1.16.0
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch
BuildRequires:	nuget

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
Requires:       mingw32-gstreamer1

Obsoletes:	mingw32-gstreamer1-sharp
Provides:	mingw32-gstreamer1-sharp

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
Requires:       mingw64-gstreamer1

Obsoletes:      mingw64-gstreamer1-sharp
Provides:       mingw64-gstreamer1-sharp

%description -n mingw64-%{mingw_pkg_name}
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > gstreamer-sharp-1.0.pc32 << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{summary} 
Version: %{version}
Libs: -r:${libdir}/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF

cat > gstreamer-sharp-1.0.pc64 << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{summary}
Version: %{version}
Libs: -r:${libdir}/gstreamer-sharp.dll
Requires: gtk-sharp-3.0
EOF


%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net45/gstreamer-sharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 %{buildroot}%{mingw32_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc32 %{buildroot}%{mingw32_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net45/gstreamer-sharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 %{buildroot}%{mingw64_prefix}/share/pkgconfig
install -m 644 gstreamer-sharp-1.0.pc64 %{buildroot}%{mingw64_prefix}/share/pkgconfig/gstreamer-sharp-1.0.pc


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root)
%{mingw32_prefix}%{libdir}/gstreamer-sharp.dll
%{mingw32_datadir}/pkgconfig/gstreamer-sharp-1.0.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root)
%{mingw64_prefix}%{libdir}/gstreamer-sharp.dll
%{mingw64_datadir}/pkgconfig/gstreamer-sharp-1.0.pc


%changelog
* Wed Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.14.2-1
- Updated to use NuGet package

* Mon Nov 20 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.12.3-1
- first draft of spec file


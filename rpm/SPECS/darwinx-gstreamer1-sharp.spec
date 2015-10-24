%define debug_package %{nil}

Name:		darwinx-gstreamer1-sharp
Version: 	1.39.91
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source: 	http://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:	darwinx-gstreamer1 >= 1.2

BuildRequires:	pkgconfig

BuildRequires:	darwinx-filesystem >= 14
BuildRequires:	darwinx-mono
BuildRequires:	darwinx-gstreamer1 >= 1.2

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

sed -i '' 's!csc.exe!msc!' configure.ac

%build
#NOCONFIGURE=yes sh autogen.sh
#DARWINX_CFLAGS="%{_darwinx_cppflags} -arch x86_64 -DMAC_OS_X_VERSION_MIN_REQUIRED=1050 -D__DARWIN_UNIX03" DARWINX_CXXFLAGS="%{_darwinx_cppflags} -arch x86_64 -DMAC_OS_X_VERSION_MIN_REQUIRED=1050 -D__DARWIN_UNIX03" 
autoreconf --verbose --install -I /usr/darwinx/usr/share/aclocal
%{_darwinx_configure} --disable-static

%{_darwinx_make}

%install  
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT program_transform_name=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_darwinx_libdir}/libgstreamersharpglue-1.0.0.la
%{_darwinx_libdir}/libgstreamersharpglue-1.0.0.so
%{_darwinx_libdir}/mono/gac/gstreamer-sharp
%{_darwinx_libdir}/mono/gstreamer-sharp/gstreamer-sharp.dll
%{_darwinx_libdir}/monodoc/sources/gstreamer-sharp-docs.source
%{_darwinx_libdir}/monodoc/sources/gstreamer-sharp-docs.tree
%{_darwinx_libdir}/monodoc/sources/gstreamer-sharp-docs.zip
%{_darwinx_libdir}/pkgconfig/gstreamer-sharp-1.0.pc
%{_darwinx_datadir}/gapi-3.0/gstreamer-sharp-api.xml

%changelog
* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.9.1.2
- first draft of spec file


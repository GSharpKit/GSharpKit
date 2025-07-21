%define		majorminor	1.0

Name:		darwinx-gstreamer1-plugins-base
Version: 	1.26.4
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework base plug-ins
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-gstreamer1 >= %{version}

BuildRequires:	darwinx-filesystem >= 108
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-zlib
BuildRequires:	darwinx-opus
#BuildRequires:	darwinx-libtheora
BuildRequires:	darwinx-gstreamer1 >= %{version}

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Requires:	darwinx-filesystem >= 108
Requires:	darwinx-gstreamer1

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

%prep
%setup -q -n gst-plugins-base-%{version}

%build
%darwinx_meson \
    --default-library=shared \
    -Ddoc=disabled \
    -Dtests=disabled \
    -Dexamples=disabled \
    -Dintrospection=disabled \
    -Dx11=disabled \
    -Dxshm=disabled \
    -Dxvideo=disabled \
    -Dxi=disabled \
    -Dorc=disabled \
    -Dtremor=disabled \
    -Dtheora=disabled \
    -Dopus=enabled \
    -Dalsa=disabled \
    -Dcdparanoia=disabled \
    -Dlibvisual=disabled \
    -Dgl-graphene=disabled \
    -Ddrm=disabled \
    -Diso-codes=disabled

%darwinx_meson_build

%install
rm -rf $RPM_BUILD_ROOT

%darwinx_meson_install

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, wheel, -)
%{_darwinx_bindir}
%{_darwinx_libdir}
%{_darwinx_includedir}
%{_darwinx_datadir}

%changelog
* Thu Apr 06 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


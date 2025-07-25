%define		majorminor	1.0

Name:		darwinx-gstreamer1-plugins-good
Version: 	1.26.4
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework base plug-ins
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-gstreamer1 >= %{version}
Requires:	darwinx-gstreamer1-plugins-base >= %{version}

BuildRequires:	darwinx-filesystem-base >= 109
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-zlib
BuildRequires:	darwinx-gstreamer1 >= %{version}
BuildRequires:	darwinx-gstreamer1-plugins-base >= %{version}
BuildRequires:	darwinx-speex
BuildRequires:	darwinx-wavpack

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Requires:	darwinx-filesystem >= 109
Requires:  	darwinx-gstreamer1 >= %{version}
Requires:  	darwinx-gstreamer1-plugins-base >= %{version}


%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

%prep
%setup -q -n gst-plugins-good-%{version}

%build
%darwinx_meson \
	--default-library=shared \
	--auto-features=auto \
	-Ddoc=disabled \
	-Dnls=disabled \
	-Dtests=disabled \
	-Dexamples=disabled \
	-Dasm=disabled

%install
rm -rf $RPM_BUILD_ROOT

%darwinx_meson_install

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

# Remove GConf schemas
rm -rf $RPM_BUILD_ROOT%{_darwinx_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, wheel, -)
%{_darwinx_libdir}/gstreamer-1.0/*.dylib
%{_darwinx_datadir}/gstreamer-1.0

%changelog
* Thu Apr 06 2010 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


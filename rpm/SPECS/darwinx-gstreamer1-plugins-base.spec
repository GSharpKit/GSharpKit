%define		majorminor	1.0

Name:		darwinx-gstreamer1-plugins-base
Version: 	1.8.1
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework base plug-ins
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:	darwinx-gstreamer1 >= %{version}

BuildRequires:	darwinx-filesystem >= 18
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gstreamer1 >= %{version}
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Requires:	darwinx-filesystem >= 18

Obsoletes:	darwinx-gstreamer-plugins-base

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

#%patch1 -p1 -b .rpm-provides

%build
%{_darwinx_configure} \
  --with-package-name='Fedora gstreamer package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --disable-gtk-doc \
  --enable-debug \
  --disable-tests \
  --disable-examples \
  --disable-x \
  --disable-xvideo \
  --disable-zlib \
  --enable-vorbis

%{_darwinx_make} %{?_smp_mflags}

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily later will be removed
%{_darwinx_makeinstall} program_transform_name=""

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_darwinx_bindir}
%{_darwinx_libdir}
%{_darwinx_includedir}
%{_darwinx_datadir}

%changelog
* Thu Apr 06 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


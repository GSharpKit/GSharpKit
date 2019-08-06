%define		majorminor	1.0

Name:		darwinx-gstreamer1-plugins-good
Version: 	1.14.2
Release: 	2%{?dist}
Summary: 	GStreamer streaming media framework base plug-ins
Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:	darwinx-gstreamer1 >= %{version}
Requires:	darwinx-gstreamer1-plugins-base >= %{version}

BuildRequires:	darwinx-filesystem-base >= 109
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gstreamer1 >= %{version}
BuildRequires:	darwinx-gstreamer1-plugins-base >= %{version}
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Obsoletes:	darwinx-gstreamer-plugins-good

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
%{_darwinx_configure} \
  --with-package-name='Fedora gstreamer package' \
  --with-package-origin='http://download.fedora.redhat.com/fedora' \
  --disable-x \
  --disable-xvideo \
  --disable-gtk-doc \
  --enable-debug \
  --disable-tests \
  --disable-examples \
  --disable-shout2 \
  --disable-shout2test \
  --disable-jpeg \
  --disable-goom \
  --disable-osx_video

%{_darwinx_make} OBJC=%{_darwinx-cc} %{?_smp_mflags}

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily later will be removed
%{_darwinx_makeinstall}

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

# Remove GConf schemas
rm -rf $RPM_BUILD_ROOT%{_darwinx_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_darwinx_libdir}
%{_darwinx_datadir}

%changelog
* Thu Apr 06 2010 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


%define		majorminor	1.0

Name:		darwinx-gst-editing-services
Version: 	1.12.4
Release: 	1%{?dist}
Summary: 	This is a high-level library for facilitating the creation of audio/video non-linear editors.

Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	https://github.com/GStreamer/gst-editing-services/releases/gst-editing-services-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-gstreamer1

Requires:	darwinx-filesystem >= 18

Obsoletes:	darwinx-gstreamer

%description
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%prep
%setup -q -n gst-editing-services-%{version}

%build
%{_darwinx_env} ; meson --prefix=%{_darwinx_prefix} --libdir=%{_darwinx_prefix}/lib build/
ninja -C build/

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily later will be removed
make install DESTDIR=$RPM_BUILD_ROOT program_transform_name=""

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


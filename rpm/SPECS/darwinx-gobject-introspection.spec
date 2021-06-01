Name:		darwinx-gobject-introspection
Version: 	1.68.0
Release: 	1%{?dist}
Summary: 	This is a high-level library for facilitating the creation of audio/video non-linear editors.

Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	https://download-fallback.gnome.org/sources/gobject-introspection/1.68/gobject-introspection-1.68.0.tar.xz
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
%setup -q -n gobject-introspection-%{version}

%build
export MACOSX_DEPLOYMENT_TARGET=10.9
%darwinx_meson \
    --default-library=shared \
    --auto-features=auto

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
%defattr(-, root, root, -)
%{_darwinx_bindir}
%{_darwinx_libdir}
%{_darwinx_datadir}
%{_darwinx_includedir}

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


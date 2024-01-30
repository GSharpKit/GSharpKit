%define debug_package %{nil}

%define _use_internal_dependency_generator 0

#_target_arch	noarch
#define _target_os	linux

Name: 		darwinx-filesystem
Version: 	203
Release: 	1%{?dist}
Summary: 	Darwin filesystem and environment
License: 	GPLv2+
Group: 		Development/Libraries
URL: 		http://www.gsharpkit.org

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

Provides:	Carbon
Provides:	CoreFoundation
Provides:	CoreServices
Provides:	Foundation
Provides:	ApplicationServices
Provides:	CoreGraphics
Provides:	CoreText
Provides:	AppKit
Provides:	Cocoa
Provides:	Security
Provides:	SystemConfiguration
Provides:	AudioToolbox
Provides:	AudioUnit
Provides:	CoreAudio
Provides:	OpenGL
Provides:	CoreMedia
Provides:	CoreVideo
Provides:	QTKit
Provides:       AVFoundation
Provides:       VideoToolbox
Provides:	Kerberos
Provides:	QuartzCore
Provides:	GSS
Provides:	IOSurface
Provides:	CFNetwork

Provides:	libSystem.B.dylib
Provides:	libexpat.1.dylib
Provides:	libiconv.2.dylib
Provides:	libncurses.5.4.dylib
Provides:	libstdc++.6.dylib
Provides:	libxml2.2.dylib
Provides:	libobjc.A.dylib
Provides:	libresolv.9.dylib
Provides:	libz.1.dylib
Provides:	libbz2.1.0.dylib
Provides:	libc++.1.dylib
Provides:	libcups.2.dylib
Provides:	libedit.3.dylib 
#Provides:	libsqlite3.dylib 
Provides:	liblzma.5.dylib
Provides:	libltdl.7.dylib

%description
This package contains the base filesystem layout, RPM macros and
environment for Darwin (Mac OS X) cross-compiler packages.


%prep
%setup -q -c -T

%build
# nothing


%install

%clean

%files
%defattr(-,root,root)


%changelog
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1-1
- Initial RPM release.

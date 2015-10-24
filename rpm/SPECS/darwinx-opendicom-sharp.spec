Name:		darwinx-opendicom-sharp
Version: 	0.1.1
Release: 	6%{?dist}
Summary: 	openDICOM# - DICOM Mono/.NET library
Group: 		System Environment/Libraries
License: 	LGPL
URL:		http://opendicom.sourceforge.net
Source0: 	opendicom-sharp-%{version}.tar.bz2
Source1:        xcare.pub
Patch0:		opendicom-sharp-%{version}-nodocs.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch:      noarch

BuildRequires:	darwinx-mono
BuildRequires:	darwinx-gtk-sharp3

Requires:  	darwinx-mono
Requires:  	darwinx-gtk-sharp3

%description
The opendicom-sharp class libary, main part of the project, provides 
an API to DICOM in C# for Mono and the .NET Framework. It is a 
completely new implementation of DICOM. In contrast to other similar 
libraries the intention of this implementation is to provide a clean 
classification with support of unidirectional DICOM data streaming. 
Another implemented goal is the support of DICOM as XML. This is not 
standard conform but very use- and powerful within software development, 
storage and manipulation. The entire DICOM content can be accessed 
as sequence or as tree of class instances. Latter is the default 
representation of DICOM content by the library.

%prep
%setup -q -n opendicom-sharp-%{version}
%patch0 -p1

cat > opendicom-sharp.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_libdir}

Name: openDICOM#
Description: openDICOM# - DICOM Mono/.NET library
Requires:
Version: %{version}
Libs: -r:${libdir}/opendicom-sharp.dll
Cflags:
EOF

cp %{SOURCE1} .
sed -i '' "s!DICOM_SHARP_COMPILE=mcs!DICOM_SHARP_COMPILE=/usr/bin/mcs -keyfile:xcare.pub!" Makefile

%build

%{_darwinx_make}

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_libdir}/
install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_libdir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/opendicom
install -m 755 bin/opendicom-sharp.dll $RPM_BUILD_ROOT%{_darwinx_libdir}/
install -m 644 opendicom-sharp.pc $RPM_BUILD_ROOT%{_darwinx_libdir}/pkgconfig/
install -m 644 dd/*.dic $RPM_BUILD_ROOT%{_darwinx_datadir}/opendicom/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%dir %{_darwinx_datadir}/opendicom
%{_darwinx_libdir}/*.dll
%{_darwinx_datadir}/opendicom/*
%{_darwinx_libdir}/pkgconfig/opendicom-sharp.pc



%changelog
* Sat Jun 05 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


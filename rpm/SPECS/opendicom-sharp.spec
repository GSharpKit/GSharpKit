%global debug_package %{nil}

%define libdir /lib

Name:		opendicom-sharp
Version: 	0.1.1
Release: 	6%{?dist}
Summary: 	openDICOM# - DICOM Mono/.NET library
Group: 		System Environment/Libraries
License: 	LGPL
URL:		http://opendicom.sourceforge.net
Source0: 	opendicom-sharp-%{version}.tar.bz2
Source1:	xcare.pub
Patch0:		opendicom-sharp-%{version}-nodocs.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch
BuildRequires:	mono-core
BuildRequires:	gtk-sharp3-devel

Requires:  	mono-core
Requires:  	gtk-sharp3

Provides:	opendicom-devel

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
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: openDICOM#
Description: openDICOM# - DICOM Mono/.NET library
Requires:
Version: 0.1.1.0
Libs: -r:${libdir}/opendicom-sharp.dll
Cflags:
EOF

cp %{SOURCE1} .
sed -i -e "s!DICOM_SHARP_COMPILE=mcs!DICOM_SHARP_COMPILE=mcs -keyfile:xcare.pub!" Makefile

%build
make

%install  
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 755 bin/opendicom-sharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
#install -m 755 bin/opendicom-sharp.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 opendicom-sharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/opendicom
install -m 644 dd/*.dic $RPM_BUILD_ROOT%{_datadir}/opendicom/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%dir %{_datadir}/opendicom
%{_prefix}%{libdir}/opendicom-sharp.dll
#%{_prefix}%{libdir}/opendicom-sharp.dll.mdb
%{_datadir}/opendicom/*
%{_datadir}/pkgconfig/opendicom-sharp.pc



%changelog
* Sat Jun 05 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


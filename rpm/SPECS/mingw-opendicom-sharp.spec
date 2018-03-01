%{?mingw_package_header}

%global mingw_pkg_name opendicom-sharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:		mingw-opendicom-sharp
Version: 	0.1.1
Release: 	2%{?dist}
Summary: 	openDICOM# - DICOM Mono/.NET library
Group: 		System Environment/Libraries
License: 	LGPL
URL:		http://opendicom.sourceforge.net
Source0: 	opendicom-sharp-%{version}.tar.bz2
Source1:        xcare.pub
BuildArch:      noarch
Patch0:		opendicom-sharp-%{version}-nodocs.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildRequires:	mono-core
BuildRequires:	mingw32-gtk-sharp3

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

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2
Requires:       mingw32-mono >= 2.11

%description -n mingw32-%{mingw_pkg_name}
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

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-mono >= 2.11

%description -n mingw64-%{mingw_pkg_name}
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

cat > opendicom-sharp-32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_libdir}

Name: openDICOM#
Description: openDICOM# - DICOM Mono/.NET library
Requires:
Version: %{version}
Libs: -r:${libdir}/opendicom-sharp.dll
Cflags:
EOF

cat > opendicom-sharp-64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_libdir}

Name: openDICOM#
Description: openDICOM# - DICOM Mono/.NET library
Requires:
Version: %{version}
Libs: -r:${libdir}/opendicom-sharp.dll
Cflags:
EOF


cp %{SOURCE1} .
sed -i -e "s!DICOM_SHARP_COMPILE=mcs!DICOM_SHARP_COMPILE=/usr/bin/mcs -keyfile:xcare.pub!" Makefile

%build
find . -name Makefile | while read f ;
         do
           sed -i -e 's!CSC = /usr/i686-w64-mingw32/sys-root/mingw/bin/mcs!CSC = /usr/bin/mcs!' "$f"
         done


%install  
rm -rf $RPM_BUILD_ROOT

%mingw32_make

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_libdir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/opendicom
install -m 755 bin/opendicom-sharp.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 644 opendicom-sharp-32.pc $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/opendicom-sharp.pc
install -m 644 dd/*.dic $RPM_BUILD_ROOT%{mingw32_datadir}/opendicom/

%mingw32_make clean

%mingw64_make

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_libdir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/opendicom
install -m 755 bin/opendicom-sharp.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 644 opendicom-sharp-64.pc $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/opendicom-sharp.pc
install -m 644 dd/*.dic $RPM_BUILD_ROOT%{mingw64_datadir}/opendicom/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-, root, root, -)
%dir %{mingw32_datadir}/opendicom
%{mingw32_libdir}/*.dll
%{mingw32_datadir}/opendicom/*
%{mingw32_libdir}/pkgconfig/opendicom-sharp.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-, root, root, -)
%dir %{mingw64_datadir}/opendicom
%{mingw64_libdir}/*.dll
%{mingw64_datadir}/opendicom/*
%{mingw64_libdir}/pkgconfig/opendicom-sharp.pc


%changelog
* Sat Jun 05 2010 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


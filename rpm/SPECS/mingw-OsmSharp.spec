%{?mingw_package_header}

%global mingw_pkg_name OsmSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%global debug_package %{nil}

Name:		mingw-OsmSharp
Version: 	4.2.0.724
Release: 	2%{?dist}
Summary: 	OsmSharp is an open-source mapping tool
Group: 		System Environment/Libraries
License: 	LGPL
URL:		http://osmsharp.com/
Source0: 	OsmSharp-master.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem

BuildRequires:	referenceassemblies-pcl
BuildRequires:	mono-core

%description
OsmSharp is an open-source mapping tool designed to work with OpenStreetMap. 
Most important features are offline rendering of vector-data and routing. 
All OsmSharp features are available on Android, iOS, Windows Phone 
(using the Xamarin products) and the regulars Linux, Windows, OSX (using Mono).

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-mono >= 3.0

%description -n mingw32-%{mingw_pkg_name}
OsmSharp is an open-source mapping tool designed to work with OpenStreetMap.
Most important features are offline rendering of vector-data and routing.
All OsmSharp features are available on Android, iOS, Windows Phone
(using the Xamarin products) and the regulars Linux, Windows, OSX (using Mono).

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-mono >= 3.0

%description -n mingw64-%{mingw_pkg_name}
OsmSharp is an open-source mapping tool designed to work with OpenStreetMap.
Most important features are offline rendering of vector-data and routing.
All OsmSharp features are available on Android, iOS, Windows Phone
(using the Xamarin products) and the regulars Linux, Windows, OSX (using Mono).



%prep
%setup -q -n OsmSharp-master

cat > OsmSharp32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_libdir}

Name: OsmSharp
Description: OsmSharp is an open-source mapping tool 
Requires:
Version: %{version}
Libs: -r:${libdir}/OsmSharp.dll -r:${libdir}/OsmSharp.Osm.dll -r:${libdir}/OsmSharp.Routing.dll -r:${libdir}/protobuf-net.dll -r:${libdir}/Zlib.Portable.dll
Cflags:
EOF

cat > OsmSharp64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_libdir}

Name: OsmSharp
Description: OsmSharp is an open-source mapping tool
Requires:
Version: %{version}
Libs: -r:${libdir}/OsmSharp.dll -r:${libdir}/OsmSharp.Osm.dll -r:${libdir}/OsmSharp.Routing.dll -r:${libdir}/protobuf-net.dll -r:${libdir}/Zlib.Portable.dll
Cflags:
EOF

%build


%install  
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_libdir}

install -m 755 OsmSharp.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 755 OsmSharp.dll.mdb $RPM_BUILD_ROOT%{mingw32_libdir}/

install -m 755 OsmSharp.Osm.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 755 OsmSharp.Osm.dll.mdb $RPM_BUILD_ROOT%{mingw32_libdir}/

install -m 755 OsmSharp.Routing.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 755 OsmSharp.Routing.dll.mdb $RPM_BUILD_ROOT%{mingw32_libdir}/

install -m 755 protobuf-net.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 755 Zlib.Portable.dll $RPM_BUILD_ROOT%{mingw32_libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 OsmSharp32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/OsmSharp.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_libdir}

install -m 755 OsmSharp.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 755 OsmSharp.dll.mdb $RPM_BUILD_ROOT%{mingw64_libdir}/

install -m 755 OsmSharp.Osm.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 755 OsmSharp.Osm.dll.mdb $RPM_BUILD_ROOT%{mingw64_libdir}/

install -m 755 OsmSharp.Routing.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 755 OsmSharp.Routing.dll.mdb $RPM_BUILD_ROOT%{mingw64_libdir}/

install -m 755 protobuf-net.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 755 Zlib.Portable.dll $RPM_BUILD_ROOT%{mingw64_libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 OsmSharp64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/OsmSharp.pc




%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw32_libdir}/OsmSharp.dll
%{mingw32_libdir}/OsmSharp.dll.mdb
%{mingw32_libdir}/OsmSharp.Osm.dll
%{mingw32_libdir}/OsmSharp.Osm.dll.mdb
%{mingw32_libdir}/OsmSharp.Routing.dll
%{mingw32_libdir}/OsmSharp.Routing.dll.mdb
%{mingw32_libdir}/protobuf-net.dll
%{mingw32_libdir}/Zlib.Portable.dll
%{mingw32_datadir}/pkgconfig/OsmSharp.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw64_libdir}/OsmSharp.dll
%{mingw64_libdir}/OsmSharp.dll.mdb
%{mingw64_libdir}/OsmSharp.Osm.dll
%{mingw64_libdir}/OsmSharp.Osm.dll.mdb
%{mingw64_libdir}/OsmSharp.Routing.dll
%{mingw64_libdir}/OsmSharp.Routing.dll.mdb
%{mingw64_libdir}/protobuf-net.dll
%{mingw64_libdir}/Zlib.Portable.dll
%{mingw64_datadir}/pkgconfig/OsmSharp.pc


%changelog
* Tue Jul 28 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


%global debug_package %{nil}

%define libdir /lib

Name:		OsmSharp
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
BuildRequires:	referenceassemblies-pcl
BuildRequires:	mono-core

Requires:  	referenceassemblies-pcl
Requires:  	mono-core

%description
OsmSharp is an open-source mapping tool designed to work with OpenStreetMap. 
Most important features are offline rendering of vector-data and routing. 
All OsmSharp features are available on Android, iOS, Windows Phone 
(using the Xamarin products) and the regulars Linux, Windows, OSX (using Mono).

%prep
%setup -q -n OsmSharp-master

cat > OsmSharp.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

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

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -m 755 OsmSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 OsmSharp.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -m 755 OsmSharp.Osm.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 OsmSharp.Osm.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -m 755 OsmSharp.Routing.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 OsmSharp.Routing.dll.mdb $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -m 755 protobuf-net.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 Zlib.Portable.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 OsmSharp.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_prefix}%{libdir}/OsmSharp.dll
%{_prefix}%{libdir}/OsmSharp.dll.mdb
%{_prefix}%{libdir}/OsmSharp.Osm.dll
%{_prefix}%{libdir}/OsmSharp.Osm.dll.mdb
%{_prefix}%{libdir}/OsmSharp.Routing.dll
%{_prefix}%{libdir}/OsmSharp.Routing.dll.mdb
%{_prefix}%{libdir}/protobuf-net.dll
%{_prefix}%{libdir}/Zlib.Portable.dll
%{_datadir}/pkgconfig/OsmSharp.pc

%changelog
* Tue Jul 28 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


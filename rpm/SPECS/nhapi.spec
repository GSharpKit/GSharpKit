%global debug_package %{nil}

%define libdir /lib


Name:		nHapi
Version: 	2.5.0.6
Release: 	1%{?dist}
Summary: 	nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Group: 		System Environment/Libraries
License: 	MPL 1.1
URL:		https://github.com/duaneedwards/nHapi
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch

BuildRequires:	nuget
Requires:  	mono-core

Obsoletes:	NHapi-devel NHapi
Provides:	NHapi-devel NHapi

%description
nHapi is a port of the original project HAPI.
nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model. This object model allows for parsing and encoding HL7 2.x data to/from Pipe Delmimited or XML formats. A very handy program for use in the health care industry.
This project is NOT affiliated with the HL7 organization. This software just conforms to the HL7 2.x specifications.
Key Benefits:
    Easy object model
    Microsoft .NET 2.0 library that conforms to HL7 2.1, 2.2, 2.3, 2.3.1, 2.4, and 2.5 specifications
    Can take a pipe delmimited or XML formated HL7 2.x message and build the C# object model for use in code
    Can take the C# Hl7 object model and produce pipe delimited or XML formatted HL7
    FREE! (You can't beat that price) and open source
    Fast

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > nHapi-v281.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V281.dll
Cflags:
EOF

cat > nHapi-v28.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V28.dll
Cflags:
EOF

cat > nHapi-v271.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V271.dll
Cflags:
EOF

cat > nHapi-v27.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V27.dll
Cflags:
EOF

cat > nHapi-v26.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V26.dll
Cflags:
EOF

cat > nHapi-v251.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V251.dll
Cflags:
EOF

cat > nHapi-v25.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V25.dll
Cflags:
EOF

cat > nHapi-v24.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V24.dll
Cflags:
EOF

cat > nHapi-v231.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires: 
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V231.dll
Cflags:
EOF

cat > nHapi-v23.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V23.dll
Cflags:
EOF

cat > nHapi-v22.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V22.dll
Cflags:
EOF

cat > nHapi-v21.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: nHapi
Description: nHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V21.dll
Cflags:
EOF


%build

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Base.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V21.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V22.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V23.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V231.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V24.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V25.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V251.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V26.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V27.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V271.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V28.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 nHapi.%{version}/lib/NHapi.Model.V281.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -m 644 nHapi-v21.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v22.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v23.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v231.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v24.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v25.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v251.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v26.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v27.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v271.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v28.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 nHapi-v281.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_prefix}/%{libdir}/NHapi.Base.dll
%{_prefix}/%{libdir}/NHapi.Model.V21.dll
%{_prefix}/%{libdir}/NHapi.Model.V22.dll
%{_prefix}/%{libdir}/NHapi.Model.V23.dll
%{_prefix}/%{libdir}/NHapi.Model.V231.dll
%{_prefix}/%{libdir}/NHapi.Model.V24.dll
%{_prefix}/%{libdir}/NHapi.Model.V25.dll
%{_prefix}/%{libdir}/NHapi.Model.V251.dll
%{_prefix}/%{libdir}/NHapi.Model.V26.dll
%{_prefix}/%{libdir}/NHapi.Model.V27.dll
%{_prefix}/%{libdir}/NHapi.Model.V271.dll
%{_prefix}/%{libdir}/NHapi.Model.V28.dll
%{_prefix}/%{libdir}/NHapi.Model.V281.dll
%{_datadir}/pkgconfig/nHapi-v21.pc
%{_datadir}/pkgconfig/nHapi-v22.pc
%{_datadir}/pkgconfig/nHapi-v23.pc
%{_datadir}/pkgconfig/nHapi-v231.pc
%{_datadir}/pkgconfig/nHapi-v24.pc
%{_datadir}/pkgconfig/nHapi-v25.pc
%{_datadir}/pkgconfig/nHapi-v251.pc
%{_datadir}/pkgconfig/nHapi-v26.pc
%{_datadir}/pkgconfig/nHapi-v27.pc
%{_datadir}/pkgconfig/nHapi-v271.pc
%{_datadir}/pkgconfig/nHapi-v28.pc
%{_datadir}/pkgconfig/nHapi-v281.pc

%changelog
* Sat Apr 21 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Created for later versions aswell

* Mon Aug 13 2012 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


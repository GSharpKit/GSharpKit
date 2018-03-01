%global debug_package %{nil}

%define libdir /lib


Name:		NHapi
Version: 	2.3.1
Release: 	4%{?dist}
Summary: 	NHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Group: 		System Environment/Libraries
License: 	MPL 1.1
URL:		http://nhapi.sourceforge.net
Source0: 	NHapi-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch
Requires:  	mono-core

Obsoletes:	NHapi-devel
Provides:	NHapi-devel

%description
NHapi is a port of the original project HAPI.
NHapi allows Microsoft .NET developers to easily use an HL7 2.x object model. This object model allows for parsing and encoding HL7 2.x data to/from Pipe Delmimited or XML formats. A very handy program for use in the health care industry.
This project is NOT affiliated with the HL7 organization. This software just conforms to the HL7 2.x specifications.
Key Benefits:
    Easy object model
    Microsoft .NET 2.0 library that conforms to HL7 2.1, 2.2, 2.3, 2.3.1, 2.4, and 2.5 specifications
    Can take a pipe delmimited or XML formated HL7 2.x message and build the C# object model for use in code
    Can take the C# Hl7 object model and produce pipe delimited or XML formatted HL7
    FREE! (You can't beat that price) and open source
    Fast

%prep
%setup -q -n NHapi-%{version}

cat > NHapi.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapi
Description: NHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires: 
Version: 2.4.0.0
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V231.dll
Cflags:
EOF

%build

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapi.Base.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapi.Model.V231.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -m 644 NHapi.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_prefix}/%{libdir}/NHapi.Base.dll
%{_prefix}/%{libdir}/NHapi.Model.V231.dll
%{_datadir}/pkgconfig/NHapi.pc

%changelog
* Mon Aug 13 2012 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


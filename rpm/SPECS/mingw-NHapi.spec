%{?mingw_package_header}

%global mingw_pkg_name NHapi
%global mingw_build_win32 1
%global mingw_build_win64 1

%global debug_package %{nil}

Name:		mingw-NHapi
Version: 	2.3.1
Release: 	4%{?dist}
Summary: 	NHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Group: 		System Environment/Libraries
License: 	MPL 1.1
URL:		http://nhapi.sourceforge.net
Source0: 	%{mingw_pkg_name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch
Requires:  	mono-core

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

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-mono >= 3.0

%description -n mingw32-%{mingw_pkg_name}
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

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-mono >= 3.0

%description -n mingw64-%{mingw_pkg_name}
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
%setup -q -n %{mingw_pkg_name}-%{version}

cat > NHapi32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_libdir}

Name: NHapi
Description: NHapi allows Microsoft .NET developers to easily use an HL7 2.x object model.
Requires: 
Version: 2.4.0.0
Libs: -r:${libdir}/NHapi.Base.dll -r:${libdir}/NHapi.Model.V231.dll
Cflags:
EOF

cat > NHapi64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_libdir}

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

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_libdir}
install -m 755 NHapi.Base.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 755 NHapi.Model.V231.dll $RPM_BUILD_ROOT%{mingw32_libdir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig
install -m 644 NHapi32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/NHapi.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_libdir}
install -m 755 NHapi.Base.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -m 755 NHapi.Model.V231.dll $RPM_BUILD_ROOT%{mingw64_libdir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig
install -m 644 NHapi64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/NHapi.pc


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw32_libdir}/NHapi.Base.dll
%{mingw32_libdir}/NHapi.Model.V231.dll
%{mingw32_datadir}/pkgconfig/NHapi.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw64_libdir}/NHapi.Base.dll
%{mingw64_libdir}/NHapi.Model.V231.dll
%{mingw64_datadir}/pkgconfig/NHapi.pc

%changelog
* Mon Aug 13 2012 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


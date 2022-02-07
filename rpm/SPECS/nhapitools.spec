%global debug_package %{nil}

%define libdir /lib


Name:		NHapiTools
Version: 	1.9.0.0
Release: 	1%{?dist}
Summary: 	The NHapiTools are tools that will make using NHapi easier.
Group: 		System Environment/Libraries
License: 	MIT
URL:		https://github.com/dib0/NHapiTools
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr
BuildArch:	noarch

BuildRequires:	nuget

Requires:  	nHapi

%description
The NHapiTools are tools that will make using NHapi (the open source 
.Net HL7 implementation) easier. NHapi has a steep learning curve and 
not everything works as easy as it should. 
NHapiTools aims to improve that without tampering with NHapi itselves.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > NHapiTools-v281.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V281.dll
Cflags:
EOF

cat > NHapiTools-v28.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V28.dll
Cflags:
EOF

cat > NHapiTools-v271.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V271.dll
Cflags:
EOF

cat > NHapiTools-v27.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V27.dll
Cflags:
EOF

cat > NHapiTools-v26.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V26.dll
Cflags:
EOF

cat > NHapiTools-v251.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V251.dll
Cflags:
EOF

cat > NHapiTools-v25.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V25.dll
Cflags:
EOF

cat > NHapiTools-v24.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V24.dll
Cflags:
EOF

cat > NHapiTools-v231.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier. 
Requires: 
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V231.dll
Cflags:
EOF

cat > NHapiTools-v23.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V23.dll
Cflags:
EOF

cat > NHapiTools-v22.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V22.dll
Cflags:
EOF

cat > NHapiTools-v21.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}/lib

Name: NHapiTools
Description: The NHapiTools are tools that will make using NHapi easier.
Requires:
Version: %{version}
Libs: -r:${libdir}/NHapiTools.Base.dll -r:${libdir}/NHapiTools.Model.V21.dll
Cflags:
EOF


%build

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Base.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V21.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V22.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V23.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V231.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V24.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V25.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V251.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V26.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V27.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V271.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V28.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 755 NHapiTools.%{version}/lib/NHapiTools.Model.V281.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -m 644 NHapiTools-v21.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v22.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v23.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v231.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v24.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v25.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v251.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v26.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v27.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v271.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v28.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 NHapiTools-v281.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_prefix}/%{libdir}/NHapiTools.Base.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V21.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V22.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V23.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V231.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V24.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V25.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V251.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V26.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V27.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V271.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V28.dll
%{_prefix}/%{libdir}/NHapiTools.Model.V281.dll
%{_datadir}/pkgconfig/NHapiTools-v21.pc
%{_datadir}/pkgconfig/NHapiTools-v22.pc
%{_datadir}/pkgconfig/NHapiTools-v23.pc
%{_datadir}/pkgconfig/NHapiTools-v231.pc
%{_datadir}/pkgconfig/NHapiTools-v24.pc
%{_datadir}/pkgconfig/NHapiTools-v25.pc
%{_datadir}/pkgconfig/NHapiTools-v251.pc
%{_datadir}/pkgconfig/NHapiTools-v26.pc
%{_datadir}/pkgconfig/NHapiTools-v27.pc
%{_datadir}/pkgconfig/NHapiTools-v271.pc
%{_datadir}/pkgconfig/NHapiTools-v28.pc
%{_datadir}/pkgconfig/NHapiTools-v281.pc

%changelog
* Sat Apr 21 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


%global debug_package %{nil}

%define libdir /lib

Name:           System.ServiceModel.WCF
Version:        4.6.0
Release:        2%{?dist}
Summary:        WCF libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet/wcf
Prefix:		/usr
BuildArch:	noarch

Provides:	mono(System.ServiceModel.Syndication) = 4.0.0.0
Provides:	mono(System.Security.Cryptography.Xml) = 4.0.1.0
Provides:	mono(System.Security.Cryptography.Pkcs) = 4.0.3.2

%description
Provides the common types used by all of the WCF libraries.
Provides the types that permit SOAP messages to be exchanged using Http (example: BasicHttpBinding).
Provides the types that permit SOAP messages to be exchanged using TCP (example: NetTcpBinding).
Provides the types that permit 2-way ("duplex") exchanges of messages.

%prep
%setup -c %{name}-%{version} -T
nuget install System.Private.ServiceModel -Version %{version}
nuget install System.ServiceModel.Syndication -Version %{version}
nuget install System.Security.Cryptography.Xml -Version %{version}
nuget install System.Security.Cryptography.Pkcs -Version %{version}

nuget install System.ServiceModel.Primitives -Version %{version}
nuget install System.ServiceModel.Http -Version %{version}
nuget install System.ServiceModel.NetTcp -Version %{version}
nuget install System.ServiceModel.Duplex -Version %{version}
nuget install System.ServiceModel.Security -Version %{version}


cat > System.ServiceModel.WCF.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: System.ServiceModel.WCF
Description: System.ServiceModel. Primitives, Http, NetTcp, Duplex, Security
Requires:
Version: %{version}
Libs: -r:${libdir}/System.Private.ServiceModel.dll -r:${libdir}/System.ServiceModel.dll -r:${libdir}/System.ServiceModel.Primitives.dll -r:${libdir}/System.ServiceModel.Http.dll -r:${libdir}/System.ServiceModel.NetTcp.dll -r:${libdir}/System.ServiceModel.Duplex.dll -r:${libdir}/System.ServiceModel.Security.dll -r:${libdir}/System.Reflection.DispatchProxy.dll -r:${libdir}/System.Security.AccessControl.dll -r:${libdir}/System.Security.Cryptography.Pkcs.dll -r:${libdir}/System.Security.Cryptography.Xml.dll -r:${libdir}/System.Security.Permissions.dll -r:${libdir}/System.Security.Principal.Windows.dll -r:${libdir}/System.ServiceModel.Syndication.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 System.ServiceModel.WCF.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll
%{_datadir}/pkgconfig/System.ServiceModel.WCF.pc

%changelog
* Fri Sep 27 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.6.0
- Initial version

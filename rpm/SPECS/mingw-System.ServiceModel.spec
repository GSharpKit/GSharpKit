%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.ServiceModel
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.ServiceModel
Version:        4.8.1
Release:        1%{?dist}
Summary:        WCF libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet/wcf
Prefix:		/usr
BuildArch:	noarch

BuildRequires:	nuget

Requires:	System.Common >= 1.0.0
Requires:	System.Security >= 5.0.0


%description
Provides the common types used by all of the WCF libraries.
Provides the types that permit SOAP messages to be exchanged using Http (example: BasicHttpBinding).
Provides the types that permit SOAP messages to be exchanged using TCP (example: NetTcpBinding).
Provides the types that permit 2-way ("duplex") exchanges of messages.

dotnet tool install --global dotnet-svcutil

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
Provides the common types used by all of the WCF libraries.
Provides the types that permit SOAP messages to be exchanged using Http (example: BasicHttpBinding).
Provides the types that permit SOAP messages to be exchanged using TCP (example: NetTcpBinding).
Provides the types that permit 2-way ("duplex") exchanges of messages.

dotnet tool install --global dotnet-svcutil


%prep
%setup -c %{name}-%{version} -T
nuget install System.Private.ServiceModel -Version %{version}
nuget install System.ServiceModel.Primitives -Version %{version}
nuget install System.ServiceModel.Http -Version %{version}
nuget install System.ServiceModel.NetTcp -Version %{version}
nuget install System.ServiceModel.Duplex -Version %{version}
nuget install System.ServiceModel.Security -Version %{version}

nuget install System.ServiceModel.Syndication -Version 5.0.0


cat > System.ServiceModel.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: System.ServiceModel
Description: System.ServiceModel. Primitives, Http, NetTcp, Duplex, Security
Requires: System.Common System.Security
Version: %{version}
Libs: -r:${libdir}/System.Private.ServiceModel.dll -r:${libdir}/System.ServiceModel.dll -r:${libdir}/System.ServiceModel.Primitives.dll -r:${libdir}/System.ServiceModel.Http.dll -r:${libdir}/System.ServiceModel.NetTcp.dll -r:${libdir}/System.ServiceModel.Duplex.dll -r:${libdir}/System.ServiceModel.Security.dll -r:${libdir}/System.ServiceModel.Syndication.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

rm -rf System.Security.AccessControl.4.5.0
rm -rf System.Security.Cryptography.Xml.4.5.0
rm -rf System.Security.Permissions.4.5.0
rm -rf System.Security.Principal.Windows.4.5.0
rm -rf System.Security.AccessControl.4.7.0
rm -rf System.Security.Cryptography.Xml.4.7.0
rm -rf System.Security.Permissions.4.7.0
rm -rf System.Security.Principal.Windows.4.7.0
rm -rf System.Numerics.Vectors.4.5.0
rm -rf System.Reflection.DispatchProxy.4.7.1

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 System.ServiceModel.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/System.ServiceModel.pc

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.8.1
- Renamed to System.ServiceModel
* Wed Aug 25 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.8.1
- Initial version

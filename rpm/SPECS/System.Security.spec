%global debug_package %{nil}

%define libdir /lib

Name:           System.Security
Version:        5.0.0
Release:        1%{?dist}
Summary:        System Security libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet/wcf
Prefix:		/usr
BuildArch:	noarch

#Provides:	mono(System.Security.Cryptography.Xml) = 4.0.1.0
#Provides:	mono(System.Security.Cryptography.Pkcs) = 4.0.3.2
#Provides:	mono(System.Security.AccessControl) = 4.1.1.0
#Provides:	mono(System.Security.Principal.Windows) = 4.1.1.0

%description
Provides classes to support the creation and validation of XML digital signatures. 
The classes in this namespace implement the World Wide Web Consortium Recommendation, 
"XML-Signature Syntax and Processing", described at http://www.w3.org/TR/xmldsig-core/.

Provides support for PKCS and CMS algorithms.

Provides base classes that enable managing access and audit control lists on securable objects.

Provides classes for retrieving the current Windows user and for interacting with Windows users and groups.

%prep
%setup -c %{name}-%{version} -T
nuget install System.Security.Cryptography.Xml -Version %{version}
nuget install System.Security.Cryptography.Pkcs -Version %{version}
nuget install System.Security.AccessControl -Version %{version}
nuget install System.Security.Principal.Windows -Version %{version}
nuget install System.Security.Permissions -Version %{version}

cat > System.Security.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: System.Security
Description: System.Security
Requires:
Version: %{version}
Libs: -r:${libdir}/System.Security.AccessControl.dll -r:${libdir}/System.Security.Cryptography.Pkcs.dll -r:${libdir}/System.Security.Cryptography.Xml.dll -r:${libdir}/System.Security.Permissions.dll -r:${libdir}/System.Security.Principal.Windows.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 System.Security.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll
%{_datadir}/pkgconfig/System.Security.pc

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.0.0
- Initial version

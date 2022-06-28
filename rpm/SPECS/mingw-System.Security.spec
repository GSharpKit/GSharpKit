%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.Security
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.Security
Version:        6.0.0
Release:        3%{?dist}
Summary:        System Security libraries

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet/wcf
Prefix:		/usr
BuildArch:	noarch

%description
Provides classes to support the creation and validation of XML digital signatures. 
The classes in this namespace implement the World Wide Web Consortium Recommendation, 
"XML-Signature Syntax and Processing", described at http://www.w3.org/TR/xmldsig-core/.

Provides support for PKCS and CMS algorithms.

Provides base classes that enable managing access and audit control lists on securable objects.

Provides classes for retrieving the current Windows user and for interacting with Windows users and groups.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
AutoReqProv:    no

%description -n mingw64-%{mingw_pkg_name}
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
nuget install System.Security.Cryptography.ProtectedData -Version %{version}
nuget install System.Configuration.ConfigurationManager -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
find */lib/net6.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/ \;

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.0.0
- Initial version

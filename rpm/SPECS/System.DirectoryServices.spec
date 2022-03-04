%global debug_package %{nil}

%define libdir /lib

Name:           System.DirectoryServices
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides easy access to Active Directory Domain Services.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet
Prefix:		/usr
BuildArch:	noarch

Requires:	System.Security >= 6.0.0

%description
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

cat > System.DirectoryServices.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: System.DirectoryServices
Description: Provides easy access to Active Directory Domain Services.
Requires: System.Security
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.DirectoryServices.Protocols.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/lib/netstandard2.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/lib/netstandard2.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/lib/netstandard2.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 System.DirectoryServices.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll
%{_datadir}/pkgconfig/System.DirectoryServices.pc

%changelog
* Wed Jul 15 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.7.0
- Initial version

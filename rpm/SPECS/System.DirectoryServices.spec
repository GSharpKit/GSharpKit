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
AutoReqProv:    no

%description
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/lib/net6.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/lib/net6.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/runtimes/linux/lib/net6.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll

%changelog
* Wed Mar 9 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.0
- Use runtime
* Wed Jul 15 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.7.0
- Initial version

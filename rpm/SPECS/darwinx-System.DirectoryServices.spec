%global debug_package %{nil}

%define pkg_name System.DirectoryServices
%define libdir /lib

Name:           darwinx-System.DirectoryServices
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides easy access to Active Directory Domain Services.

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

%description
Provides easy access to Active Directory Domain Services.

%prep
%setup -q -T -c %{name}-%{version}
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/lib/net6.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/lib/net6.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/runtimes/osx/lib/net6.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll

%changelog
* Wed Mar 9 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.0
- Use runtime
* Fri Apr 16 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial version

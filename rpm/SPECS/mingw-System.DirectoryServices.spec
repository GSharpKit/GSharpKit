%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.DirectoryServices
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.DirectoryServices
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides easy access to Active Directory Domain Services.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.DirectoryServices

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  nuget

%description
Provides easy access to Active Directory Domain Services.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:	%{summary}
AutoReqProv:    no
Requires:	mingw64-System.Security >= 6.0.0

%description -n mingw64-%{mingw_pkg_name}
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/runtimes/win/lib/net6.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/runtimes/win/lib/net6.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/runtimes/win/lib/net6.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll

%changelog
* Wed Mar 9 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.0
- Use runtime
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

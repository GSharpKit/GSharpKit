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

Requires:       darwinx-System.Security >= 6.0.0

%description
Provides easy access to Active Directory Domain Services.

%prep
%setup -q -T -c %{name}-%{version}
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

cat > %{pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{pkg_name}
Description: Provides easy access to Active Directory Domain Services.
Requires: System.Security
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.DirectoryServices.Protocols.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/lib/netstandard2.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/lib/netstandard2.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/runtimes/osx/lib/net6.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 %{pkg_name}.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll
%{_darwinx_datadir}/pkgconfig/*.pc


%changelog
* Wed Mar 9 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.0
- Use runtime
* Fri Apr 16 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial version

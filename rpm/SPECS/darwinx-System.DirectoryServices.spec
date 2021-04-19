%global debug_package %{nil}

%define pkg_name System.DirectoryServices
%define libdir /lib

Name:           darwinx-System.DirectoryServices
Version:        5.0.0
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
nuget install %{pkg_name} -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}
nuget install System.Security.Principal.Windows -Version %{version}

cat > %{pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{pkg_name}
Description: Provides easy access to Active Directory Domain Services.
Requires:
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.Security.Principal.Windows.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 %{pkg_name}.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll
%{_darwinx_datadir}/pkgconfig/*.pc


%changelog
* Fri Apr 16 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial version

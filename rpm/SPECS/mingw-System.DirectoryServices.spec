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
Requires:	mingw64-System.Security >= 6.0.0

%description -n mingw64-%{mingw_pkg_name}
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: System.DirectoryServices
Description: %{name} - %{summary}
Requires: System.Security
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.DirectoryServices.Protocols.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.%{version}/lib/netstandard2.0/System.DirectoryServices.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.AccountManagement.%{version}/lib/netstandard2.0/System.DirectoryServices.AccountManagement.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 System.DirectoryServices.Protocols.%{version}/lib/netstandard2.0/System.DirectoryServices.Protocols.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

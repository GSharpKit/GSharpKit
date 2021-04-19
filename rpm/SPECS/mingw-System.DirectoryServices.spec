%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.DirectoryServices
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.DirectoryServices
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides easy access to Active Directory Domain Services.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.DirectoryServices

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Provides easy access to Active Directory Domain Services.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw32-%{mingw_pkg_name}
Provides easy access to Active Directory Domain Services.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}
nuget install System.Security.Principal.Windows -Version %{version}


cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.Security.Principal.Windows.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.Security.Principal.Windows.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/ \;

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/*.dll
%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/*.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

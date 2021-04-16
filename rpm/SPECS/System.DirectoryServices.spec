%global debug_package %{nil}

%define libdir /lib

Name:           System.DirectoryServices
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides easy access to Active Directory Domain Services.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/dotnet
Prefix:		/usr
BuildArch:	noarch

Provides:	mono(System.IO.FileSystem.AccessControl) = 4.0.5.0
Provides:	mono(System.Security.Permissions) = 4.0.3.0


%description
Provides easy access to Active Directory Domain Services.

%prep
%setup -c %{name}-%{version} -T
nuget install System.DirectoryServices -Version %{version}
nuget install System.DirectoryServices.AccountManagement -Version %{version}
nuget install System.Security.Principal.Windows -Version %{version}

cat > System.DirectoryServices.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: System.DirectoryServices
Description: Provides easy access to Active Directory Domain Services.
Requires:
Version: %{version}
Libs: -r:${libdir}/System.DirectoryServices.dll -r:${libdir}/System.DirectoryServices.AccountManagement.dll -r:${libdir}/System.Security.Principal.Windows.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_prefix}%{libdir}/ \;

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

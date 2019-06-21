%global debug_package %{nil}

%define darwinx_pkg_name Seal.net
%define libdir /lib

Name:           darwinx-Seal.net
Version:        4.1.0
Release:        1%{?dist}
Summary:        Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/SealApi/ 
Prefix:		/usr

BuildArch:	noarch

Obsoletes:      darwinx-SealApi
Provides:       darwinx-SealApi

%description
Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.

%prep
%setup -c %{name}-%{version} -T
nuget install Seal.net -Version %{version}

cat > Seal.net.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: SealApi
Description: Seal.net - Seal.net for SAML 
Requires:
Version: %{version}
Libs: -r:${libdir}/Seal.dll -r:${libdir}/DgwsTypes.dll 
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net462/DgwsTypes.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{darwinx_pkg_name}.%{version}/lib/net462/Seal.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 Seal.net.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/Seal.dll
%{_darwinx_prefix}%{libdir}/DgwsTypes.dll
%{_darwinx_datadir}/pkgconfig/Seal.net.pc

%changelog
* Thu Nov 30 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.7-1
- Initial version

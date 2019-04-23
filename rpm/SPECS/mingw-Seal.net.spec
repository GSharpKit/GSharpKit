%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Seal.net
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 4.1.0.0

Name:           mingw-Seal.net
Version:        4.1.0
Release:        1%{?dist}
Summary:        Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Seal.net/ 
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:	%{summary}
Obsoletes:	mingw32-SealApi
Provides:	mingw32-SealApi

%description -n mingw32-%{mingw_pkg_name}
Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:	%{summary}
Obsoletes:	mingw64-SealApi
Provides:	mingw64-SealApi

%description -n mingw64-%{mingw_pkg_name}
Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.


%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS.
Requires:
Version: %{version}
Libs: -r:${libdir}/Seal.dll -r:${libdir}/DgwsTypes.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{mingw_pkg_name} - Seal.NET er et API som har til formål at lette udviklingen af software som overholder DGWS. 
Requires:
Version: %{version}
Libs: -r:${libdir}/Seal.dll -r:${libdir}/DgwsTypes.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net462/DgwsTypes.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net462/Seal.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net462/DgwsTypes.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net462/Seal.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Seal.dll
%{mingw32_prefix}%{libdir}/DgwsTypes.dll
%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Seal.dll
%{mingw64_prefix}%{libdir}/DgwsTypes.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc


%changelog
* Wed Apr 10 2019 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.1.0-1
- Updated to official Seal.net NuGet package

* Thu Nov 30 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.7-1
- Initial version

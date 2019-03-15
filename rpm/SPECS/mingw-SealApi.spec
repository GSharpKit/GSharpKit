%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name SealApi
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 2.0.0.0

Name:           mingw-SealApi
Version:        2.0.7
Release:        1%{?dist}
Summary:        SealApi for SAML

Group:          Development/Languages
License:        LGPL
URL:            https://github.com/openmedicus/SealApi
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.0.0

%description
SealApi for SAML

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw32-%{mingw_pkg_name}
SealApi for SAML

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
SealApi for SAML


%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > SealApi32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: %{name}
Description: %{name} - SealApi for SAML 
Requires:
Version: %{version}
Libs: -r:${libdir}/SealApi.dll -r:${libdir}/Microsoft.Web.Services3.dll
Cflags:
EOF

cat > SealApi64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: %{name}
Description: %{name} - SealApi for SAML
Requires:
Version: %{version}
Libs: -r:${libdir}/SealApi.dll -r:${libdir}/Microsoft.Web.Services3.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 SealApi.%{version}/lib/net461/SealApi.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Microsoft.Web.Services3.3.0.0.0/lib/net20/Microsoft.Web.Services3.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 SealApi32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/SealApi.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 SealApi.%{version}/lib/net461/SealApi.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Microsoft.Web.Services3.3.0.0.0/lib/net20/Microsoft.Web.Services3.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 SealApi64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/SealApi.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/SealApi.dll
%{mingw32_prefix}%{libdir}/Microsoft.Web.Services3.dll
%{mingw32_datadir}/pkgconfig/SealApi.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/SealApi.dll
%{mingw64_prefix}%{libdir}/Microsoft.Web.Services3.dll
%{mingw64_datadir}/pkgconfig/SealApi.pc


%changelog
* Thu Nov 30 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.7-1
- Initial version

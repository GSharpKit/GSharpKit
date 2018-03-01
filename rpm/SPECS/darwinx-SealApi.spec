%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-SealApi
Version:        2.0.7
Release:        1%{?dist}
Summary:        SealApi for SAML

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/SealApi/ 
Prefix:		/usr

BuildArch:	noarch

Requires:	darwinx-mono-core >= 4.0.0

%description
SealApi for SAML

%prep
%setup -c %{name}-%{version} -T
nuget install SealApi -Version %{version}

cat > SealApi.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: SealApi
Description: SealApi - SealApi for SAML 
Requires:
Version: %{version}
Libs: -r:${libdir}/mono/SealApi/SealApi.dll -r:${libdir}/Microsoft.Web.Services3.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i SealApi.%{version}/lib/net461/SealApi.dll -package SealApi -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 Microsoft.Web.Services3.3.0.0.0/lib/net20/Microsoft.Web.Services3.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 SealApi.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/SealApi/SealApi.dll
%{_darwinx_prefix}%{libdir}/Microsoft.Web.Services3.dll
%{_darwinx_datadir}/pkgconfig/SealApi.pc

%changelog
* Thu Nov 30 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.7-1
- Initial version

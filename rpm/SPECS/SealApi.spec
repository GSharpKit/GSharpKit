%global debug_package %{nil}

%define libdir /lib
%define apiversion 2.0.0.0

Name:           SealApi
Version:        2.0.7
Release:        1%{?dist}
Summary:        SealApi for SAML

Group:          Development/Languages
License:        MIT
URL:            http://npgsql.projects.pgfoundry.org/
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.0.0

%description
SealApi for SAML

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > SealApi.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{name} - SealApi for SAML 
Requires:
Version: %{version}
Libs: -r:${libdir}/mono/%{name}/%{name}.dll -r:${libdir}/Microsoft.Web.Services3.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

gacutil -i %{name}.%{version}/lib/net461/%{name}.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 Microsoft.Web.Services3.3.0.0.0/lib/net20/Microsoft.Web.Services3.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 SealApi.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/%{name}.dll
%{_prefix}%{libdir}/Microsoft.Web.Services3.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Nov 30 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.7-1
- Initial version

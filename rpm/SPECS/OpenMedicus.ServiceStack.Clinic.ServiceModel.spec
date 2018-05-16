%global debug_package %{nil}

%define libdir /lib
%define api_version 0.0.0.0

Name:           OpenMedicus.ServiceStack.Clinic.ServiceModel
Version:        2.4.12
Release:        1%{?dist}
Summary:        ServiceStack access to XMedicus Healthcare System

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/OpenMedicus.ServiceStack.Clinic.ServiceModel/
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 3.0.0
Requires:	mono-data >= 3.0.0
Requires:	ServiceStack >= 5.0.2

%description
ServiceStack access to XMedicus Healthcare System

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: ServiceStack access to XMedicus Healthcare System 
Requires:
Version: %{api_version}
Libs: -r:${libdir}/%{name}/%{name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i OpenMedicus.ServiceStack.Clinic.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.Clinic.ServiceModel.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.Clinic.ServiceModel.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/OpenMedicus.ServiceStack.Clinic.ServiceModel.dll
%{_datadir}/pkgconfig/OpenMedicus.ServiceStack.Clinic.ServiceModel.pc


%changelog
* Fri May 11 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.12-1
- Initial version

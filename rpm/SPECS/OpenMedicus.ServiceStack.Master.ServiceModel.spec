%global debug_package %{nil}

%define libdir /lib
%define api_version 0.0.0.0

Name:           OpenMedicus.ServiceStack.Master.ServiceModel
Version:        1.2.3
Release:        1%{?dist}
Summary:        ServiceStack access to Master Healthcare System

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/OpenMedicus.ServiceStack.Master.ServiceModel/
Prefix:		/usr
BuildArch:	noarch

Requires:	mono-core >= 3.0.0
Requires:	mono-data >= 3.0.0
Requires:	ServiceStack >= 5.0.2

%description
ServiceStack access to Master Healthcare System

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: ServiceStack access to Master Healthcare System 
Requires: ServiceStack
Version: %{api_version}
Libs: -r:${libdir}/%{name}/%{name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i OpenMedicus.ServiceStack.Master.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.Master.ServiceModel.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.Master.ServiceModel.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/OpenMedicus.ServiceStack.Master.ServiceModel.dll
%{_datadir}/pkgconfig/OpenMedicus.ServiceStack.Master.ServiceModel.pc


%changelog
* Fri May 11 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.2.3-1
- Initial version

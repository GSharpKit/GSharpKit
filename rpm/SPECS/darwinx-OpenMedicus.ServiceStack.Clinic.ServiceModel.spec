%global debug_package %{nil}

%define darwinx_pkg_name OpenMedicus.ServiceStack.Clinic.ServiceModel

%define libdir /lib

Name:           darwinx-OpenMedicus.ServiceStack.Clinic.ServiceModel
Version:        2.4.12
Release:        2%{?dist}
Summary:        ServiceStack access to Clinic Healthcare System

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/OpenMedicus.ServiceStack.Clinic.ServiceModel/
Prefix:		/usr
BuildArch:	noarch

Requires:	darwinx-ServiceStack >= 5.0.2

%description
ServiceStack access to Clinic Healthcare System

%prep
%setup -c %{darwinx_pkg_name}-%{version} -T
nuget install %{darwinx_pkg_name} -Version %{version}

cat > %{darwinx_pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{darwinx_pkg_name}
Description: ServiceStack access to Clinic Healthcare System 
Requires: ServiceStack
Version: %{version}
Libs: -r:${libdir}/%{darwinx_pkg_name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 OpenMedicus.ServiceStack.Clinic.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.Clinic.ServiceModel.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.Clinic.ServiceModel.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/OpenMedicus.ServiceStack.Clinic.ServiceModel.dll
%{_darwinx_datadir}/pkgconfig/OpenMedicus.ServiceStack.Clinic.ServiceModel.pc


%changelog
* Fri May 11 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.12-1
- Initial version

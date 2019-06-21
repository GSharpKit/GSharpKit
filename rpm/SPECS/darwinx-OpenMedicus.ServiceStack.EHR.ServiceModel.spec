%global debug_package %{nil}

%define darwinx_pkg_name OpenMedicus.ServiceStack.EHR.ServiceModel

%define libdir /lib

Name:           darwinx-OpenMedicus.ServiceStack.EHR.ServiceModel
Version:        1.0.34
Release:        2%{?dist}
Summary:        ServiceStack access to EHR Healthcare System

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/OpenMedicus.ServiceStack.EHR.ServiceModel/
Prefix:		/usr
BuildArch:	noarch

Requires:	darwinx-ServiceStack >= 5.5.0

%description
ServiceStack access to EHR Healthcare System

%prep
%setup -c %{darwinx_pkg_name}-%{version} -T
nuget install %{darwinx_pkg_name} -Version %{version}

cat > %{darwinx_pkg_name}.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: %{darwinx_pkg_name}
Description: ServiceStack access to EHR Healthcare System 
Requires: ServiceStack
Version: %{version}
Libs: -r:${libdir}/%{darwinx_pkg_name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 OpenMedicus.ServiceStack.EHR.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.EHR.ServiceModel.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.EHR.ServiceModel.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/OpenMedicus.ServiceStack.EHR.ServiceModel.dll
%{_darwinx_datadir}/pkgconfig/OpenMedicus.ServiceStack.EHR.ServiceModel.pc


%changelog
* Fri May 11 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.12-1
- Initial version

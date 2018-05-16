%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name OpenMedicus.ServiceStack.Master.ServiceModel
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define api_version 0.0.0.0

Name:           mingw-OpenMedicus.ServiceStack.Master.ServiceModel
Version:        1.2.3
Release:        1%{?dist}
Summary:        ServiceStack access to Master Healthcare System

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/OpenMedicus.ServiceStack.Master.ServiceModel/
Prefix:		/usr
BuildArch:	noarch


%description
ServiceStack access to Master Healthcare System

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono
Requires:	mingw32-ServiceStack >= 5.0.2

%description -n mingw32-%{mingw_pkg_name}
ServiceStack access to Master Healthcare System

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono
Requires:	mingw64-ServiceStack >= 5.0.2

%description -n mingw64-%{mingw_pkg_name}
ServiceStack access to Master Healthcare System

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: %{mingw_pkg_name}
Description: ServiceStack access to Master Healthcare System 
Requires: ServiceStack
Version: %{api_version}
Libs: -r:${libdir}/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: %{mingw_pkg_name}
Description: ServiceStack access to Master Healthcare System
Requires: ServiceStack
Version: %{api_version}
Libs: -r:${libdir}/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i OpenMedicus.ServiceStack.Master.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.Master.ServiceModel.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.Master.ServiceModel32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/OpenMedicus.ServiceStack.Master.ServiceModel.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i OpenMedicus.ServiceStack.Master.ServiceModel.%{version}/lib/net461/OpenMedicus.ServiceStack.Master.ServiceModel.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 OpenMedicus.ServiceStack.Master.ServiceModel64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/OpenMedicus.ServiceStack.Master.ServiceModel.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/OpenMedicus.ServiceStack.Master.ServiceModel.dll
%{mingw32_datadir}/pkgconfig/OpenMedicus.ServiceStack.Master.ServiceModel.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/OpenMedicus.ServiceStack.Master.ServiceModel.dll
%{mingw64_datadir}/pkgconfig/OpenMedicus.ServiceStack.Master.ServiceModel.pc

%changelog
* Fri May 11 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.4.12-1
- Initial version
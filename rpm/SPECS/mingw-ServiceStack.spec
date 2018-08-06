%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name ServiceStack
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:           mingw-ServiceStack
Version:        5.1.0
Release:        1%{?dist}
Summary:        ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.

Group:          Development/Languages
License:        Copyright 2017 ServiceStack
URL:            https://www.nuget.org/packages/ServiceStack
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

Requires:	mono-core >= 4.0.0

%description
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework 
for all your services and web apps that's intuitive and Easy to use!

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono-core

%description -n mingw32-%{mingw_pkg_name}
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework
for all your services and web apps that's intuitive and Easy to use!

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono-core

%description -n mingw64-%{mingw_pkg_name}
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework
for all your services and web apps that's intuitive and Easy to use!

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > ServiceStack32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: ServiceStack
Description: ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.
Requires:
Version: %{version}
Libs: -r:${libdir}/ServiceStack/ServiceStack.dll -r:${libdir}/ServiceStack.Common/ServiceStack.Common.dll -r:${libdir}/ServiceStack.Client/ServiceStack.Client.dll -r:${libdir}/ServiceStack.Text/ServiceStack.Text.dll -r:${libdir}/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
Cflags:
EOF

cat > ServiceStack.Interfaces32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: ServiceStack.Interfaces
Description: Lightweight and implementation-free interfaces for DTO's, providers and adapters.
Requires:
Version: %{version}
Libs: -r:${libdir}/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
Cflags:
EOF

cat > ServiceStack64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: ServiceStack
Description: ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.
Requires:
Version: %{version}
Libs: -r:${libdir}/ServiceStack/ServiceStack.dll -r:${libdir}/ServiceStack.Common/ServiceStack.Common.dll -r:${libdir}/ServiceStack.Client/ServiceStack.Client.dll -r:${libdir}/ServiceStack.Text/ServiceStack.Text.dll -r:${libdir}/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
Cflags:
EOF

cat > ServiceStack.Interfaces64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: ServiceStack.Interfaces
Description: Lightweight and implementation-free interfaces for DTO's, providers and adapters.
Requires:
Version: %{version}
Libs: -r:${libdir}/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i ServiceStack.%{version}/lib/net45/ServiceStack.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Common.%{version}/lib/net45/ServiceStack.Common.dll -package %{mingw_pkg_name}.Common -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Client.%{version}/lib/net45/ServiceStack.Client.dll -package %{mingw_pkg_name}.Client -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Text.%{version}/lib/net45/ServiceStack.Text.dll -package %{mingw_pkg_name}.Text -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Interfaces.%{version}/lib/net45/ServiceStack.Interfaces.dll -package %{mingw_pkg_name}.Interfaces -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 ServiceStack32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/ServiceStack.pc
install -m 644 ServiceStack.Interfaces32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/ServiceStack.Interfaces.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i ServiceStack.%{version}/lib/net45/ServiceStack.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Common.%{version}/lib/net45/ServiceStack.Common.dll -package %{mingw_pkg_name}.Common -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Client.%{version}/lib/net45/ServiceStack.Client.dll -package %{mingw_pkg_name}.Client -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Text.%{version}/lib/net45/ServiceStack.Text.dll -package %{mingw_pkg_name}.Text -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac
gacutil -i ServiceStack.Interfaces.%{version}/lib/net45/ServiceStack.Interfaces.dll -package %{mingw_pkg_name}.Interfaces -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 ServiceStack64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/ServiceStack.pc
install -m 644 ServiceStack.Interfaces64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/ServiceStack.Interfaces.pc



%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/ServiceStack/ServiceStack.dll
%{mingw32_prefix}%{libdir}/mono/ServiceStack.Common/ServiceStack.Common.dll
%{mingw32_prefix}%{libdir}/mono/ServiceStack.Client/ServiceStack.Client.dll
%{mingw32_prefix}%{libdir}/mono/ServiceStack.Text/ServiceStack.Text.dll
%{mingw32_prefix}%{libdir}/mono/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
%{mingw32_datadir}/pkgconfig/ServiceStack.pc
%{mingw32_datadir}/pkgconfig/ServiceStack.Interfaces.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/ServiceStack/ServiceStack.dll
%{mingw64_prefix}%{libdir}/mono/ServiceStack.Common/ServiceStack.Common.dll
%{mingw64_prefix}%{libdir}/mono/ServiceStack.Client/ServiceStack.Client.dll
%{mingw64_prefix}%{libdir}/mono/ServiceStack.Text/ServiceStack.Text.dll
%{mingw64_prefix}%{libdir}/mono/ServiceStack.Interfaces/ServiceStack.Interfaces.dll
%{mingw64_datadir}/pkgconfig/ServiceStack.pc
%{mingw64_datadir}/pkgconfig/ServiceStack.Interfaces.pc


%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.1.0-1
- Update to 5.1.0

* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-ServiceStack
Version:        5.5.0
Release:        1%{?dist}
Summary:        ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.

Group:          Development/Languages
License:        Copyright 2017 ServiceStack
URL:            https://www.nuget.org/packages/ServiceStack
Prefix:		/usr

BuildArch:	noarch

%description
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework 
for all your services and web apps that's intuitive and Easy to use!

%prep
%setup -c %{name}-%{version} -T
nuget install ServiceStack -Version %{version}

cat > ServiceStack.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: ServiceStack
Description: ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.
Requires:
Version: %{version}
Libs: -r:${libdir}/System.Numerics.Vectors.dll -r:${libdir}/System.Buffers.dll -r:${libdir}/System.Memory.dll -r:${libdir}/ServiceStack.dll -r:${libdir}/ServiceStack.Common.dll -r:${libdir}/ServiceStack.Client.dll -r:${libdir}/ServiceStack.Text.dll -r:${libdir}/ServiceStack.Interfaces.dll 
Cflags:
EOF

cat > ServiceStack.Interfaces.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: ServiceStack.Interfaces
Description: Lightweight and implementation-free interfaces for DTO's, providers and adapters.
Requires:
Version: %{version}
Libs: -r:${libdir}/ServiceStack.Interfaces.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.%{version}/lib/net45/ServiceStack.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Common.%{version}/lib/net45/ServiceStack.Common.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Client.%{version}/lib/net45/ServiceStack.Client.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Text.%{version}/lib/net45/ServiceStack.Text.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Interfaces.%{version}/lib/net45/ServiceStack.Interfaces.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 ServiceStack.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 ServiceStack.Interfaces.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/ServiceStack.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Common.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Client.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Text.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Interfaces.dll

%{_darwinx_datadir}/pkgconfig/ServiceStack.pc
%{_darwinx_datadir}/pkgconfig/ServiceStack.Interfaces.pc

%changelog
* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

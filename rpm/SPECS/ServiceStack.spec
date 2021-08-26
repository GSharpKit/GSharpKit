#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:           ServiceStack
Version:        5.12.0
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

%prep
%setup -c %{name}-%{version} -T
nuget install %{name}.Core -Version %{version}

cat > ServiceStack.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: ServiceStack
Description: ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.
Requires: System.Common
Version: %{version}
Libs: -r:${libdir}/ServiceStack.dll -r:${libdir}/ServiceStack.Common.dll -r:${libdir}/ServiceStack.Client.dll -r:${libdir}/ServiceStack.Text.dll -r:${libdir}/ServiceStack.Interfaces.dll
Cflags:
EOF

cat > ServiceStack.Interfaces.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

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

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 ServiceStack.Core.%{version}/lib/netstandard2.0/ServiceStack.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Common.Core.%{version}/lib/netstandard2.0/ServiceStack.Common.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Client.Core.%{version}/lib/netstandard2.0/ServiceStack.Client.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Text.Core.%{version}/lib/netstandard2.0/ServiceStack.Text.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Interfaces.Core.%{version}/lib/netstandard2.0/ServiceStack.Interfaces.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 ServiceStack.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 ServiceStack.Interfaces.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/ServiceStack.dll
%{_prefix}%{libdir}/ServiceStack.Common.dll
%{_prefix}%{libdir}/ServiceStack.Client.dll
%{_prefix}%{libdir}/ServiceStack.Text.dll
%{_prefix}%{libdir}/ServiceStack.Interfaces.dll
%{_datadir}/pkgconfig/ServiceStack.pc
%{_datadir}/pkgconfig/ServiceStack.Interfaces.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.1.0-1
- Update to 5.1.0

* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

#sudo mozroots --import --machine --sync
#sudo certmgr -ssl -m https://go.microsoft.com
#sudo certmgr -ssl -m https://nugetgallery.blob.core.windows.net
#sudo certmgr -ssl -m https://nuget.org

%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:           ServiceStack
Version:        6.1.0
Release:        1%{?dist}
Summary:        ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.

Group:          Development/Languages
License:        Copyright 2017 ServiceStack
URL:            https://www.nuget.org/packages/ServiceStack
Prefix:		/usr

BuildArch:	noarch
AutoReqProv:    no

BuildRequires:  nuget

%description
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework 
for all your services and web apps that's intuitive and Easy to use!

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 ServiceStack.%{version}/lib/net6.0/ServiceStack.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Common.%{version}/lib/net6.0/ServiceStack.Common.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Client.%{version}/lib/net6.0/ServiceStack.Client.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Text.%{version}/lib/net6.0/ServiceStack.Text.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/
install -m 644 ServiceStack.Interfaces.%{version}/lib/net6.0/ServiceStack.Interfaces.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/ServiceStack.dll
%{_prefix}%{libdir}/ServiceStack.Common.dll
%{_prefix}%{libdir}/ServiceStack.Client.dll
%{_prefix}%{libdir}/ServiceStack.Text.dll
%{_prefix}%{libdir}/ServiceStack.Interfaces.dll

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.1.0-1
- Update to 5.1.0

* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

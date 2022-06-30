%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-ServiceStack
Version:        6.1.0
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

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.%{version}/lib/net6.0/ServiceStack.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Common.%{version}/lib/net6.0/ServiceStack.Common.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Client.%{version}/lib/net6.0/ServiceStack.Client.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Text.%{version}/lib/net6.0/ServiceStack.Text.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 ServiceStack.Interfaces.%{version}/lib/net6.0/ServiceStack.Interfaces.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/ServiceStack.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Common.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Client.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Text.dll
%{_darwinx_prefix}%{libdir}/ServiceStack.Interfaces.dll

%changelog
* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

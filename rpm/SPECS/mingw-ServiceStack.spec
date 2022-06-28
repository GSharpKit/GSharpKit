%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name ServiceStack
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-ServiceStack
Version:        6.1.0
Release:        1%{?dist}
Summary:        ServiceStack webservice framework: Faster, Cleaner, Modern WCF alternative.

Group:          Development/Languages
License:        Copyright 2017 ServiceStack
URL:            https://www.nuget.org/packages/ServiceStack
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

%description
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework 
for all your services and web apps that's intuitive and Easy to use!

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
AutoReqProv:    no

%description -n mingw64-%{mingw_pkg_name}
A simple and fast alternative to WCF, MVC and Web API in one cohesive framework
for all your services and web apps that's intuitive and Easy to use!

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 ServiceStack.%{version}/lib/net6.0/ServiceStack.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 ServiceStack.Common.%{version}/lib/net6.0/ServiceStack.Common.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 ServiceStack.Client.%{version}/lib/net6.0/ServiceStack.Client.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 ServiceStack.Text.%{version}/lib/net6.0/ServiceStack.Text.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 ServiceStack.Interfaces.%{version}/lib/net6.0/ServiceStack.Interfaces.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/ServiceStack.dll
%{mingw64_prefix}%{libdir}/ServiceStack.Common.dll
%{mingw64_prefix}%{libdir}/ServiceStack.Client.dll
%{mingw64_prefix}%{libdir}/ServiceStack.Text.dll
%{mingw64_prefix}%{libdir}/ServiceStack.Interfaces.dll

%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 5.1.0-1
- Update to 5.1.0

* Thu Nov 23 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.14-1
- Initial version

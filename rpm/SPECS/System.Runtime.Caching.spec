%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib

Name:           System.Runtime.Caching
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides classes to use caching facilities.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.Runtime.Caching
Prefix:		/usr
BuildArch:	noarch
AutoReqProv:    no

%description
Provides classes to use caching facilities.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.Runtime.Caching.%{version}/lib/net6.0/System.Runtime.Caching.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/System.Runtime.Caching.dll


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

%global debug_package %{nil}

%define pkg_name System.Runtime.Caching
%define libdir /lib

Name:           darwinx-System.Runtime.Caching
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides classes to use caching facilities.

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Prefix:		/usr

BuildArch:	noarch

%description
Provides classes to use caching facilities.

%prep
%setup -q -T -c %{name}-%{version}
nuget install %{pkg_name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 %{pkg_name}.%{version}/lib/net6.0/%{pkg_name}.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll


%changelog
* Fri Apr 16 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial version

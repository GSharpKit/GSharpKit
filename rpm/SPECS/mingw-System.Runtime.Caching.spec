%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.Runtime.Caching
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-System.Runtime.Caching
Version:        6.0.0
Release:        1%{?dist}
Summary:        Provides classes to use caching facilities.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.Runtime.Caching

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  nuget

%description
Provides classes to use caching facilities.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
AutoReqProv:    no

%description -n mingw64-%{mingw_pkg_name}
Provides classes to use caching facilities.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/net6.0/%{mingw_pkg_name}.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/%{mingw_pkg_name}.dll

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

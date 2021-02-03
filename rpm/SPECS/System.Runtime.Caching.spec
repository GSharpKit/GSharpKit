%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define libdir /lib
%define api_version 5.0.0.0

Name:           System.Runtime.Caching
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides classes to use caching facilities.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.Runtime.Caching
Prefix:		/usr
BuildArch:	noarch

%description
Provides classes to use caching facilities.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > System.Runtime.Caching.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: System.Runtime.Caching
Description: Provides classes to use caching facilities.
Requires:
Version: %{api_version}
Libs: -r:${libdir}/System.Runtime.Caching.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 System.Runtime.Caching.%{version}/lib/netstandard2.0/System.Runtime.Caching.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 System.Runtime.Caching.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/System.Runtime.Caching.dll
%{_datadir}/pkgconfig/System.Runtime.Caching.pc


%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

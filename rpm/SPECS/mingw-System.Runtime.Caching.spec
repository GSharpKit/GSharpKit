%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name System.Runtime.Caching
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 4.7.0.0

Name:           mingw-System.Runtime.Caching
Version:        5.0.0
Release:        1%{?dist}
Summary:        Provides classes to use caching facilities.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/System.Runtime.Caching

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Provides classes to use caching facilities.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw32-%{mingw_pkg_name}
Provides classes to use caching facilities.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}

%description -n mingw64-%{mingw_pkg_name}
Provides classes to use caching facilities.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > %{mingw_pkg_name}32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/%{mingw_pkg_name}.dll
Cflags:
EOF

cat > %{mingw_pkg_name}64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/%{mingw_pkg_name}.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/netstandard2.0/%{mingw_pkg_name}.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 %{mingw_pkg_name}.%{version}/lib/netstandard2.0/%{mingw_pkg_name}.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 %{mingw_pkg_name}64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/%{mingw_pkg_name}.dll
%{mingw32_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/%{mingw_pkg_name}.dll
%{mingw64_datadir}/pkgconfig/%{mingw_pkg_name}.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version

%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Newtonsoft.Json
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 11.0.0.0

Name:           mingw-Newtonsoft.Json
Version:        11.0.2
Release:        3%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Json.NET is a popular high-performance JSON framework for .NET

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Obsoletes:      mingw32-newtonsoft-json
Provides:       mingw32-newtonsoft-json

%description -n mingw32-%{mingw_pkg_name}
Json.NET is a popular high-performance JSON framework for .NET

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Obsoletes:      mingw64-newtonsoft-json
Provides:       mingw64-newtonsoft-json

%description -n mingw64-%{mingw_pkg_name}
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > Newtonsoft.Json32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Newtonsoft.Json
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Newtonsoft.Json.dll
Cflags:
EOF

cat > Newtonsoft.Json64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Newtonsoft.Json
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Newtonsoft.Json.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Newtonsoft.Json.%{version}/lib/netstandard2.0/Newtonsoft.Json.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Newtonsoft.Json.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Newtonsoft.Json.%{version}/lib/netstandard2.0/Newtonsoft.Json.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Newtonsoft.Json64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Newtonsoft.Json.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Newtonsoft.Json.dll
%{mingw32_datadir}/pkgconfig/Newtonsoft.Json.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Newtonsoft.Json.dll
%{mingw64_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 11.0.2-1
- Fixed API version to 11.0.0.0

* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 11.0.2-1
- Updated to 11.0.2

* Thu Sep 7 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 10.0.3-1
- Initial version

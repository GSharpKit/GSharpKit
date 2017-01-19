%{?mingw_package_header}

%global mingw_pkg_name Newtonsoft.Json
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:           mingw-Newtonsoft.Json
Version:        9.0.1
Release:        1%{?dist}
Summary:        Json.NET is a popular high-performance JSON framework for .NET

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/
Source0:        Newtonsoft.Json-%{version}.tar.gz
Prefix:         /usr

BuildRequires:	mingw32-filesystem
BuildRequires:	mingw64-filesystem

BuildArch:	noarch

%description
Json.NET is a popular high-performance JSON framework for .NET

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-mono >= 3.0
Obsoletes:      mingw32-newtonsoft-json
Provides:       mingw32-newtonsoft-json

%description -n mingw32-%{mingw_pkg_name}
Json.NET is a popular high-performance JSON framework for .NET


# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-mono >= 3.0
Obsoletes:      mingw64-newtonsoft-json
Provides:       mingw64-newtonsoft-json

%description -n mingw64-%{mingw_pkg_name}
Json.NET is a popular high-performance JSON framework for .NET

%prep
%setup -q -n %{mingw_pkg_name}-%{version}

cat > Newtonsoft.Json-32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_libdir}

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{version}
Libs: -r:${libdir}/mono/Newtonsoft.Json/Newtonsoft.Json.dll
Cflags:
EOF

cat > Newtonsoft.Json-64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_libdir}

Name: Newtonsoft.Json
Description: Json.NET is a popular high-performance JSON framework for .NET
Requires:
Version: %{version}
Libs: -r:${libdir}/mono/Newtonsoft.Json/Newtonsoft.Json.dll
Cflags:
EOF


%build
cd Src/Newtonsoft.Json
xbuild Newtonsoft.Json.Net40.csproj                     \
/property:SignAssembly=true                             \
/property:AssemblyOriginatorKeyFile=Dynamic.snk         \
/property:Configuration=Release                         \
/property:DefineConstants='SIGNED NET40'

%install
%{__rm} -rf %{buildroot}


gacutil -i Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll -f -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_libdir}
gacutil -i Src/Newtonsoft.Json/bin/Release/Net40/Newtonsoft.Json.dll -f -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/

install -m 644 Newtonsoft.Json-32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Newtonsoft.Json.pc
install -m 644 Newtonsoft.Json-64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Newtonsoft.Json.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll
%{mingw32_libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll.mdb
%{mingw32_libdir}/mono/Newtonsoft.Json/Newtonsoft.Json.dll
%{mingw32_datadir}/pkgconfig/Newtonsoft.Json.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll
%{mingw64_libdir}/mono/gac/Newtonsoft.Json/*/Newtonsoft.Json.dll.mdb
%{mingw64_libdir}/mono/Newtonsoft.Json/Newtonsoft.Json.dll
%{mingw64_datadir}/pkgconfig/Newtonsoft.Json.pc


%changelog
* Wed Jul 02 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5-1
- Initial version

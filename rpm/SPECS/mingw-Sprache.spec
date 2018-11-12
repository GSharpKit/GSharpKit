%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Sprache
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 2.1.2.0

Name:           mingw-Sprache
Version:        2.2.0
Release:        1%{?dist}
Summary:        Sprache is a simple, lightweight library for constructing parsers directly in C# code

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Sprache is a simple, lightweight library for constructing parsers directly in C# code

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono

%description -n mingw32-%{mingw_pkg_name}
Sprache is a simple, lightweight library for constructing parsers directly in C# code

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono

%description -n mingw64-%{mingw_pkg_name}
Sprache is a simple, lightweight library for constructing parsers directly in C# code

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name}.Signed -Version %{version}

cat > Sprache32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: Sprache
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Sprache/Sprache.Signed.dll
Cflags:
EOF

cat > Sprache64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: Sprache
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Sprache/Sprache.Signed.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i Sprache.Signed.%{version}/lib/netstandard2.0/Sprache.Signed.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Sprache32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Sprache.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i Sprache.Signed.%{version}/lib/netstandard2.0/Sprache.Signed.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Sprache64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Sprache.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/Sprache/Sprache.Signed.dll
%{mingw32_datadir}/pkgconfig/Sprache.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/Sprache/Sprache.Signed.dll
%{mingw64_datadir}/pkgconfig/Sprache.pc


%changelog
* Mon Oct 01 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.1.2-1
- Initial version

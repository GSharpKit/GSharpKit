%{?mingw_package_header}

%global mingw_pkg_name Mono.Addins.Setup
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:		mingw-Mono.Addins.Setup
Version:	1.3.8
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		http://www.mono-project.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

BuildRequires:  mingw32-filesystem mingw64-filesystem
BuildRequires:	nuget

%description
Mono.Addins.Setup is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-mono-core >= 5.14
Requires:	mingw32-SharpZipLib >= 1.0.0

%description -n mingw32-%{mingw_pkg_name}
Mono.Addins.Setup is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-mono-core >= 5.14
Requires:	mingw64-SharpZipLib >= 1.0.0

%description -n mingw64-%{mingw_pkg_name}
Mono.Addins.Setup is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.


%prep

%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > mono-addins-setup32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: %{mingw_pkg_name}
Description: %{summary}
Requires: SharpZipLib
Version: %{version}
Libs: -r:${libdir}/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
Cflags:
EOF

cat > mono-addins-setup64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: %{mingw_pkg_name}
Description: %{summary}
Requires: SharpZipLib
Version: %{version}
Libs: -r:${libdir}/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i %{mingw_pkg_name}.%{version}/lib/net45/%{mingw_pkg_name}.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 mono-addins-setup32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/mono-addins-setup.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i %{mingw_pkg_name}.%{version}/lib/net45/%{mingw_pkg_name}.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 mono-addins-setup64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/mono-addins-setup.pc

%clean
%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name} 
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
%{mingw32_datadir}/pkgconfig/mono-addins-setup.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/%{mingw_pkg_name}/%{mingw_pkg_name}.dll
%{mingw64_datadir}/pkgconfig/mono-addins-setup.pc

%changelog
* Thu Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.3.8-1
- Initial build


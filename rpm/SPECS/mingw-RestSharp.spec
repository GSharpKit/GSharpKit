%{?mingw_package_header}

%global mingw_pkg_name RestSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define platform netstandard2.0

Name:		mingw-RestSharp
Version: 	106.11.4
Release: 	1%{?dist}
Summary: 	Simple REST and HTTP API Client
Group: 		System Environment/Libraries
License: 	Apache License
URL:		http://sourceforge.net/projects/sharpssh/
Source0: 	Apache-LICENSE.txt
BuildArch:      noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildRequires:	nuget
Requires:	mono-core

%description
Simple REST and HTTP API Client

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw32-%{mingw_pkg_name}
Simple REST and HTTP API Client

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw64-%{mingw_pkg_name}
Simple REST and HTTP API Client

%prep
%setup -c %{mingw_pkg_name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > RestSharp32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: RestSharp
Description: Simple REST and HTTP API Client
Requires: 
Version: %{version}
Libs: -r:${libdir}/RestSharp.dll
Cflags:
EOF

cat > RestSharp64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: RestSharp
Description: Simple REST and HTTP API Client
Requires:
Version: %{version}
Libs: -r:${libdir}/RestSharp.dll
Cflags:
EOF


%build

%install  
rm -rf $RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 RestSharp.%{version}/lib/%{platform}/RestSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/RestSharp
install -m 664 %{SOURCE0} $RPM_BUILD_ROOT%{mingw32_datadir}/RestSharp/License

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig
install -m 644 RestSharp32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/RestSharp.pc

# Mingw32 
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 RestSharp.%{version}/lib/%{platform}/RestSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/RestSharp
install -m 664 %{SOURCE0} $RPM_BUILD_ROOT%{mingw64_datadir}/RestSharp/License

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig
install -m 644 RestSharp64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/RestSharp.pc


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw32_datadir}/RestSharp/License
%{mingw32_prefix}%{libdir}/RestSharp.dll
%{mingw32_datadir}/pkgconfig/RestSharp.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw64_datadir}/RestSharp/License
%{mingw64_prefix}%{libdir}/RestSharp.dll
%{mingw64_datadir}/pkgconfig/RestSharp.pc

%changelog
* Fri Aug 3 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 106.3.1-1
- Updated to 106.3.1

* Wed May 03 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


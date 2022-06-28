%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Sprache
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define apiversion 2.2.0.0

Name:           mingw-Sprache
Version:        2.2.0
Release:        1%{?dist}
Summary:        Sprache is a simple, lightweight library for constructing parsers directly in C# code

Group:          Development/Languages
License:        MIT
URL:            http://json.codeplex.com/

Prefix:		/usr
BuildArch:	noarch
AutoReqProv:    no

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Sprache is a simple, lightweight library for constructing parsers directly in C# code

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
AutoReqProv:    no

%description -n mingw64-%{mingw_pkg_name}
Sprache is a simple, lightweight library for constructing parsers directly in C# code

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name}.Signed -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Sprache.Signed.%{version}/lib/netstandard2.0/Sprache.Signed.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Sprache.Signed.dll

%changelog
* Mon Oct 01 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.1.2-1
- Initial version

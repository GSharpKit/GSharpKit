%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name MimeKit
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-MimeKit
Version:        3.3.0
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MimeKit

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  nuget


%description
MimeKit is an Open Source library for creating and parsing MIME,
S/MIME and PGP messages on desktop and mobile platforms.
It also supports parsing of Unix mbox files.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:	%{summary}
Requires:       mingw64-System.Security >= 6.0.0
Requires:       mingw64-BouncyCastle >= 1.9.0
AutoReqProv:    no


%description -n mingw64-%{mingw_pkg_name}
MimeKit is an Open Source library for creating and parsing MIME,
S/MIME and PGP messages on desktop and mobile platforms.
It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MimeKit.%{version}/lib/net6.0/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/MimeKit.dll

%changelog
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6

* Fri Aug 03 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5

* Thu Sep 7 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version

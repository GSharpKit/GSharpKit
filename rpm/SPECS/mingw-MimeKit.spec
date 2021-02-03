%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name MimeKit
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin

Name:           mingw-MimeKit
Version:        2.10.1
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MimeKit

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget


%description
MimeKit is an Open Source library for creating and parsing MIME,
S/MIME and PGP messages on desktop and mobile platforms.
It also supports parsing of Unix mbox files.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-BouncyCastle

%description -n mingw32-%{mingw_pkg_name}
MimeKit is an Open Source library for creating and parsing MIME,
S/MIME and PGP messages on desktop and mobile platforms.
It also supports parsing of Unix mbox files.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-BouncyCastle

%description -n mingw64-%{mingw_pkg_name}
MimeKit is an Open Source library for creating and parsing MIME,
S/MIME and PGP messages on desktop and mobile platforms.
It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > MimeKit32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: MimeKit
Description: %{name} - %{summary}
Requires: BouncyCastle
Version: %{version}
Libs: -r:${libdir}/MimeKit.dll
Cflags:
EOF

cat > MimeKit64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: MimeKit
Description: %{name} - %{summary}
Requires: BouncyCastle
Version: %{version}
Libs: -r:${libdir}/MimeKit.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 MimeKit.%{version}/lib/netstandard2.0/MimeKit.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 MimeKit32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/MimeKit.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 MimeKit.%{version}/lib/netstandard2.0/MimeKit.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 MimeKit64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/MimeKit.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/MimeKit.dll
%{mingw32_datadir}/pkgconfig/MimeKit.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/MimeKit.dll
%{mingw64_datadir}/pkgconfig/MimeKit.pc


%changelog
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6

* Fri Aug 03 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5

* Thu Sep 7 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version

%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-MimeKit
Version:        2.1.4
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-BouncyCastle

%description
MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages on desktop 
and mobile platforms. It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install MimeKit -Version %{version}

cat > MimeKit.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: MimeKit
Description: %{summary} 
Requires: BouncyCastle
Version: %{version}
Libs: -r:${libdir}/MimeKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 MimeKit.%{version}/lib/net45/MimeKit.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 MimeKit.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/MimeKit.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/MimeKit.dll
%{_darwinx_datadir}/pkgconfig/MimeKit.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

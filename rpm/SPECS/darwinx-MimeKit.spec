%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-MimeKit
Version:        2.15.0
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:       darwinx-System.Common >= 1.0.0
Requires:       darwinx-System.Security >= 5.0.0
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
Requires: System.Common System.Security BouncyCastle
Version: %{version}
Libs: -r:${libdir}/MimeKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/ \;

rm $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/BouncyCastle.Crypto.dll
rm $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/System.Buffers.dll

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 MimeKit.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/MimeKit.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/*.dll
%{_darwinx_datadir}/pkgconfig/MimeKit.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

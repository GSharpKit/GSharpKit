%global debug_package %{nil}

%define libdir /lib

Name:           MimeKit
Version:        2.10.1
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MimeKit
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

Requires:	BouncyCastle >= 1.8.8

%description
MimeKit is an Open Source library for creating and parsing MIME, 
S/MIME and PGP messages on desktop and mobile platforms. 
It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}
nuget install System.Text.Encoding.CodePages -Version 4.4.0
nuget install System.Data.DataSetExtensions -Version 4.5.0
nuget install System.Reflection.TypeExtensions -Version 4.4.0
nuget install System.Security.Cryptography.Pkcs -Version 4.7.0

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{name} - %{summary}
Requires: BouncyCastle
Version: %{version}
Libs: -r:${libdir}/MimeKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
find */lib/netstandard2.0/ -iname "*.dll" -exec install -m 644 {} $RPM_BUILD_ROOT%{_prefix}%{libdir}/ \;

rm $RPM_BUILD_ROOT%{_prefix}%{libdir}/BouncyCastle.Crypto.dll
rm $RPM_BUILD_ROOT%{_prefix}%{libdir}/System.Buffers.dll

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Dec 11 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.10.1-1
- Updated to netstandard2.0
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5
* Mon Aug 18 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version

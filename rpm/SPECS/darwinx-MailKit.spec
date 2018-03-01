%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-MailKit
Version:        1.22.0
Release:        1%{?dist}
Summary:        MailKit is an Open Source cross-platform .NET mail-client library.
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-mono-core >= 4.8
Requires:	darwinx-MimeKit

%description
MailKit is an Open Source cross-platform .NET mail-client library that is based on 
MimeKit and optimized for mobile devices.

%prep
%setup -c %{name}-%{version} -T
nuget install MailKit -Version %{version}

cat > MailKit.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: MailKit
Description: %{summary} 
Requires: MimeKit 
Version: %{version}
Libs: -r:${libdir}/MailKit/MailKit.dll
Cflags:
EOF

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/mono/gac
gacutil -i MailKit.%{version}/lib/net45/MailKit.dll -package MailKit -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 MailKit.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/MailKit.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/MailKit/MailKit.dll
%{_darwinx_datadir}/pkgconfig/MailKit.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

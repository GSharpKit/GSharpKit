%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-MailKit
Version:        2.15.0
Release:        1%{?dist}
Summary:        MailKit is an Open Source cross-platform .NET mail-client library.
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
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
libdir=%{_darwinx_prefix}%{libdir}

Name: MailKit
Description: %{summary} 
Requires: MimeKit 
Version: %{version}
Libs: -r:${libdir}/MailKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 MailKit.%{version}/lib/netstandard2.0/MailKit.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 MailKit.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/MailKit.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/MailKit.dll
%{_darwinx_datadir}/pkgconfig/MailKit.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

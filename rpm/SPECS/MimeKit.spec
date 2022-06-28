%global debug_package %{nil}

%define _binary_payload w2.xzdio

%define libdir /lib

Name:           MimeKit
Version:        3.3.0
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MimeKit
Prefix:		/usr

BuildArch:	noarch
AutoReqProv:    no

BuildRequires:  nuget

Requires:	System.Security >= 6.0.0
Requires:	BouncyCastle >= 1.9.0

%description
MimeKit is an Open Source library for creating and parsing MIME, 
S/MIME and PGP messages on desktop and mobile platforms. 
It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 MimeKit.%{version}/lib/net6.0/*.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/*.dll

%changelog
* Thu Aug 26 2021 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.15
- Updated to use System.Common and System.Security
* Fri Dec 11 2020 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.10.1-1
- Updated to netstandard2.0
* Fri Aug 17 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.6-1
- Update to 2.0.6
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5
* Mon Aug 18 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version

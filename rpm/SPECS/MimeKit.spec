%global debug_package %{nil}

%define libdir /lib

Name:           MimeKit
Version:        2.0.5
Release:        1%{?dist}
Summary:        MimeKit is an Open Source library for creating and parsing MIME, S/MIME and PGP messages.

Group:          Development/Languages
License:        MIT
URL:            https://github.com/jstedfast/MimeKit
Prefix:		/usr

BuildArch:	noarch

BuildRequires:  nuget

Requires:	mono-core >= 4.8.0
Requires:	BouncyCastle >= 1.8.2

%description
MimeKit is an Open Source library for creating and parsing MIME, 
S/MIME and PGP messages on desktop and mobile platforms. 
It also supports parsing of Unix mbox files.

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

cat > %{name}.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}/mono

Name: %{name}
Description: %{name} - %{summary}
Requires: BouncyCastle
Version: %{version}
Libs: -r:Facades/netstandard.dll -r:${libdir}/%{name}/MimeKit.dll
Cflags:
EOF

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/mono/gac
gacutil -i MimeKit.%{version}/lib/netstandard2.0/MimeKit.dll -package %{name} -root $RPM_BUILD_ROOT%{_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/mono/gac
%{_prefix}%{libdir}/mono/%{name}/MimeKit.dll
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.5-1
- Update to 2.0.5
* Mon Aug 18 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.18.0-1
- Initial version

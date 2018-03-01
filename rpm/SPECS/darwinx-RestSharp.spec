%global debug_package %{nil}

%define libdir /lib

Name:           darwinx-RestSharp
Version:        105.2.3
Release:        1%{?dist}
Summary:        Simple REST and HTTP API Client
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
Simple REST and HTTP API Client

%prep
%setup -c %{name}-%{version} -T
nuget install RestSharpSigned -Version %{version}

cat > RestSharp.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}/mono

Name: RestSharp
Description: %{summary} 
Requires: MimeKit 
Version: %{version}
Libs: -r:${libdir}/RestSharp/RestSharp.dll
Cflags:
EOF

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}/mono/gac
gacutil -i RestSharpSigned.%{version}/lib/net45/RestSharp.dll -package RestSharp -root $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 RestSharp.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/RestSharp.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/mono/gac
%{_darwinx_prefix}%{libdir}/mono/RestSharp/RestSharp.dll
%{_darwinx_datadir}/pkgconfig/RestSharp.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

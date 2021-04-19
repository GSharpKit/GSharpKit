%global debug_package %{nil}

%define libdir /lib
%define platform netstandard2.0

Name:           darwinx-RestSharp
Version:        106.11.7
Release:        1%{?dist}
Summary:        Simple REST and HTTP API Client
Group:          Development/Languages
License:        MIT
URL:            https://github.com/npgsql/npgsql/archive

Prefix:		/usr
BuildArch:	noarch

BuildRequires:	darwinx-filesystem-base >= 18

Requires:	darwinx-filesystem >= 18
Requires:	darwinx-MimeKit

%description
Simple REST and HTTP API Client

%prep
%setup -c %{name}-%{version} -T
nuget install RestSharp -Version %{version}

cat > RestSharp.pc << \EOF
prefix=%{_darwinx_prefix}
exec_prefix=${prefix}
libdir=%{_darwinx_prefix}%{libdir}

Name: RestSharp
Description: %{summary} 
Requires: MimeKit 
Version: %{version}
Libs: -r:${libdir}/RestSharp.dll
Cflags:
EOF

%build

%install

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}
install -m 644 RestSharp.%{version}/lib/%{platform}/RestSharp.dll $RPM_BUILD_ROOT%{_darwinx_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/
install -m 644 RestSharp.pc $RPM_BUILD_ROOT%{_darwinx_datadir}/pkgconfig/RestSharp.pc

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_darwinx_prefix}%{libdir}/RestSharp.dll
%{_darwinx_datadir}/pkgconfig/RestSharp.pc

%changelog
* Mon Jan  8 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.1-1
- Initial version

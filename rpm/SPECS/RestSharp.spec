%define _binary_payload w2.xzdio

%define debug_package %{nil}

%define libdir /lib

Name:		RestSharp
Version: 	106.15.0
Release: 	1%{?dist}
Summary: 	Simple REST and HTTP API Client
Group: 		System Environment/Libraries
License: 	Apache License
URL:		http://sourceforge.net/projects/sharpssh/
Source0: 	Apache-LICENSE.txt
BuildArch:      noarch
AutoReqProv:    no
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildRequires:	nuget

%description
Simple REST and HTTP API Client

%prep
%setup -c %{name}-%{version} -T
nuget install %{name} -Version %{version}

%build

%install  
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 RestSharp.%{version}/lib/netstandard2.0/RestSharp.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/RestSharp
install -m 664 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/RestSharp/License

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_datadir}/RestSharp/License
%{_prefix}%{libdir}/RestSharp.dll

%changelog
* Thu Aug 02 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 106.3.1-1
- Updated to 106.3.1

* Fri Nov 24 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define cefname cef_binary_112.3.0+gb09c4ca+chromium-112.0.5615.165_linux64_client

%define libdir /lib

Name:           libcef
Version:        112.3.0
Release:        1%{?dist}
Summary:        Chromium Embedded Framework (CEF)
Group:          Development/Languages
License:        AsIs
URL:            https://cef-builds.spotifycdn.com/ 
Prefix:		/usr
Source0:	%{cefname}.tar.bz2

BuildArch:	x86_64
AutoReqProv:    no

%description
Chromium Embedded Framework (CEF). A simple framework for embedding Chromium-based 
browsers in other applications.

%prep
%setup -q -n %{cefname} 

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef
install -m 755 Release/*.* $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef/
install -m 755 Release/cefsimple $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef/
install -m 755 Release/chrome-sandbox $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef/

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef/locales
install -m 644 Release/locales/* $RPM_BUILD_ROOT%{_prefix}%{libdir}/cef/locales/

%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_prefix}%{libdir}/cef
%{_prefix}%{libdir}/cef/cefsimple
%{_prefix}%{libdir}/cef/chrome-sandbox
%{_prefix}%{libdir}/cef/*.*

%dir %{_prefix}%{libdir}/cef/locales
%{_prefix}%{libdir}/cef/locales/*


%changelog
* Sat Apr 15 2023 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 110.0.29-1
- Updated
* Sat Apr 8 2023 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 102.0.3-1
- Initial version

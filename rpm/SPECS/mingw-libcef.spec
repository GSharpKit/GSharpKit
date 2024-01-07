%{?mingw_package_header}

%global mingw_build_win32 0
%global mingw_build_win64 1

%define _binary_payload w2.xzdio

%global debug_package %{nil}

%define cefname cef_binary_112.3.0+gb09c4ca+chromium-112.0.5615.165_windows64_client

%define libdir /bin

Name:           mingw-libcef
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

%package -n mingw64-libcef
Summary:        Chromium Embedded Framework (CEF)

%description -n mingw64-libcef
Chromium Embedded Framework (CEF). A simple framework for embedding Chromium-based
browsers in other applications.

%prep
%setup -q -n %{cefname} 

%build

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/cef
install -m 755 Release/*.* $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/cef/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/cef/locales
install -m 644 Release/locales/* $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/cef/locales/

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw64-libcef
%defattr(-,root,root,-)
%dir %{mingw64_prefix}%{libdir}/cef
%{mingw64_prefix}%{libdir}/cef/*.*

%dir %{mingw64_prefix}%{libdir}/cef/locales
%{mingw64_prefix}%{libdir}/cef/locales/*


%changelog
* Sat Apr 8 2023 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 102.0.3-1
- Initial version

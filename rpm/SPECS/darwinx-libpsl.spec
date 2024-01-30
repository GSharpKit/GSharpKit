Name:           darwinx-libpsl
Version:        0.21.5
Release:        1%{?dist}
Summary:        C Library for the Public Suffix List

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/rockdaboot/libpsl
Source0:        libpsl-%{version}.tar.gz
Source1:	list-5db9b65997e3c9230ac4353b01994c2ae9667cb9.zip

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc

Requires:  	darwinx-filesystem >= 18

%description
A Public Suffix List is a collection of Top Level Domains (TLDs) suffixes. 
TLDs include Global Top Level Domains (gTLDs) like .com and .net; Country 
Top Level Domains (ccTLDs) like .de and .cn; and Brand Top Level Domains 
like .apple and .google. Brand TLDs allows users to register their own top 
level domain that exist at the same level as ICANN's gTLDs. Brand TLDs are 
sometimes referred to as Vanity Domains.

%prep
%setup -q -n libpsl-%{version}

unzip %{SOURCE1}
rm -rf list
mv list-5db9b65997e3c9230ac4353b01994c2ae9667cb9 list

%build
%darwinx_meson \
    -Ddocs=false \
    -Dtests=false

%darwinx_meson_build

%install
%darwinx_meson_install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/man

%files
%defattr(-,root,wheel,-)
%{_darwinx_bindir}/psl
%{_darwinx_libdir}/libpsl.dylib
%{_darwinx_libdir}/libpsl.5.dylib
%{_darwinx_libdir}/pkgconfig/libpsl.pc
%{_darwinx_includedir}/libpsl.h

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

Name:           darwinx-libpsl
Version:        0.21.0
Release:        1%{?dist}
Summary:        C Library for the Public Suffix List

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/rockdaboot/libpsl
Source0:        libpsl-%{version}.tar.gz

BuildArch:      noarch

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

%package static
Summary:        Static version of the C Library for the Public Suffix List 
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
A Public Suffix List is a collection of Top Level Domains (TLDs) suffixes.
TLDs include Global Top Level Domains (gTLDs) like .com and .net; Country
Top Level Domains (ccTLDs) like .de and .cn; and Brand Top Level Domains
like .apple and .google. Brand TLDs allows users to register their own top
level domain that exist at the same level as ICANN's gTLDs. Brand TLDs are
sometimes referred to as Vanity Domains.

%prep
%setup -q -n libpsl-%{version}

%build
%{_darwinx_configure} --disable-nls

%{_darwinx_make} %{?_smp_mflags} V=1


%install
%{_darwinx_make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_darwinx_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/man

%files -n darwinx-libpsl
%defattr(-,root,root,-)
%{_darwinx_bindir}/psl
%{_darwinx_libdir}/libpsl.dylib
%{_darwinx_libdir}/libpsl.5.dylib
%{_darwinx_libdir}/pkgconfig/libpsl.pc
%{_darwinx_includedir}/libpsl.h

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libpsl.a

%changelog
* Tue Nov 04 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.0-1
- Initial RPM release

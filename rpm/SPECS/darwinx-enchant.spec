Name:           darwinx-enchant
Version:        1.6.0
Release:        1%{?dist}
Summary:        On the surface, Enchant appears to be a generic spell checking library

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            http://www.abisource.com/downloads/enchant/1.6.0
Source0:        enchant-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 12
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
On the surface, Enchant appears to be a generic spell checking library

%prep
%setup -q -n enchant-%{version}

%build
%{_darwinx_configure} \
  --disable-static

%{_darwinx_make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/enchant
%{_darwinx_bindir}/enchant-lsmod
%{_darwinx_libdir}/libenchant.*.dylib
%{_darwinx_libdir}/libenchant.dylib
%{_darwinx_libdir}/libenchant.la
%{_darwinx_libdir}/enchant/libenchant_ispell.la
%{_darwinx_libdir}/enchant/libenchant_ispell.so
%{_darwinx_libdir}/enchant/libenchant_myspell.la
%{_darwinx_libdir}/enchant/libenchant_myspell.so
%{_darwinx_libdir}/pkgconfig/enchant.pc
%{_darwinx_includedir}/

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.6-1
- Initial RPM release.


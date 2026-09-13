Name:           darwinx-gsm
Version:        1.0.22
Release:        1%{?dist}
Summary:        GSM 06.10 lossy speech compression
License:        BSD
Group:          Development/Libraries
URL:            https://www.quut.com/gsm/
Source0:        https://www.quut.com/gsm/gsm-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
GSM 06.10 lossy speech compression

%prep
%setup -q -n gsm-1.0-pl22

%build
#{_darwinx_make} gsminstall

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_darwinx_prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_darwinx_prefix}/lib
make INSTALL_ROOT=$RPM_BUILD_ROOT%{_darwinx_prefix} gsminstall

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/*
%dir %{_darwinx_includedir}/speex
%{_darwinx_includedir}/speex/*
%{_darwinx_libdir}/libspeex.*.dylib
%{_darwinx_libdir}/libspeex.dylib
%{_darwinx_libdir}/pkgconfig/speex.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4.2-1
- Initial RPM release.

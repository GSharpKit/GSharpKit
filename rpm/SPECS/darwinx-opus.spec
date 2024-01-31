Name:           darwinx-opus
Version:        1.2.1
Release:        1%{?dist}
Summary:        Opus is a totally open, royalty-free, highly versatile audio codec.
License:        BSD
Group:          Development/Libraries
URL:            https://opus-codec.org/
Source0:        https://downloads.xiph.org/releases/opus/opus-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
Opus is a totally open, royalty-free, highly versatile audio codec. 
Opus is unmatched for interactive speech and music transmission over the Internet, 
but is also intended for storage and streaming applications. It is standardized by 
the Internet Engineering Task Force (IETF) as RFC 6716 which incorporated 
technology from Skype’s SILK codec and Xiph.Org’s CELT codec.

%prep
%setup -q -n opus-%{version}

%build
%{_darwinx_configure} \
	--disable-static

%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install program_transform_name=""

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%dir %{_darwinx_includedir}/opus
%{_darwinx_includedir}/opus/*
%{_darwinx_libdir}/libopus.*.dylib
%{_darwinx_libdir}/libopus.dylib
%{_darwinx_libdir}/pkgconfig/opus.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4.2-1
- Initial RPM release.

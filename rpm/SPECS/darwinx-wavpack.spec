Name:           darwinx-wavpack
Version:        5.8.1
Release:        1%{?dist}
Summary:        WavPack is a completely open audio compression format
License:        BSD
Group:          Development/Libraries
URL:            https://www.wavpack.com
Source0:        https://www.wavpack.com/wavpack-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
WavPack is a completely open audio compression format providing lossless, 
high-quality lossy, and a unique hybrid compression mode. 

%prep
%setup -q -n wavpack-%{version}

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
%{_darwinx_bindir}/*
%dir %{_darwinx_includedir}/wavpack
%{_darwinx_includedir}/wavpack/*
%{_darwinx_libdir}/libwavpack.*.dylib
%{_darwinx_libdir}/libwavpack.dylib
%{_darwinx_libdir}/pkgconfig/wavpack.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4.2-1
- Initial RPM release.

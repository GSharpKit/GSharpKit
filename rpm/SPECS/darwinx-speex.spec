Name:           darwinx-speex
Version:        1.2.1
Release:        1%{?dist}
Summary:        Speex is an Open Source/Free Software patent-free audio compression format designed for speech
License:        BSD
Group:          Development/Libraries
URL:            https://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/speex-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
Speex is an Open Source/Free Software patent-free audio compression 
format designed for speech

%prep
%setup -q -n speex-%{version}

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-assembly \
	--enable-libwebpdecoder

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
%dir %{_darwinx_includedir}/speex
%{_darwinx_includedir}/speex/*
%{_darwinx_libdir}/libspeex.*.dylib
%{_darwinx_libdir}/libspeex.dylib
%{_darwinx_libdir}/pkgconfig/speex.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.4.2-1
- Initial RPM release.

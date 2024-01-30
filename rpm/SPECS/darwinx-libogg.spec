Name:           darwinx-libogg
Version:        1.3.5
Release:        1%{?dist}
Summary:        The Ogg bitstream file format library
License:        BSD
Group:          Development/Libraries
URL:            http://www.xiph.org/downloads/
Source:         http://downloads.xiph.org/releases/ogg/libogg-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams

%prep
%setup -q -n libogg-%{version}

%build
%{_darwinx_configure} \
	--disable-static
%{_darwinx_make}

%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libogg*.dylib
%dir %{_darwinx_includedir}/ogg
%{_darwinx_includedir}/ogg/*.h
%{_darwinx_libdir}/pkgconfig/ogg.pc

%changelog

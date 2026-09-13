Name:           darwinx-libtheora
Version:        1.2.0
Release:        1%{?dist}
Summary:        Theora is a free and open video compression format
License:        BSD
Group:          Development/Libraries
URL:            https://www.theora.org/
Source:         http://downloads.xiph.org/releases/theora/libtheora-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

%description
Theora is a free and open video compression format

%prep
%setup -q -n libtheora-%{version}

%build
%{_darwinx_configure} \
	--disable-static

%{_darwinx_make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_make} DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libtheora*.dylib
%dir %{_darwinx_includedir}/theora
%{_darwinx_includedir}/theora/*.h
%{_darwinx_libdir}/pkgconfig/*.pc

%changelog

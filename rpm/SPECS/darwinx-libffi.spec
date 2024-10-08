Name:           darwinx-libffi
Version:        3.4.4
Release:        1%{?dist}
Summary:        A portable foreign function interface library

License:        LGPLv2+
Group:          Development/Libraries
URL:            ftp://sourceware.org/pub/libffi
Source0:        ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 106
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
Compilers for high level languages generate code that follows certain conventions. 
These conventions are necessary, in part, for separate compilation to work. 
One such convention is the "calling convention". The "calling convention" is a set 
of assumptions made by the compiler about where function arguments will be found on 
entry to a function. A "calling convention" also specifies where the return value 
for a function is found. 

%prep
%setup -q -n libffi-%{version}


%build
%{_darwinx_configure} \
	--disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libffi.dylib
%{_darwinx_libdir}/libffi.*.dylib
%{_darwinx_includedir}/ffi.h
%{_darwinx_includedir}/ffitarget.h
%{_darwinx_libdir}/pkgconfig/libffi.pc

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.0.13-1
- Initial RPM release

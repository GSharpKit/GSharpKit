Name:           darwinx-gmp
Version:        6.1.0
Release:        1%{?dist}
Summary:        A GNU arbitrary precision library
License:        LGPLv3+
Group:          Development/Libraries
URL:            https://gmplib.org/download/gmp/
Source0:        gmp-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libgpg-error
BuildRequires:  darwinx-libgcrypt >= 1.5.2
BuildRequires:  darwinx-gettext

BuildRequires:  pkgconfig

Requires:  	darwinx-filesystem >= 18

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%prep
%setup -q -n gmp-%{version}

%build
%{_darwinx_configure} --disable-static --disable-assembly
%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_darwinx_includedir}/gmp.h
%{_darwinx_libdir}/libgmp.10.dylib
%{_darwinx_libdir}/libgmp.dylib
%{_darwinx_libdir}/libgmp.la

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 6.0.0-1
- Initial RPM release.

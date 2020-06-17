Name:           darwinx-libunistring
Version:        0.9.10
Release:        1%{?dist}
Summary:        This library provides functions for manipulating Unicode strings.

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            https://www.gnu.org/software/libunistring/
Source0:        libunistring-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
This library provides functions for manipulating Unicode strings 
and for manipulating C strings according to the Unicode standard. 

%prep
%setup -q -n libunistring-%{version}

%build
%{_darwinx_configure} \
  --disable-static

%{_darwinx_make}
# %{?_smp_mflags} doesn't build correctly.


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_infodir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_darwinx_includedir}/unicase.h
%{_darwinx_includedir}/uniconv.h
%{_darwinx_includedir}/unictype.h
%{_darwinx_includedir}/unigbrk.h
%{_darwinx_includedir}/unilbrk.h
%{_darwinx_includedir}/uniname.h
%{_darwinx_includedir}/uninorm.h
%{_darwinx_includedir}/unistdio.h
%{_darwinx_includedir}/unistr.h
%{_darwinx_includedir}/unitypes.h
%{_darwinx_includedir}/uniwbrk.h
%{_darwinx_includedir}/uniwidth.h
%dir %{_darwinx_includedir}/unistring
%{_darwinx_includedir}/unistring/
%{_darwinx_libdir}/libunistring.2.dylib
%{_darwinx_libdir}/libunistring.dylib
%{_darwinx_libdir}/libunistring.la

%changelog
* Sat Jan  6 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.8-1
- Initial RPM release.


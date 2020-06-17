Name:           darwinx-pcre
Version:        8.44
Release:        1%{?dist}
Summary:        Perl-compatible regular expression library

License:        BSD
Group:          System Environment/Libraries
URL:            http://www.pcre.org/
Source0:        ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
PCRE, Perl-compatible regular expression, library has its own native API, but
a set of wrapper functions that are based on the POSIX API are also supplied
in the libpcreposix library. Note that this just provides a POSIX calling
interface to PCRE: the regular expressions themselves still follow Perl syntax
and semantics. Detailed change log is provided by pcre-doc package.

%package static
Summary:        Perl-compatible regular expression library
Requires:       %{name} = %{version}-%{release}
Group:          System Environment/Libraries

%description static
RE, Perl-compatible regular expression, library has its own native API, but
a set of wrapper functions that are based on the POSIX API are also supplied
in the libpcreposix library. Note that this just provides a POSIX calling
interface to PCRE: the regular expressions themselves still follow Perl syntax
and semantics. Detailed change log is provided by pcre-doc package.

%prep
%setup -q -n pcre-%{version}

%build
%{_darwinx_configure} --enable-unicode-properties --enable-utf
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/pcre-config
%{_darwinx_bindir}/pcregrep
%{_darwinx_bindir}/pcretest
%{_darwinx_libdir}/libpcre.dylib
%{_darwinx_libdir}/libpcre.*.dylib
%{_darwinx_libdir}/libpcre.la
%{_darwinx_libdir}/libpcrecpp.dylib
%{_darwinx_libdir}/libpcrecpp.*.dylib
%{_darwinx_libdir}/libpcrecpp.la
%{_darwinx_libdir}/libpcreposix.dylib
%{_darwinx_libdir}/libpcreposix.*.dylib
%{_darwinx_libdir}/libpcreposix.la
%{_darwinx_includedir}/*.h
%{_darwinx_libdir}/pkgconfig/*.pc

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libpcre.a
%{_darwinx_libdir}/libpcrecpp.a
%{_darwinx_libdir}/libpcreposix.a

%changelog
* Wed Jul 20 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 8.39-1
- Initial RPM release

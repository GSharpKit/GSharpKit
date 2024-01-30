Name:           darwinx-pcre2
Version:        10.42
Release:        1%{?dist}
Summary:        Perl-compatible regular expression library

License:        BSD
Group:          System Environment/Libraries
URL:            http://www.pcre.org/
Source0:        ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre2-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
PCRE, Perl-compatible regular expression, library has its own native API, but
a set of wrapper functions that are based on the POSIX API are also supplied
in the libpcreposix library. Note that this just provides a POSIX calling
interface to PCRE: the regular expressions themselves still follow Perl syntax
and semantics. Detailed change log is provided by pcre-doc package.

%prep
%setup -q -n pcre2-pcre2-%{version}

%build
NOCONFIGURE=yes sh autogen.sh
%{_darwinx_configure}§

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/pcre2-config
%{_darwinx_bindir}/pcre2grep
%{_darwinx_bindir}/pcre2test
%{_darwinx_libdir}/libpcre2-8.dylib
%{_darwinx_libdir}/libpcre2-8.*.dylib
%{_darwinx_libdir}/libpcre2-posix.dylib
%{_darwinx_libdir}/libpcre2-posix.*.dylib
%{_darwinx_includedir}/*.h
%{_darwinx_libdir}/pkgconfig/*.pc

%changelog
* Wed Jul 20 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 8.39-1
- Initial RPM release

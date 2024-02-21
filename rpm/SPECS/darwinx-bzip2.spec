Name:           darwinx-bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        The bzip2 file compression program

License:        As-is
Group:          Development/Libraries
URL:            http://www.bzip.org
Source0:        https://github.com/libarchive/bzip2/archive/refs/tags/bzip2-bzip2-%{version}.tar.gz
Source1:	Makefile-libbz2_dylib
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem >= 7
BuildRequires:  darwinx-gcc

BuildRequires:  pkgconfig

%description
The bzip2 file compression program

%prep
%setup -q -n bzip2-bzip2-%{version}

cp %{SOURCE1} .

%build
%{_darwinx_make}
%{_darwinx_make} -f Makefile-libbz2_dylib


%install
rm -rf $RPM_BUILD_ROOT

make PREFIX=$RPM_BUILD_ROOT%{_darwinx_prefix} install
make -f Makefile-libbz2_dylib PREFIX=$RPM_BUILD_ROOT%{_darwinx_prefix} install

rm -rf $RPM_BUILD_ROOT%{_darwinx_prefix}/man
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/*.a

rm -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzcmp
rm -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzegrep
rm -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzfgrep
rm -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzless

cp -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzdiff $RPM_BUILD_ROOT%{_darwinx_bindir}/bzcmp
cp -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzgrep $RPM_BUILD_ROOT%{_darwinx_bindir}/bzegrep
cp -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzgrep $RPM_BUILD_ROOT%{_darwinx_bindir}/bzfgrep
cp -f $RPM_BUILD_ROOT%{_darwinx_bindir}/bzmore $RPM_BUILD_ROOT%{_darwinx_bindir}/bzless

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_darwinx_bindir}/bunzip2
%{_darwinx_bindir}/bzcat
%{_darwinx_bindir}/bzdiff
%{_darwinx_bindir}/bzgrep
%{_darwinx_bindir}/bzip2
%{_darwinx_bindir}/bzip2recover
%{_darwinx_bindir}/bzmore
%{_darwinx_bindir}/bzcmp
%{_darwinx_bindir}/bzegrep
%{_darwinx_bindir}/bzfgrep
%{_darwinx_bindir}/bzless
%{_darwinx_includedir}/*
%{_darwinx_libdir}/libbz2.*.dylib
%{_darwinx_libdir}/libbz2.dylib

%changelog
* Sat Jan  6 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.9.8-1
- Initial RPM release.


%define debug_package %{nil}

%define _prefix /Library/Frameworks/AppBox.framework/Versions/1.0.0

Name: 		darwinx-filesystem-base
Version: 	102
Release: 	1%{?dist}
Summary: 	Darwin filesystem and environment
License: 	GPLv2+
Group: 		Development/Libraries
URL: 		http://www.appbox.info
Source0:	macros.darwinx
Source1:	macros.dist
Source2:	darwinx.sh
Source3:	zlib.pc
Source4:	sqlite3.pc

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

Requires:	darwinx-filesystem = %{version}

Provides:       darwinx-gcc
Provides:       darwinx-odcctools
Provides:       darwinx-sdk
Provides:       autoconf, automake, libtool
Provides:	bison, flex, m4, gperf, ruby, perl

%description
This package contains the base filesystem layout, RPM macros and
environment for Darwin (Mac OS X) cross-compiler packages.


%prep
%setup -q -c -T

%build
# nothing


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/etc/profile.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/etc/rpm

cp %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/etc/rpm/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/etc/rpm/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_prefix}/etc/profile.d/

mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig

cp %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/
cp %{SOURCE4} $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_prefix}/etc/profile.d/darwinx.sh
%{_prefix}/etc/rpm/macros.darwinx
%{_prefix}/etc/rpm/macros.dist
%{_prefix}/lib/pkgconfig/zlib.pc
%{_prefix}/lib/pkgconfig/sqlite3.pc

%changelog
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1-1
- Initial RPM release.

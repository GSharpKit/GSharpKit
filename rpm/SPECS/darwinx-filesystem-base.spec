%define debug_package %{nil}

Name: 		darwinx-filesystem-base
Version: 	203
Release: 	1%{?dist}
Summary: 	Darwin filesystem and environment
License: 	GPLv2+
Group: 		Development/Libraries
URL: 		http://www.gsharpkit.org
Source0:	macros.darwinx
Source1:	macros.darwinx.x86
Source2:	macros.dist
Source3:	darwinx.sh
Prefix:         /usr

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	darwinx-filesystem = %{version}

Provides:       darwinx-gcc
Provides:       darwinx-odcctools
Provides:       darwinx-sdk
Provides:       autoconf, automake, libtool
Provides:	bison, flex, m4, gperf, ruby, perl
Provides:       pkgconfig
Provides:       python
Provides:	/bin/sh
Provides:	/usr/bin/env
Provides:	/usr/bin/perl
Provides:	perl(Getopt::Long)
Provides:	perl(locale)


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

%ifarch x86_64
cp %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/etc/rpm/macros.darwinx
%else
cp %{SOURCE0} $RPM_BUILD_ROOT%{_prefix}/etc/rpm/macros.darwinx
%endif
cp %{SOURCE2} $RPM_BUILD_ROOT%{_prefix}/etc/rpm/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/etc/profile.d/

mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_prefix}/etc/profile.d/darwinx.sh
%{_prefix}/etc/rpm/macros.darwinx
%{_prefix}/etc/rpm/macros.dist

%changelog
* Fri Jan 24 2014 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1-1
- Initial RPM release.

Name:		ige-mac-bundler	
Version:	0.5
Release:	4%{?dist}
Summary:	Application bundles form GTK+ executables for Mac OS X

Group:		Development/Libraries	
License:	GPLv2
URL:		http://ftp.imendio.com/pub/imendio/ige-mac-bundler/
Source0:	http://ftp.imendio.com/pub/imendio/ige-mac-bundler/ige-mac-bundler-0.5.tar.gz
Source1:	mkdmg
Patch0:		ige-mac-bundler-0.5-no-gtk2.patch
Patch1:		darwinx+ige-mac-bundler-0.5-simple.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch

Requires:	python
Requires:	hfsplus-tools

%description
The script ige-mac-bundler is a helper script that creates application
bundles form GTK+ executables for Mac OS X. The resulting bundle will
contain a complete self-hosting GTK+ installation, ready to run on any
computer with Mac OS X 10.4 or later installed.


%prep
%setup -q
%patch 0 -p1
%patch 1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

sed -i -e 's!@PATH@!%{_datadir}/ige-mac-bundler!' ige-mac-bundler.in

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -m 755 ige-mac-bundler.in $RPM_BUILD_ROOT%{_bindir}/ige-mac-bundler

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/ige-mac-bundler/bundler
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/ige-mac-bundler/ui

install -m 644 bundler/* $RPM_BUILD_ROOT%{_datadir}/ige-mac-bundler/bundler/
install -m 644 ui/* $RPM_BUILD_ROOT%{_datadir}/ige-mac-bundler/ui/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/mkdmg
%{_bindir}/ige-mac-bundler
%{_datadir}/ige-mac-bundler


%changelog


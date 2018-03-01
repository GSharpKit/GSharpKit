Name:           xmedicus-release-rhel
License:        GPL
Group:          System Environment/Base 
Version:        2.4
Release:        1%{?dist}
Url:		https://www.xmedicus.com
Summary:        XMedicus release file and package configuration
Source0:        xmedicus-rhel.repo
Source1:	RPM-GPG-KEY-xmedicus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Obsoletes:	linet-release-rhel

%description
XMedicus release file. This package also contains yum configuration to
use the linet provided rpm packages, as well as the public gpg key
used to sign them.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg/
cp %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/yum.repos.d/xmedicus-rhel.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-xmedicus

%changelog

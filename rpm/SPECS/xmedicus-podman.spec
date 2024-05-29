%define _source_payload w2.xzdio
%define _binary_payload w2.xzdio

%define debug_package %{nil}
%define _build_id_links none

Summary: 	For reloading network in pods.
Name: 		xmedicus-podman
Version:	3.2
Release:	1%{?dist}
BuildArch:	x86_64
License:	XMedicus Systems ApS (See LICENSE file)
Group: 		Applications/Medical
Source0: 	xmedicus-cron-podman-network-reload.service
Source1:	xmedicus-cron-podman-network-restart.service
URL:		https://www.xmedicus.com
Vendor:		XMedicus Systems ApS
Packager:	Mikkel Kruse Johnsen <mikkel@xmedicus.com>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	podman

%description
For reloading network in pods.

%prep
%setup -c %{name}-%{version} -T

%build

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

install -d -m 755 $RPM_BUILD_ROOT/etc/systemd/system
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/systemd/system/podman-network-reload.service
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/systemd/system/podman-network-restart.service

%post
/usr/bin/systemctl daemon-reload >/dev/null 2>&1
test -f /usr/bin/podman && systemctl enable podman-network-reload.service && systemctl enable podman-network-restart.service && systemctl start podman-network-reload.service && systemctl start podman-network-restart.service
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%attr(0644,root,root) /etc/systemd/system/podman-network-reload.service
%attr(0644,root,root) /etc/systemd/system/podman-network-restart.service

###########################################################################
%changelog
* Wed May 29 2022 Mikkel Kruse Johnsen, XMedicus Systems ApS <mikkel@xmedicus.com>
- First rpm build.

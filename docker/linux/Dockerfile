FROM fedora:28
MAINTAINER Mikkel Kruse Johnsen <mikkel@xmedicus.com>

RUN rpm -Uvh http://yum.gsharpkit.org/gsharpkit/fedora-28-x86_64/RPMS/GSharpKit-release-28.5-1.fc28.noarch.rpm

RUN dnf -y --exclude darwinx* install sudo rpm-build NHapi nuget netstandard mono-nunit GSharpKit-sdk && dnf clean all && rm -rf /var/cache/dnf

RUN mkdir -p /root/rpm/SPECS ; mkdir -p /root/rpm/SOURCES ; mkdir -p /root/rpm/BUILD ; mkdir -p /root/rpm/RPMS ; mkdir -p /root/rpm/SRPMS ; mkdir -p /root/rpm/BUILDROOT ; echo "%_topdir /root/rpm" > /root/.rpmmacros 

RUN nuget sources Add -Name "XMedicus" -Source http://nuget.xmedicus.com -username build -password o9hn8n%MJ

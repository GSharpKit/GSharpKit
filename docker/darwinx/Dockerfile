FROM fedora:27
MAINTAINER Mikkel Kruse Johnsen <mikkel@xmedicus.com>

RUN rpm -Uvh http://yum.gsharpkit.org/gsharpkit/fedora-27-x86_64/RPMS/GSharpKit-release-27.18-1.fc27.noarch.rpm

ADD packages/darwinx-*.noarch.rpm /tmp/
RUN rpm -Uvh --nodeps --ignoreos /tmp/darwinx-*.noarch.rpm && rm -f /tmp/darwinx-*.noarch.rpm

RUN dnf -y install sudo GSharpKit-sdk GSharpKit-sdk-darwinx && dnf clean all && rm -rf /var/cache/dnf

RUN mkdir /usr/darwinx/usr/share/myspell ; cp /usr/share/myspell/da_DK.aff /usr/share/myspell/da_DK.dic /usr/share/myspell/en_GB.aff /usr/share/myspell/en_GB.dic /usr/share/myspell/en_US.aff /usr/share/myspell/en_US.dic /usr/darwinx/usr/share/myspell/


FROM fedora:27
MAINTAINER Mikkel Kruse Johnsen <mikkel@xmedicus.com>

RUN rpm -Uvh http://yum.gsharpkit.org/gsharpkit/fedora-27-x86_64/RPMS/GSharpKit-release-27.18-1.fc27.noarch.rpm

RUN dnf -y --exclude darwinx* install sudo GSharpKit-sdk GSharpKit-sdk-mingw-devel GSharpKit-sdk-mingw && dnf clean all && rm -rf /var/cache/dnf

RUN mkdir /usr/i686-w64-mingw32/sys-root/mingw/share/myspell ; cp /usr/share/myspell/da_DK.aff /usr/share/myspell/da_DK.dic /usr/share/myspell/en_GB.aff /usr/share/myspell/en_GB.dic /usr/share/myspell/en_US.aff /usr/share/myspell/en_US.dic /usr/i686-w64-mingw32/sys-root/mingw/share/myspell/


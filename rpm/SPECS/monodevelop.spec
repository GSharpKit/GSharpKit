#
# spec file for package monodevelop
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# PREPARE RELEASE
# git clone https://github.com/mono/monodevelop.git
# cd monodevelop
# git checkout c92f57f326843c4c6e475a26d627b240ab8580f9
# git submodule update --init --recursive
# ./configure --prefix=/usr --enable-release --profile=stable
# make
# find . -iname ".git" -exec rm -rf {} \;

# cd ..
# cp -r monodevelop monodevelop-version
# tar cfJ monodevelop-version.tar.xz monodevelop-version

Name:           monodevelop
BuildRequires:  mono-devel
BuildRequires:  mono-data
BuildRequires:  mono-mvc
BuildRequires: 	nunit-devel
BuildRequires:	gnome-sharp-devel
BuildRequires:  pkgconfig(glade-sharp-2.0) >= 2.12.20
BuildRequires:  pkgconfig(glib-sharp-2.0) >= 2.12.20
BuildRequires:  pkgconfig(gnome-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0) >= 2.12.20
BuildRequires:  pkgconfig(gconf-sharp-2.0) >= 2.12.20
BuildRequires:  pkgconfig(gnome-vfs-sharp-2.0)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  libssh2-devel
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(wcf)
# Mono.Cecil.dll requires rsync after it's build
BuildRequires:  rsync
Url:            http://www.monodevelop.com/
%define __majorver 6.0.2
%define __minorver 41
Version:	%{__majorver}.%{__minorver}
Release:	1%{?dist}
Summary:        Full-Featured IDE for Mono and Gtk-Sharp
License:        LGPL-2.1 and MIT
Group:          Development/Tools/IDE
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildArch:      noarch
Requires:       mono-basic
Requires:       mono-web
Requires:       pkgconfig
Requires:       xsp
Requires:       mono-devel
Requires:       nunit

%description
MonoDevelop is a full-featured integrated development
environment (IDE) for Mono and Gtk-Sharp primarily designed
for C-Sharp and other .NET languages. It allows to quickly
create desktop and ASP.NET Web applications. Support
for Visual Studio file formats eases porting to Linux.

%package devel
Summary:        Development files for MonoDevelop
Group:          Development/Languages/Mono
Requires:       monodevelop = %{version}

%description devel
MonoDevelop is a full-featured integrated development
environment (IDE) for Mono and Gtk-Sharp. It was originally
a port of SharpDevelop 0.98.

This package contains development files for the IDE and plugins.

%prep
%setup -q -n monodevelop-%{version}

%build
%{?env_options}

./configure --prefix=%{_prefix} --enable-release --profile=stable
#make

%install
%{?env_options}
make install DESTDIR=%{buildroot} GACUTIL_FLAGS="/package monodevelop /root %{buildroot}%{_prefix}/lib"

mkdir -p %{buildroot}%{_prefix}/share/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/* %{buildroot}%{_datadir}/pkgconfig
#cp -a /usr/lib/mono/nuget/NuGet.Core.dll %{buildroot}%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.PackageManagement/
#cp -a /usr/lib/mono/nuget/Microsoft.Web.XmlTransform.dll %{buildroot}%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.PackageManagement/

rm -f %{buildroot}%{_prefix}/share/mime/mime.cache

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%defattr(0644,root,root)
%{_datadir}/applications/monodevelop.desktop
%{_datadir}/icons/hicolor/*/apps/monodevelop.png
%{_datadir}/icons/hicolor/scalable/apps/monodevelop.svg
%{_prefix}/lib/monodevelop
%{_mandir}/man1/mdtool.1.gz
%{_mandir}/man1/monodevelop.1.gz
%{_datadir}/mime

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/*.pc

%changelog


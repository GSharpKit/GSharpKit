#
# spec file for package monodevelop-beta
#

%define srcsubdir main
%define vsuffix 2017.08.01.git.23dbfec46c
%define version_suffix .git.23dbfec46c

Name:           monodevelop-beta
BuildRequires:  mono-data
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
BuildRequires:  msbuild
BuildRequires:  fsharp
BuildRequires:  pkgconfig(mono-2)
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gnome-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(gconf-sharp-2.0)
BuildRequires:  pkgconfig(gnome-vfs-sharp-2.0)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  shared-mime-info
BuildRequires:  rsync
Url:            http://www.monodevelop.com/
Version:        7.2.0.487%{version_suffix}
Release:        1.4
Summary:        Full-Featured IDE for Mono and Gtk-Sharp
License:        LGPL-2.1 and MIT
Group:          Development/Tools/IDE
Source:         monodevelop-%{vsuffix}.tar.xz
Source2:        monodevelop-beta-rpmlintrc
Source3:        FakeNuget.cs
Source4:        buildinfo
Source5:        fsharp-packages.config
Source7:        NuGet.Config.template
Source8:        md_packages.tar.xz
Source9:        MDBuild.tar.xz
Source10:       core-gen-buildinfo.patch.template
Source96:       find-embedded-packages.sh
Source97:       deploy-nuget-packages.sh
Source98:       create-md-packages-archive.sh
Source99:       create-monodevelop-source-archive.sh
Patch2:         fsharp-bindings-project-fix.patch
Patch6:         disable-package-mgr-tests.patch
Patch7:         nuget-disable.patch
Patch10:        core-gen-buildinfo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mono-basic
Requires:       mono-web
Requires:       monodoc-core
Requires:       msbuild
Requires:       pkgconfig
Requires:       xsp
Requires:       fsharp
Requires:       distribution-release
Requires:       libgnomeui
Requires:       mono(gnome-sharp)
Requires:       mono(gconf-sharp)
Recommends:     mono-devel
Recommends:     mono-tools
Recommends:     git
# Conflicts with older monodevelop package. Remove following lines if merging this specfile with original monodevelop.spec
Conflicts:      monodevelop
Conflicts:      monodevelop-debugger-gdb
Conflicts:      monodevelop-database
AutoReqProv:    no

%description
This is a custom monodevelop package.
It is really hard to maintain ever-changing and complicating build process, so this package can be removed any time.
I cannot guarantee that all MD features is working as intended.
If you want a stable monodevelop, you should use official flatpak package (https://download.mono-project.com/repo/monodevelop.flatpakref).
Also, this package cannot be merged to official Mono:Factory because of binary nuget dependencies, some of them cannot be build at all with OBS.

%package devel
Summary:        Development files for monodevelop-beta
Group:          Development/Languages/Mono
Requires:       monodevelop-beta = %{version}

%description devel
This package contains development files for the IDE and plugins.

%package lang
Summary:        Localizations for monodevelop-beta
Group:          Development/Languages/Mono
Requires:       monodevelop-beta = %{version}

%description lang
This package contains translations for the IDE and plugins.

%prep
%setup -q -n monodevelop-%{vsuffix} -a 8
%patch2 -p 1
%patch6 -p 1
%patch7 -p 1
%patch10 -p 1
rm -rf "$HOME/.cache/MDBuild" && mkdir -p "$HOME/.cache/MDBuild"
xz -c -d %{S:9} | tar -C "$HOME/.cache" -xvf -

%build
%{?env_options}

# prepare NuGet.Config for use our sourcedir as nuget repo
# prepare NuGet.Config for use packages from our nuget_packages.tar.xz as nuget repo

#remove current nuget configudarion
rm -rf "$HOME/.nuget"
rm -rf "$HOME/.dotnet"
rm -rf "$HOME/.config/NuGet"
rm -rf "$HOME/.local/share/NuGet"

#prepare out nuget config for local deploy
mkdir -p "$HOME/.nuget/NuGet"
cp %{S:7} "$HOME/.nuget/NuGet/NuGet.Config"
sed -i -e "s|__feed_dir__|$PWD/md_packages|g" "$HOME/.nuget/NuGet/NuGet.Config"

# enter subdir where MD sources is, needed for git builds.
pushd %{srcsubdir}

#copy our nuget config to other locations
cp "$HOME/.nuget/NuGet/NuGet.Config" "NuGet.Config"
mkdir -p "$HOME/.config/NuGet"
cp "$HOME/.nuget/NuGet/NuGet.Config" "$HOME/.config/NuGet"

# deploy our manually crafted nuget's packages.config for fsharpbinding
cp %{S:5} external/fsharpbinding/packages.config

# deploy local nuget packages for MD components that require this to work and cannot be disabled from build
chmod 755 %{S:97}
%{S:97} "$PWD"

# we done now with deploying all necessary packages, other deps will be picked from installed system versions
# because package download with nuget will not work in OBS, compile fake NuGet.exe mono executable that only logs command line options
mcs %{S:3} -out:NuGet.exe

# and install it over nuget binary that is used during build, so no more packages will be deployed during build
mkdir .nuget
cp NuGet.exe .nuget
cp NuGet.exe external/RefactoringEssentials/.nuget
cp NuGet.exe external/fsharpbinding/.nuget

# create fake nuget binary used by some shell scripts
nuget_dir=`mktemp -d`
echo "#!/bin/sh" > $nuget_dir/nuget
echo "mono \"$PWD/.nuget/NuGet.exe\" \"\$@\"" >> $nuget_dir/nuget
chmod 755 $nuget_dir/nuget
export PATH="$nuget_dir:$PATH"

# also, install it as fake paket executables needed for fsharp bindings build inside OBS
cp NuGet.exe external/fsharpbinding/.paket/paket.exe
cp NuGet.exe external/fsharpbinding/.paket/paket.bootstrapper.exe

rm NuGet.exe

# exit srcsubdir
popd

# perform configuration and build
pushd %{srcsubdir}
NOCONFIGURE=YES ./autogen.sh
%configure --enable-tests=no --enable-gnomeplatform=yes --enable-subversion=yes --enable-git=yes --enable-release --libdir=%{_prefix}/lib --disable-update-mimedb
cp %{S:4} .
popd

%install
%{?env_options}

pushd %{srcsubdir}
make install DESTDIR=%{buildroot} GACUTIL_FLAGS="/package monodevelop /root %{buildroot}%{_prefix}/lib"
popd

mkdir -p %{buildroot}%{_prefix}/share/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/* %{buildroot}%{_datadir}/pkgconfig

#copy buildinfo
cp %{S:4} %{buildroot}%{_prefix}/lib/monodevelop/bin

#fix fsharp packages
pkg_tdir="%{buildroot}%{_prefix}/lib/monodevelop/AddIns/FSharpBinding/Packages"
for pkg_dir in "$pkg_tdir"/*
do
  [[ ! -d $pkg_dir ]] && continue
  pkg_name=`basename "$pkg_dir"`
  mv "$pkg_dir"/*.nupkg "/tmp/$pkg_name"
  rm -rf "$pkg_dir"
  mv "/tmp/$pkg_name" "$pkg_tdir"
done

# show fake nuget logfile
cat /tmp/fake-nuget.log

%fdupes %{buildroot}%{_prefix}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%{_bindir}/*
%defattr(0644,root,root)
%{_datadir}/applications/monodevelop.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/monodevelop.appdata.xml
%{_datadir}/icons/hicolor/*/apps/monodevelop.png
%{_datadir}/icons/hicolor/scalable/apps/monodevelop.svg
%dir %{_prefix}/lib/monodevelop
%{_prefix}/lib/monodevelop/AddIns
%{_prefix}/lib/monodevelop/bin
%{_prefix}/lib/monodevelop/data
%{_mandir}/man1/mdtool.1%ext_man
%{_mandir}/man1/monodevelop.1%ext_man
%{_datadir}/mime/packages/monodevelop.xml

%files devel
%defattr(0644,root,root)
%{_datadir}/pkgconfig/*.pc

%files lang
%defattr(0644,root,root)
%dir %{_prefix}/lib/monodevelop
%{_prefix}/lib/monodevelop/locale
%{_datadir}/locale/*/*/*.mo

%changelog
* Tue Aug  8 2017 fwdsbs.to.11df@xoxy.net
- Package updated to version 7.2 (preview):
  * Using commit 23dbfec46cc34a04c0b4d31238f0a545418724c3, tag monodevelop-7.2.0.487
- Drop mono-addins-pkg-path-fix.patch
- Update helper scripts for nuget packaging in offline mode (OBS)
* Tue May  9 2017 fwdsbs.to.11df@xoxy.net
- Package updated to version 7.1 (beta)
- Major packaging changes
- Build process now require msbuild utility
- Drop most of the external dependencies: MD now comes with its own copies of most of the required packages
* Sun Oct  2 2016 fwdsbs.to.11df@xoxy.net
- Changes in build process:
  * enabled build of FSharp addons, all binary nuget requirements deployed locally during build.
  maybe it is a good idea to split FSharp addons to the separate rpm,
  (or even to a separate package, but now it is a part of MD's source tree)
* Sat Oct  1 2016 fwdsbs.to.11df@xoxy.net
- Changes in build process:
  * get rid of nunit3 stub, always enable nunit3 support in build
  * disable mono-nuget requires, because MD now shipped with it's own nuget binaries
  * use Newtonsoft.Json.6.0.8 from official nupkg, it is required for nuget support and MD build
* Thu Sep 29 2016 fwdsbs.to.11df@xoxy.net
- Package updated to version 6.1.1, using cycle8-sr0 git branch
  * disabled FSharp support: fsharp addins need more work to be build and properly packaged using OBS
  * disabled MonoDevelop.PackageManagement.Tests project build: it also require some work to be build with OBS
* Mon May 30 2016 fwdsbs.to.11df@xoxy.net
- Package created. This package created for testing purposes only. May be removed in future.
  * It may be built in unusable state.
  * It may ruin your project, YOU HAVE BEEN WARNED, use at your own risk!

#
# spec file for package msbuild
#

#for use with script that create nuget_packages.tar.xz (TODO)
#define online_build 1

%define vsuffix 2017.08.03.git.431c7ec

Name:           msbuild
Version:        15.3+xamarinxplat.2017.07.20
Release:        1.13
License:        MIT
Summary:        Microsoft Build Engine (MSbuild) for Mono
Url:            https://github.com/Microsoft/msbuild
Group:          Development/Languages/Mono
Source0:        msbuild-%{vsuffix}.tar.xz
Source90:       create-msbuild-source-archive.sh
Source93:       NuGet.Config.template
#libraries from ubuntu 16.10, needed for binary M$ dotnet sdk, precompiled for ubuntu
Source96:       ubuntu_libs.tar.xz
#precompiled .net binaries and nuget packages needed for offline build
Source97:       nuget_packages.tar.xz
Source98:       https://github.com/Microsoft/msbuild/releases/download/mono-hosted-msbuild-v0.03/mono_msbuild_d25dd923839404bd64cc63f420e75acf96fc75c4.zip
Source99:       Tools.tar.xz
Patch0:         use-local-sources.patch
Patch1:         install-fix.patch
BuildRequires:  mono-devel
BuildRequires:  unzip
BuildRequires:  libunwind
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mono-devel
AutoReqProv:    no
ExclusiveArch:  x86_64 noarch
BuildArch:      noarch

%description
The Microsoft Build Engine is a platform for building applications.
This engine, which is also known as MSBuild, provides an XML schema
for a project file that controls how the build platform processes
and builds software. Visual Studio uses MSBuild, but MSBuild does
not depend on Visual Studio. By invoking msbuild.exe on your
project or solution file, you can orchestrate and build products
in environments where Visual Studio isn't installed.

This package contains the main msbuild build system

%package sdkresolver
Group:          Development/Languages/Mono
Summary:        Managed portion of helper library for msbuild for .NET Core SDK discovery
Requires:       %{name} = %{version}
AutoReqProv:    no

%description sdkresolver
The Microsoft Build Engine is a platform for building applications.

This package contains the managed portion of the helper library
which will auto-discover the .NET Core SDK on your system

%prep
%if 0%{?online_build} == 1
%setup -q -n msbuild-%{vsuffix} -a 99 -a 96
%else
%setup -q -n msbuild-%{vsuffix} -a 99 -a 97 -a 96
%endif

%patch0 -p1
%patch1 -p1

%build
# prepare NuGet.Config for use packages from our nuget_packages.tar.xz as nuget repo
rm -rf "$HOME/.nuget"
rm -rf "$HOME/.dotnet"
rm -rf "$HOME/.config/NuGet"
%if 0%{?online_build} == 1
# needed only for clean Tools dir deploy from internet (TODO)
export __PUBLISH_RID="ubuntu.14.04-x64"
%else
mkdir -p "$HOME/.nuget/NuGet"
cp %{S:93} "$HOME/.nuget/NuGet/NuGet.Config"
sed -i -e "s|__feed_dir__|$PWD/nuget_packages|g" "$HOME/.nuget/NuGet/NuGet.Config"
cp "$HOME/.nuget/NuGet/NuGet.Config" "NuGet.Config"
%endif
# set local msbuild archive path
sed -i "s|_LOCAL_MSBUILD_ZIP|%{S:98}|g" cibuild.sh
# setup libraries from ubuntu 16.04, used by dotnet from Tools.tar.xz
# there is no other option right now, because bootstrap process depends on particular prebuild dotnet binaries
# that only exist for ubuntu 16.04
export LD_LIBRARY_PATH="$PWD/ubuntu_libs:$LD_LIBRARY_PATH"
./cibuild.sh --scope Compile --host Mono --target Mono --config Release

%if 0%{?online_build} == 1
#populate packages list for reuse in offline build
rm -rf nuget_packages
mkdir -p nuget_packages
pushd nuget_packages
find "$HOME/.nuget" -name "*.nupkg" -exec cp {} . \;
find "../packages" -name "*.nupkg" -exec cp {} . \;
popd
tar cf nuget_packages.tar nuget_packages --owner=0 --group=0
xz -9e nuget_packages.tar
mv nuget_packages.tar.xz "%{_sourcedir}"
%endif

%install
DESTDIR="%{buildroot}" ./install-mono-prefix.sh "%{_prefix}"
find "%{buildroot}%{_prefix}" -name "Microsoft.DiaSymReader.Native.*dll" -exec rm -v {} \;
find "%{buildroot}%{_prefix}" -name "*.dylib" -exec rm -v {} \;
%fdupes "%{buildroot}%{_prefix}"

%files sdkresolver
%defattr(-,root,root)
%{_prefix}/lib/mono/msbuild/15.0/bin/SdkResolvers

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/msbuild
%{_prefix}/lib/mono/msbuild
%exclude %{_prefix}/lib/mono/msbuild/15.0/bin/SdkResolvers
%{_prefix}/lib/mono/xbuild
%{_mandir}/man1/msbuild.1.*

%changelog
* Wed Aug  9 2017 fwdsbs.to.11df@xoxy.net
- Package updated, switch to new repository https://github.com/mono/linux-packaging-msbuild.git:
  * Looks like it is the same sources that used in debian bulds from official mono downloads
  * Using commit 431c7ec5857a3ee5df758c09948719490025ef94, tag debian/15.3+xamarinxplat.2017.07.20.13.52-0xamarin1
  * Version updated to 15.3+xamarinxplat.2017.07.20
- Split .NET Core SDK resolver to separate package
* Tue Aug  8 2017 fwdsbs.to.11df@xoxy.net
- Add create-packages-archive.sh script:
  * Perform online build in order to create nuget_packages.tar.xz source file
- Package updated:
  * Using commit 0f250921e0b91ca1bda6494df49ae8ad703aeb5c from xplat-master branch
  * Version updated to d15.5.2017.07.22.git.0f250921
* Wed May 31 2017 fwdsbs.to.11df@xoxy.net
- Use git sources from https://github.com/mono/msbuild:
  * Using commit 714a4c08cfd2e0e66f18c73548e905163ea008c6 from xplat-master branch
  * Version updated to d15.3.2017.05.31.git.714a4c08
* Mon May  8 2017 fwdsbs.to.11df@xoxy.net
- Package created
- Using a lot of precompiled binary components for build:
  * There is no other option right now to build msbuild in offline and automated manner
  * TODO: get rid of binary build dependencies

%global debug_package %{nil}

%define pkg_name standard
%define libdir /usr/lib

Name:           netstandard
Version:        2.0.3
Release:        2%{?dist}
Summary:        .NET Standard solves the code sharing problem for .NET developers across all platforms.

License:        MIT
URL:            https://github.com/dotnet/standard
Source0:        %{pkg_name}-%{version}.tar.gz


# dnf copr enable @dotnet-sig/dotnet
# dnf install dotnet-sdk-2.0
BuildRequires:  dotnet-sdk-2.0

#Provides:	mono(System.Collections.NonGeneric) = 4.0.0.0
#Provides:	mono(System.IO.FileSystem) = 4.0.0.0
#Provides:	mono(System.IO.FileSystem.Primitives) = 4.0.0.0
#Provides:	mono(System.IO.UnmanagedMemoryStream) = 4.0.0.0
#Provides:	mono(System.Xml.XPath) = 4.0.0.0

%description
NET Standard solves the code sharing problem for .NET developers across all platforms by bringing all the APIs that you expect and love across the environments that you need: desktop applications, mobile apps & games, and cloud services:
    .NET Standard is a set of APIs that all .NET platforms have to implement. This unifies the .NET platforms and prevents future fragmentation.
    .NET Standard 2.0 will be implemented by .NET Framework, .NET Core, and Xamarin. For .NET Core, this will add many of the existing APIs that have been requested.
    .NET Standard 2.0 includes a compatibility shim for .NET Framework binaries, significantly increasing the set of libraries that you can reference from your .NET Standard libraries.
    .NET Standard will replace Portable Class Libraries (PCLs) as the tooling story for building multi-platform .NET libraries.


%prep
%setup -q -n %{pkg_name}-%{version}
#sed -i "s!ubuntu!rhel.7!g" init-tools.sh
#sed -i "s!rm -rf -- \$__TOOLRUNTIME_DIR;!mkdir -p Tools;!g" init-tools.sh
#sed -i "s!cp -r \$DOTNET_TOOL_DIR\/\* \$__DOTNET_PATH!cp -r \$DOTNET_TOOL_DIR\/\* \$__DOTNET_PATH\n\telif [ -f \"\$DOTNET_CMD\" ]; then\n\t\tmkdir -p \$__TOOLRUNTIME_DIR/dotnetcli; ln -s \$DOTNET_CMD \$__TOOLRUNTIME_DIR/dotnetcli/dotnet;!g" init-tools.sh

%build
#export __PUBLISH_RID="rhel.7-x64"
export DOTNET_CMD=/usr/bin/dotnet
./build.sh || exit -1

%install

mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/net461
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.0
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.1
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.2
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.3
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.4
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.5
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.6
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0

cp -rf bin/ref/net461/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/net461/
cp -rf bin/obj/CompatShims/ref/netstandard1.0/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.0/
cp -rf bin/obj/CompatShims/ref/netstandard1.1/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.1/
cp -rf bin/obj/CompatShims/ref/netstandard1.2/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.2/
cp -rf bin/obj/CompatShims/ref/netstandard1.3/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.3/
cp -rf bin/obj/CompatShims/ref/netstandard1.4/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.4/
cp -rf bin/obj/CompatShims/ref/netstandard1.5/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.5/
cp -rf bin/obj/CompatShims/ref/netstandard1.6/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.6/
cp -rf bin/shims/netstandard/* %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/
cp -rf bin/ref/netstandard/2.0.0.0/netstandard.dll %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/

%files
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/net461
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.0
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.1
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.2
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.3
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.4
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.5
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.6
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0

%{libdir}/mono/xbuild-frameworks/.NETStandard/net461/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.0/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.1/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.2/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.3/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.4/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.5/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard1.6/*
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/*

%changelog
* Wed Apr 05 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.0-2
- Include netstandard.dll

* Wed Apr 05 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.0-1
- initial package for netstandard


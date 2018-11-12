%global debug_package %{nil}

%define pkg_name NETStandard.Library
%define libdir /usr/lib

Name:           netstandard
Version:        2.0.3
Release:        1%{?dist}
Summary:        .NET Standard solves the code sharing problem for .NET developers across all platforms.

License:        MIT
URL:            https://github.com/dotnet/standard


%description
NET Standard solves the code sharing problem for .NET developers across all platforms by bringing all the APIs that you expect and love across the environments that you need: desktop applications, mobile apps & games, and cloud services:
    .NET Standard is a set of APIs that all .NET platforms have to implement. This unifies the .NET platforms and prevents future fragmentation.
    .NET Standard 2.0 will be implemented by .NET Framework, .NET Core, and Xamarin. For .NET Core, this will add many of the existing APIs that have been requested.
    .NET Standard 2.0 includes a compatibility shim for .NET Framework binaries, significantly increasing the set of libraries that you can reference from your .NET Standard libraries.
    .NET Standard will replace Portable Class Libraries (PCLs) as the tooling story for building multi-platform .NET libraries.


%prep
%setup -c %{name}-%{version} -T
nuget install %{pkg_name} -Version %{version}

%build

%install
mkdir -p %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0
install %{pkg_name}.%{version}/build/netstandard2.0/ref/*.dll %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/

rm %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/mscorlib.dll
rm %{buildroot}%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/System.dll

%files
%dir %{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0
%{libdir}/mono/xbuild-frameworks/.NETStandard/netstandard2.0/*.dll

%changelog
* Fri Nov 09 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.3-1
- Create from NuGet package instead. Only netstandard2.0.

* Wed Apr 05 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.0-2
- Include netstandard.dll

* Wed Apr 05 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.0.0-1
- initial package for netstandard


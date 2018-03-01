%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name mono-core
%global mingw_build_win32 1
%global mingw_build_win64 1

%define _binaries_in_noarch_packages_terminate_build 0

%define ver 5.10.0.95

Name:		mingw-mono-core
Version:	%{ver}
Release:	1%{?dist}
Summary:	The Mono CIL runtime, suitable for running .NET code
License:	LGPLv2
Group:		Development/Languages
URL:		http://www.mono-project.com/Main_Page
Source0:	mono-%{ver}-x86.zip
Source1:	mono-%{ver}-x64.zip
Source2:	VC_redist.x86.exe
Source3:	VC_redist.x64.exe
Source4:       	mingw-mono-5.10-config.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	redhat-rpm-config

BuildRequires:	mingw32-filesystem
BuildRequires:	mingw64-filesystem
BuildRequires:	mingw32-gcc
BuildRequires:	mingw64-gcc
BuildRequires:	mingw32-binutils
BuildRequires:	mingw64-binutils
BuildRequires:	mingw32-glib2
BuildRequires:	mingw64-glib2
BuildRequires:  mingw32-gettext >= 0.17
BuildRequires:  mingw64-gettext >= 0.17

%description
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,
I18N, Cairo and Mono.*).

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
# Requires: Must use "libintl-8.dll" inforce gettext-0.17
Requires:       mingw32-glib2
Requires:       mingw32-gettext >= 0.17
Obsoletes:      mingw32-mono
Provides:	mingw32-mono
Provides:	mingw32(vcruntime140.dll)
Provides:	mingw32(msvcr120.dll)
Provides:	mingw32(api-ms-win-core-winrt-error-l1-1-0.dll)
Provides:	mingw32(api-ms-win-core-winrt-l1-1-0.dll)
Provides:	mingw32(api-ms-win-core-winrt-string-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-conio-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-convert-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-environment-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-filesystem-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-heap-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-locale-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-math-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-multibyte-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-runtime-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-stdio-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-string-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-time-l1-1-0.dll)
Provides:	mingw32(api-ms-win-crt-utility-l1-1-0.dll)

%description -n mingw32-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
# Requires: Must use "libintl-8.dll" inforce gettext-0.17
Requires:       mingw64-glib2
Requires:       mingw64-gettext >= 0.17
Obsoletes:	mingw64-mono
Provides:       mingw64-mono
Provides:	mingw64(vcruntime140.dll)
Provides:	mingw64(msvcr120.dll)
Provides:	mingw64(api-ms-win-core-winrt-error-l1-1-0.dll)
Provides:	mingw64(api-ms-win-core-winrt-l1-1-0.dll)
Provides:	mingw64(api-ms-win-core-winrt-string-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-conio-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-convert-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-environment-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-filesystem-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-heap-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-locale-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-math-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-multibyte-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-runtime-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-stdio-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-string-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-time-l1-1-0.dll)
Provides:	mingw64(api-ms-win-crt-utility-l1-1-0.dll)

%description -n mingw64-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,

#?mingw_debug_package

%define gac_dll(dll) \
  cp -rf ../mono-%{ver}-x86/lib/mono/gac/%{1} %{buildroot}%{mingw32_libdir}/mono/gac/ \
  cp -rf ../mono-%{ver}-x64/lib/mono/gac/%{1} %{buildroot}%{mingw64_libdir}/mono/gac/ \
  %{nil}
%define bin_bat(bin) \
  cp ../mono-%{ver}-x86/bin/%{1} %{buildroot}%{mingw32_bindir} \
  cp ../mono-%{ver}-x86/bin/%{1}.bat %{buildroot}%{mingw32_bindir} \
  cp ../mono-%{ver}-x64/bin/%{1} %{buildroot}%{mingw64_bindir} \
  cp ../mono-%{ver}-x64/bin/%{1}.bat %{buildroot}%{mingw64_bindir} \
  %{nil}

%define bin_exe(bin) \
  cp ../mono-%{ver}-x86/bin/%{1}.exe %{buildroot}%{mingw32_bindir} \
  cp ../mono-%{ver}-x86/bin/%{1}.pdb %{buildroot}%{mingw32_bindir} \
  cp ../mono-%{ver}-x64/bin/%{1}.exe %{buildroot}%{mingw64_bindir} \
  cp ../mono-%{ver}-x64/bin/%{1}.pdb %{buildroot}%{mingw64_bindir} \
  %{nil}


%prep
%setup -q -c mono-%{ver} -T -b 0 -b 1

%build

%install
rm -rf $RPM_BUILD_ROOT

pushd ../mono-%{ver}-x86/etc/mono/
patch -p0 < %{_sourcedir}/mingw-mono-5.10-config.patch
popd

pushd ../mono-%{ver}-x64/etc/mono/
patch -p0 < %{_sourcedir}/mingw-mono-5.10-config.patch
popd

# Mingw32
install -d -m 755 %{buildroot}%{mingw32_sysconfdir}/mono
install -d -m 755 %{buildroot}%{mingw32_bindir}
install -d -m 755 %{buildroot}%{mingw32_libdir}/mono/gac
install -d -m 755 %{buildroot}%{mingw32_libdir}/pkgconfig
install -d -m 755 %{buildroot}%{mingw32_includedir}

cp -rf -L ../mono-%{ver}-x86/etc/mono/* %{buildroot}%{mingw32_sysconfdir}/mono/

cp -rf -L ../mono-%{ver}-x86/lib/mono/4.0 %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.0-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.5 %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.5-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.5.1-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.5.2-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.6-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.6.1-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.6.2-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.7-api %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L ../mono-%{ver}-x86/lib/mono/4.7.1-api %{buildroot}%{mingw32_libdir}/mono/

cp -f ../mono-%{ver}-x86/bin/mono-sgen.exe %{buildroot}%{mingw32_bindir}/mono-sgen.exe
cp -f ../mono-%{ver}-x86/bin/mono-sgen.pdb %{buildroot}%{mingw32_bindir}/mono-sgen.pdb
cp -f ../mono-%{ver}-x86/bin/mono-sgen.exe %{buildroot}%{mingw32_bindir}/mono.exe
cp -f ../mono-%{ver}-x86/bin/mono-sgen.pdb %{buildroot}%{mingw32_bindir}/mono.pdb
cp -f ../mono-%{ver}-x86/bin/mono-2.0-sgen.dll %{buildroot}%{mingw32_bindir}/
cp -f ../mono-%{ver}-x86/bin/MonoPosixHelper.dll %{buildroot}%{mingw32_bindir}/
cp -f ../mono-%{ver}-x86/libmono-static-sgen.lib %{buildroot}%{mingw32_libdir}/
cp -f ../mono-%{ver}-x86/mono-2.0-sgen.lib %{buildroot}%{mingw32_libdir}/
cp -f ../mono-%{ver}-x86/mono-2.0-sgen.pdb %{buildroot}%{mingw32_libdir}/
cp -f ../mono-%{ver}-x86/MonoPosixHelper.lib %{buildroot}%{mingw32_libdir}/
cp -f ../mono-%{ver}-x86/MonoPosixHelper.pdb %{buildroot}%{mingw32_libdir}/

cp -rf -L ../mono-%{ver}-x86/include/* %{buildroot}%{mingw32_includedir}/

cp -f ../mono-%{ver}-x86/lib/pkgconfig/* %{buildroot}%{mingw32_libdir}/pkgconfig/
sed -s -i 's!monosgen-2\.0!mono-2\.0-sgen!g' %{buildroot}%{mingw32_libdir}/pkgconfig/monosgen-2.pc

# Visual Studio Redistributable
install -m 755 %{SOURCE2} %{buildroot}%{mingw32_bindir}/



# Mingw64
install -d -m 755 %{buildroot}%{mingw64_sysconfdir}/mono
install -d -m 755 %{buildroot}%{mingw64_bindir}
install -d -m 755 %{buildroot}%{mingw64_libdir}/mono/gac
install -d -m 755 %{buildroot}%{mingw64_libdir}/pkgconfig
install -d -m 755 %{buildroot}%{mingw64_includedir}

cp -rf -L ../mono-%{ver}-x64/etc/mono/* %{buildroot}%{mingw64_sysconfdir}/mono/

cp -rf -L ../mono-%{ver}-x64/lib/mono/4.0 %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.0-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.5 %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.5-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.5.1-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.5.2-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.6-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.6.1-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.6.2-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.7-api %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L ../mono-%{ver}-x64/lib/mono/4.7.1-api %{buildroot}%{mingw64_libdir}/mono/

cp -f ../mono-%{ver}-x64/bin/mono-sgen.exe %{buildroot}%{mingw64_bindir}/mono-sgen.exe
cp -f ../mono-%{ver}-x64/bin/mono-sgen.pdb %{buildroot}%{mingw64_bindir}/mono-sgen.pdb
cp -f ../mono-%{ver}-x64/bin/mono-sgen.exe %{buildroot}%{mingw64_bindir}/mono.exe
cp -f ../mono-%{ver}-x64/bin/mono-sgen.pdb %{buildroot}%{mingw64_bindir}/mono.pdb
cp -f ../mono-%{ver}-x64/bin/mono-2.0-sgen.dll %{buildroot}%{mingw64_bindir}/
cp -f ../mono-%{ver}-x64/bin/MonoPosixHelper.dll %{buildroot}%{mingw64_bindir}/
cp -f ../mono-%{ver}-x64/libmono-static-sgen.lib %{buildroot}%{mingw64_libdir}/
cp -f ../mono-%{ver}-x64/mono-2.0-sgen.lib %{buildroot}%{mingw64_libdir}/
cp -f ../mono-%{ver}-x64/mono-2.0-sgen.pdb %{buildroot}%{mingw64_libdir}/
cp -f ../mono-%{ver}-x64/MonoPosixHelper.lib %{buildroot}%{mingw64_libdir}/
cp -f ../mono-%{ver}-x64/MonoPosixHelper.pdb %{buildroot}%{mingw64_libdir}/

cp -rf -L ../mono-%{ver}-x64/include/* %{buildroot}%{mingw64_includedir}/

cp -f ../mono-%{ver}-x64/lib/pkgconfig/* %{buildroot}%{mingw64_libdir}/pkgconfig/
sed -s -i 's!monosgen-2\.0!mono-2\.0-sgen!g' %{buildroot}%{mingw64_libdir}/pkgconfig/monosgen-2.pc

# Visual Studio Redistributable
install -m 755 %{SOURCE3} %{buildroot}%{mingw64_bindir}/


# mono-core
%bin_bat cert-sync

%gac_dll Accessibility
%gac_dll Commons.Xml.Relaxng
%gac_dll cscompmgd
%gac_dll CustomMarshalers
%gac_dll I18N
%gac_dll I18N.CJK
%gac_dll I18N.MidEast
%gac_dll I18N.Other
%gac_dll I18N.Rare
%gac_dll I18N.West
%gac_dll IBM.Data.DB2
%gac_dll ICSharpCode.SharpZipLib
%gac_dll Microsoft.Build
%gac_dll Microsoft.Build.Engine
%gac_dll Microsoft.Build.Framework
%gac_dll Microsoft.Build.Tasks.Core
%gac_dll Microsoft.Build.Tasks.v12.0
%gac_dll Microsoft.Build.Tasks.v4.0
%gac_dll Microsoft.Build.Utilities.Core
%gac_dll Microsoft.Build.Utilities.v12.0
%gac_dll Microsoft.Build.Utilities.v4.0
%gac_dll Microsoft.CSharp
%gac_dll Microsoft.VisualBasic
%gac_dll Microsoft.VisualC
%gac_dll Microsoft.Web.Infrastructure
%gac_dll Mono.Cairo
%gac_dll Mono.Cecil
%gac_dll Mono.Cecil.VB
%gac_dll Mono.Cecil.VB.Mdb
%gac_dll Mono.Cecil.VB.Pdb
%gac_dll Mono.CodeContracts
%gac_dll Mono.CompilerServices.SymbolWriter
%gac_dll Mono.CSharp
%gac_dll Mono.Data.Sqlite
%gac_dll Mono.Data.Tds
%gac_dll Mono.Debugger.Soft
%gac_dll Mono.Http
%gac_dll Mono.Management
%gac_dll Mono.Messaging
%gac_dll Mono.Messaging.RabbitMQ
%gac_dll Mono.Parallel
%gac_dll Mono.Posix
%gac_dll Mono.Profiler.Log
%gac_dll Mono.Security
%gac_dll Mono.Security.Win32
%gac_dll Mono.Simd
%gac_dll Mono.Tasklets
%gac_dll Mono.WebBrowser
%gac_dll Mono.WebServer2
%gac_dll Mono.XBuild.Tasks
%gac_dll Novell.Directory.Ldap
%gac_dll PEAPI
%gac_dll RabbitMQ.Client
%gac_dll SMDiagnostics
%gac_dll System
%gac_dll System.ComponentModel.Composition
%gac_dll System.ComponentModel.DataAnnotations
%gac_dll System.Configuration
%gac_dll System.Configuration.Install
%gac_dll System.Core
%gac_dll System.Data
%gac_dll System.Data.DataSetExtensions
%gac_dll System.Data.Entity
%gac_dll System.Data.Linq
%gac_dll System.Data.OracleClient
%gac_dll System.Data.Services
%gac_dll System.Data.Services.Client
%gac_dll System.Deployment
%gac_dll System.Design
%gac_dll System.DirectoryServices
%gac_dll System.DirectoryServices.Protocols
%gac_dll System.Drawing
%gac_dll System.Drawing.Design
%gac_dll System.Dynamic
%gac_dll System.EnterpriseServices
%gac_dll System.IdentityModel
%gac_dll System.IdentityModel.Selectors
%gac_dll System.IO.Compression
%gac_dll System.IO.Compression.FileSystem
%gac_dll System.Json
%gac_dll System.Json.Microsoft
%gac_dll System.Management
%gac_dll System.Messaging
%gac_dll System.Net
%gac_dll System.Net.Http
%gac_dll System.Net.Http.Formatting
%gac_dll System.Net.Http.WebRequest
%gac_dll System.Numerics
%gac_dll System.Numerics.Vectors
%gac_dll System.Reactive.Core
%gac_dll System.Reactive.Debugger
%gac_dll System.Reactive.Experimental
%gac_dll System.Reactive.Interfaces
%gac_dll System.Reactive.Linq
%gac_dll System.Reactive.Observable.Aliases
%gac_dll System.Reactive.PlatformServices
%gac_dll System.Reactive.Providers
%gac_dll System.Reactive.Runtime.Remoting
%gac_dll System.Reactive.Windows.Forms
%gac_dll System.Reactive.Windows.Threading
%gac_dll System.Reflection.Context
%gac_dll System.Runtime.Caching
%gac_dll System.Runtime.DurableInstancing
%gac_dll System.Runtime.Remoting
%gac_dll System.Runtime.Serialization
%gac_dll System.Runtime.Serialization.Formatters.Soap
%gac_dll System.Security
%gac_dll System.ServiceModel
%gac_dll System.ServiceModel.Activation
%gac_dll System.ServiceModel.Discovery
%gac_dll System.ServiceModel.Internals
%gac_dll System.ServiceModel.Routing
%gac_dll System.ServiceModel.Web
%gac_dll System.ServiceProcess
%gac_dll System.Threading.Tasks.Dataflow
%gac_dll System.Transactions
%gac_dll System.Web
%gac_dll System.Web.Abstractions
%gac_dll System.Web.ApplicationServices
%gac_dll System.Web.DynamicData
%gac_dll System.Web.Extensions
%gac_dll System.Web.Extensions.Design
%gac_dll System.Web.Http
%gac_dll System.Web.Http.SelfHost
%gac_dll System.Web.Http.WebHost
%gac_dll System.Web.Mobile
%gac_dll System.Web.Mvc
%gac_dll System.Web.Razor
%gac_dll System.Web.RegularExpressions
%gac_dll System.Web.Routing
%gac_dll System.Web.Services
%gac_dll System.Web.WebPages
%gac_dll System.Web.WebPages.Deployment
%gac_dll System.Web.WebPages.Razor
%gac_dll System.Windows
%gac_dll System.Windows.Forms
%gac_dll System.Windows.Forms.DataVisualization
%gac_dll System.Workflow.Activities
%gac_dll System.Workflow.ComponentModel
%gac_dll System.Workflow.Runtime
%gac_dll System.Xaml
%gac_dll System.Xml
%gac_dll System.Xml.Linq
%gac_dll System.Xml.Serialization
%gac_dll WebMatrix.Data
%gac_dll WindowsBase

%clean
#rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_sysconfdir}
%{mingw32_bindir}
%{mingw32_libdir}
%{mingw32_includedir}


%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_sysconfdir}
%{mingw64_bindir}
%{mingw64_libdir}
%{mingw64_includedir}


%changelog
* Mon Jul 18 2016 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.4.1.0-1
- Updated to 4.4.1.0

* Fri Aug 14 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.3-1
- Use bin and DLL from Windows build

* Mon Apr 27 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.0.1-1
- Update to Mono 4.0

* Sun Mar 29 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.1-3
- Remove Npgsql for seperate package
- Patch for DbCommand Async

* Mon Mar 23 2015 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 3.12.1-2
- Updated Npgsql to 2.2.5

* Mon Mar 24 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.2.8-1
- Move to 3.2.8

* Mon Oct 07 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.2.3-1
- Move to 3.2.3

* Tue Mar 27 2012 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 2.11.1-1
- Move to 2.11.1

* Wed Jun 08 2011 Mikkel Kruse Johnsen <mikkel@linet.dk> - 2.10.2
- Move to 2.10.2

* Mon Apr 04 2011 Mikkel Kruse Johnsen <mikkel@linet.dk> - 2.10.1
- Move to 2.10.1

* Thu Jan 20 2011 Mikkel Kruse Johnsen <mikkel@linet.dk> - 2.8
- Bump to 2.8.2

* Wed Jul 22 2009 Mikkel Kruse Johnsen <mikkel@linet.dk> - 2.4
- Initial release


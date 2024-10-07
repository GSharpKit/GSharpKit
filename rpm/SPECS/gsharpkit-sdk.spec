%define _binary_payload w4.gzdio

#### DEFINE VERSIONS
%define DOTNET_VERSION 8.0

%define major_version 39
%define minor_version 0
%define sdk_version 700

%define linux_prefix /usr/lib/GSharpKit/sdk/%{major_version}
%define mingw64_prefix /usr/x86_64-w64-mingw32/sys-root/mingw/lib/GSharpKit/sdk/%{major_version}
%define darwinx_prefix /Library/Frameworks/GSharpKit/sdk/%{major_version}

Name: 			GSharpKit-sdk-%{major_version}
Summary: 		Easy management of applications
Version:		%{major_version}.%{minor_version}.%{sdk_version}
Release:		1%{?dist}
License:		GPL
Group: 			Applications/Desktop
URL:			http://www.gsharpkit.com
Vendor:			GSharpKit
Source1:		Mono.Addins.dll
Source2:		Mono.Addins.CecilReflector.dll
Packager:		Mikkel Kruse Johnsen <mikkel@gsharpkit.com>
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch
AutoReqProv:    	no

Requires:		dotnet-sdk-%{DOTNET_VERSION}

Requires:               gnome-common intltool glib2-devel redhat-rpm-config rpm-build fedora-packager
Requires:               meson
Requires:               redhat-rpm-config rpm-build
Requires:               msitools
Requires:               osslsigncode openssl openssl-pkcs11 gnutls vim-common
Requires:               hunspell-da hunspell-en-GB hunspell-en-US
Requires:               python
Requires:               sudo

BuildRequires:		dotnet-runtime-%{DOTNET_VERSION}
BuildRequires:		GtkSharp >= 3.24.24.36

%description
Easy management of applications for Linux 64 bit



%package mingw64
Summary:                SDK for GSharpKit Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

Requires:               dotnet-sdk-%{DOTNET_VERSION}

Requires:               gnome-common intltool glib2-devel redhat-rpm-config rpm-build fedora-packager
Requires:               meson
Requires:               redhat-rpm-config rpm-build
Requires:               msitools
Requires:               osslsigncode openssl openssl-pkcs11 gnutls vim-common
Requires:               hunspell-da hunspell-en-GB hunspell-en-US
Requires:               python
Requires:               sudo

%description mingw64
Easy management of applications for Windows 64 bit



%package darwinx
Summary:                SDK for GSharpKit macOS 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

Requires:               dotnet-sdk-%{DOTNET_VERSION}

Requires:               gnome-common intltool glib2-devel redhat-rpm-config rpm-build fedora-packager
Requires:               meson
Requires:               redhat-rpm-config rpm-build
Requires:               msitools
Requires:               osslsigncode openssl openssl-pkcs11 gnutls vim-common
Requires:               hunspell-da hunspell-en-GB hunspell-en-US
Requires:               python
Requires:               sudo
Requires:		ige-mac-bundler

%description darwinx
Easy management of applications for macOS 64 bit



%prep

%setup -c %{name} -T

%build
dotnet new console
dotnet add package NLog --version 5.3.4

dotnet add package System.Security.Cryptography.Xml --version 8.0.1
dotnet add package System.Security.Cryptography.Pkcs --version 8.0.0
dotnet add package System.Security.Cryptography.ProtectedData --version 8.0.0
dotnet add package System.Configuration.ConfigurationManager --version 8.0.0

dotnet add package System.ServiceModel.Primitives --version 8.0.0
dotnet add package System.ServiceModel.Http --version 8.0.0
dotnet add package System.ServiceModel.NetTcp --version 8.0.0
dotnet add package System.ServiceModel.Federation --version 8.0.0
dotnet add package System.Web.Services.Description --version 8.0.0
dotnet add package System.ServiceModel.Syndication --version 8.0.0

dotnet add package System.Runtime.Caching --version 8.0.0

dotnet add package System.DirectoryServices --version 8.0.0
dotnet add package System.DirectoryServices.AccountManagement --version 8.0.0

dotnet add package System.CommandLine --version 2.0.0-beta4.22272.1

dotnet add package IdentityModel.OidcClient --version 6.0.0

dotnet add package Microsoft.IdentityModel.Protocols --version 8.1.0

dotnet add package Microsoft.Extensions.Caching.Memory --version 8.0.0
dotnet add package Microsoft.Extensions.Caching.Abstractions --version 8.0.0

dotnet add package Microsoft.Data.SqlClient --version 5.2.2

#dotnet add package Keycloak.AuthServices.Sdk --version 2.5.3

dotnet add package Mono.Data.Sqlite.Core --version 1.0.61.1

dotnet add package Npgsql --version 8.0.4

dotnet add package Mono.Cecil --version 0.11.6
#dotnet add package Mono.Addins --version 1.4.1
#dotnet add package Mono.Addins.CecilReflector --version 1.4.1

dotnet add package Tmds.DBus --version 0.20.0

dotnet add package ClosedXml --version 0.104.1

dotnet add package DocumentFormat.OpenXml --version 3.1.0
dotnet add package DocumentFormat.OpenXml.Framework --version 3.1.0
dotnet add package DocumentFormat.OpenXml.Linq --version 3.1.0
dotnet add package DocumentFormat.OpenXml.Features --version 3.1.0

dotnet add package GirCore.Gtk-4.0 --version 0.5.0
dotnet add package GirCore.Adw-1 --version 0.5.0

dotnet add package GirCore.WebKit-6.0 --version 0.5.0
dotnet add package GirCore.JavaScriptCore-6.0 --version 0.5.0

dotnet add package GirCore.Gst-1.0 --version 0.5.0
dotnet add package GirCore.GstBase-1.0 --version 0.5.0
dotnet add package GirCore.GstAudio-1.0 --version 0.5.0
dotnet add package GirCore.GstVideo-1.0 --version 0.5.0
dotnet add package GirCore.GstPbutils-1.0 --version 0.5.0

dotnet add package Newtonsoft.Json --version 13.0.3
dotnet add package BouncyCastle.Cryptography --version 2.4.0
dotnet add package MimeKit --version 4.8.0
dotnet add package MailKit --version 4.8.0
dotnet add package RestSharp --version 112.1.0
dotnet add package Sprache --version 2.3.1
dotnet add package PDFsharp-MigraDoc --version 6.1.1

dotnet add package nhapi.model.v231 --version 3.2.0
dotnet add package nhapi.model.v251 --version 3.2.0

sed -i -e 's!<PrivateAssets>all</PrivateAssets>!!g' *.csproj

dotnet publish -o any
dotnet publish --force --runtime linux-x64 -o lin
dotnet publish --force --runtime win-x64 -o win
dotnet publish --force --runtime osx-x64 -o darwinx

dotnet add package ServiceStack --version 8.4.0
dotnet publish -o other

%install
#if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
#DESTDIR=$RPM_BUILD_ROOT make install

install -d -m 755 $RPM_BUILD_ROOT%{linux_prefix}
install -m 644 lin/*.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 any/runtimes/unix/lib/net8.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{linux_prefix}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}
install -m 644 win/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 any/runtimes/unix/lib/net8.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/

install -d -m 755 $RPM_BUILD_ROOT%{darwinx_prefix}
install -m 644 darwinx/*.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 any/runtimes/unix/lib/net8.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{darwinx_prefix}/

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{darwinx_prefix}/

install -m 644 /usr/lib/AtkSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/CairoSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/ 
install -m 644 /usr/lib/GLibSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/GdkSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/GioSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/GtkSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/PangoSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/WebkitGtkSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/GdlSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 /usr/lib/GstSharp.dll $RPM_BUILD_ROOT%{linux_prefix}/

install -m 644 /usr/lib/AtkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/CairoSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GLibSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GdkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GioSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GtkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/PangoSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/WebkitGtkSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GdlSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 /usr/lib/GstSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}/

install -m 644 /usr/lib/AtkSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/CairoSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GLibSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GdkSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GioSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GtkSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/PangoSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/WebkitGtkSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GdlSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GstSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/
install -m 644 /usr/lib/GtkMacIntegrationSharp.dll $RPM_BUILD_ROOT%{darwinx_prefix}/

rm -f $RPM_BUILD_ROOT%{linux_prefix}/Microsoft.SqlServer.Server.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Microsoft.SqlServer.Server.dll
rm -f $RPM_BUILD_ROOT%{darwinx_prefix}/Microsoft.SqlServer.Server.dll

rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Rocks.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Rocks.dll
rm -f $RPM_BUILD_ROOT%{darwinx_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{darwinx_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{darwinx_prefix}/Mono.Cecil.Rocks.dll

rm -f $RPM_BUILD_ROOT%{linux_prefix}/GSharpKit-sdk-%{major_version}-%{version}.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/GSharpKit-sdk-%{major_version}-%{version}.dll
rm -f $RPM_BUILD_ROOT%{darwinx_prefix}/GSharpKit-sdk-%{major_version}-%{version}.dll

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%dir %{linux_prefix}
%{linux_prefix}/*.dll

%files mingw64
%defattr(-, root, root)
%dir %{mingw64_prefix}
%{mingw64_prefix}/*.dll

%files darwinx
%defattr(-, root, root)
%dir %{darwinx_prefix}
%{darwinx_prefix}/*.dll

###########################################################################
%changelog
* Thu May 09 2024 Mikkel Kruse Johnsen, GSharpKit <mikkel@gsharpkit.com>
- Update Npgsql for security CVE-2024-32655
- Update GirCore to 0.5.0
* Thu Oct 03 2017 Mikkel Kruse Johnsen, GSharpKit <mikkel@gsharpkit.com>
- Renamed to GSharpKit
* Thu Jun 08 2010 Mikkel Kruse Johnsen, Appbox <mikkel@appbox.info>
- First rpm build.


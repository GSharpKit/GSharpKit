%define _binary_payload w4.gzdio

#### DEFINES
%define DOTNET_VERSION 8.0

%define major_version 39
%define minor_version 0
%define sdk_version 100

%define linux_prefix /usr/lib/GSharpKit/sdk/%{major_version}
%define mingw64_prefix /usr/x86_64-w64-mingw32/sys-root/mingw/lib/GSharpKit/sdk/%{major_version}
%define mac64_prefix /Library/Frameworks/GSharpKit/sdk/%{major_version}

Summary: 		Easy management of applications
Name: 			GSharpKit-sdk-%{major_version}
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
Requires:               osslsigncode
Requires:               hunspell-da hunspell-en-GB hunspell-en-US
Requires:		python
Requires:		sudo

BuildRequires:		dotnet-runtime-%{DOTNET_VERSION}
BuildRequires:		GtkSharp

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
Requires:               osslsigncode
Requires:               hunspell-da hunspell-en-GB hunspell-en-US
Requires:               python
Requires:		sudo


%description mingw64
Easy management of applications for Windows 64 bit



%package macos64
Summary:                SDK for GSharpKit macOS 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

%description macos64
Easy management of applications for macOS 64 bit



%prep

%setup -c %{name} -T

%build
dotnet new console
dotnet add package NLog --version 5.2.8

dotnet add package System.Security.Cryptography.Xml --version 8.0.0
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

dotnet add package Microsoft.Data.SqlClient --version 5.1.2

# Now part of XMedicus and the helper is in runtime
#dotnet add package Mono.Posix.NETStandard --version 1.0.0

dotnet add package Mono.Data.Sqlite.Core --version 1.0.61.1

dotnet add package Npgsql --version 8.0.1

dotnet add package Mono.Cecil --version 0.11.5
#dotnet add package Mono.Addins --version 1.4.1
#dotnet add package Mono.Addins.CecilReflector --version 1.4.1

dotnet add package Tmds.DBus --version 0.15.0

dotnet add package GirCore.Gtk-4.0 --version 0.5.0-preview.3

dotnet add package Newtonsoft.Json --version 13.0.3
dotnet add package BouncyCastle.Cryptography --version 2.2.1
dotnet add package MimeKit --version 4.3.0
dotnet add package MailKit --version 4.3.0
dotnet add package RestSharp --version 106.15.0
dotnet add package Sprache --version 2.3.1
dotnet add package PDFsharp-MigraDoc --version 6.0.0

dotnet add package nhapi.model.v231 --version 3.2.0
dotnet add package nhapi.model.v251 --version 3.2.0

sed -i -e 's!<PrivateAssets>all</PrivateAssets>!!g' *.csproj

dotnet publish -o any
dotnet publish --force --runtime linux-x64 -o lin
dotnet publish --force --runtime win-x64 -o win
dotnet publish --force --runtime osx-x64 -o mac64
#dotnet publish --force --runtime osx-arm64 -o macarm

dotnet add package ServiceStack --version 8.0.0
dotnet publish -o other

%install
#if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
#DESTDIR=$RPM_BUILD_ROOT make install

install -d -m 755 $RPM_BUILD_ROOT%{linux_prefix}
install -m 644 lin/*.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 any/runtimes/unix/lib/net6.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{linux_prefix}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}
install -m 644 win/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 any/runtimes/unix/lib/net6.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/

install -d -m 755 $RPM_BUILD_ROOT%{mac64_prefix}
install -m 644 mac64/*.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 any/runtimes/unix/lib/net6.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{mac64_prefix}/

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{mac64_prefix}/

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

install -m 644 /usr/lib/AtkSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/CairoSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GLibSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GdkSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GioSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GtkSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/PangoSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/WebkitGtkSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GdlSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GstSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/
install -m 644 /usr/lib/GtkMacIntegrationSharp.dll $RPM_BUILD_ROOT%{mac64_prefix}/

rm -f $RPM_BUILD_ROOT%{linux_prefix}/Microsoft.SqlServer.Server.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Microsoft.SqlServer.Server.dll
rm -f $RPM_BUILD_ROOT%{mac64_prefix}/Microsoft.SqlServer.Server.dll

rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{linux_prefix}/Mono.Cecil.Rocks.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Mono.Cecil.Rocks.dll
rm -f $RPM_BUILD_ROOT%{mac64_prefix}/Mono.Cecil.Mdb.dll
rm -f $RPM_BUILD_ROOT%{mac64_prefix}/Mono.Cecil.Pdb.dll
rm -f $RPM_BUILD_ROOT%{mac64_prefix}/Mono.Cecil.Rocks.dll

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

%files macos64
%defattr(-, root, root)
%dir %{mac64_prefix}
%{mac64_prefix}/*.dll

###########################################################################
%changelog
* Thu Oct 03 2017 Mikkel Kruse Johnsen, GSharpKit <mikkel@gsharpkit.com>
- Renamed to GSharpKit
* Thu Jun 08 2010 Mikkel Kruse Johnsen, Appbox <mikkel@appbox.info>
- First rpm build.


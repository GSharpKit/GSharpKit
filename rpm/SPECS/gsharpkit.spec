%define MINGW_FILESYSTEM_VERSION 119
%define BINUTILS_VERSION 2.34
%define HEADER_CRT_THREAD_VERSION 7.0.0
%define COMPILER_VERSION 10.2.1
%define PKG_CONFIG_VERSION 0.28
%define TERMCAP_VERSION 1.3.1
%define ZLIB_VERSION 1.2.11
%define ICONV_VERSION 0.0.8
%define GETTEXT_VERSION 0.20.2
%define LIBFFI_VERSION 3.1
%define PCRE_VERSION 8.43
%define GLIB2_VERSION 2.64.3
%define PIXMAN_VERSION 0.40.0
%define BZIP2_VERSION 1.0.8
%define FREETYPE_VERSION 2.10.2
%define EXPAT_VERSION 2.2.8
%define FONTCONFIG_VERSION 2.13.1
%define LIBPNG_VERSION 1.6.37
%define LIBJPEG_TURBO_VERSION 1.5.3
%define LIBTIFF_VERSION 4.0.9
%define CAIRO_VERSION 1.16.0
%define ICU_VERSION 57.1
%define HARFBUZZ_VERSION 2.6.8
%define FRIBIDI_VERSION 1.0.10
%define PANGO_VERSION 1.44.7
%define ATK_VERSION 2.36.0
%define JASPER_VERSION 1.900.29
%define LIBXML2_VERSION 2.9.10
%define LIBPSL_VERSION 0.21.0
%define LIBCROCO_VERSION 0.6.12
%define LIBEPOXY_VERSION 1.5.4
%define LIBRSVG2_VERSION 2.40.19
%define GDK_PIXBUF_VERSION 2.40.0
%define GTK3_VERSION 3.24.23
%define GTK4_VERSION 4.6.5
%define GDL_VERSION 3.40.0
%define GTK3_ADWAITA_VERSION 3.26.0

%define GTK_MAC_BUNDLER_VERSION 0.5
%define GTK_MAC_INTEGRATION_VERSION 2.1.3

%define LIBGPG_ERROR_VERSION 1.36
%define LIBGCRYPT_VERSION 1.8.4
%define GMP_VERSION 6.1.2
%define NETTLE_VERSION 3.5.1
%define P11_KIT_VERSION 0.23.16.1
%define LIBTASN1_VERSION 4.16.0
%define READLINE_VERSION 8.0
%define LIBUNISTRING_VERSION 0.9.10
%define GNUTLS_VERSION 3.6.15
%define OPENSSL_VERSION 1.1.1
%define GLIB_NETWORKING_VERSION 2.64.3

%define LIBXSLT_VERSION 1.1.34
%define SQLITE_VERSION 3.34.0
%define LIBSOUP_VERSION 2.70.0

%define HUNSPELL_VERSION 1.7.0
%define ENCHANT_VERSION 1.6.0

%define LIBOGG_VERSION 1.3.3
%define LIBVORBIS_VERSION 1.3.6
%define LIBWEBP_VERSION 1.1.0
%define GSTREAMER1_VERSION 1.18.0
%define GSTREAMER1_PLUGINS_BASE_VERSION 1.18.0
%define GSTREAMER1_PLUGINS_GOOD_VERSION 1.18.0
%define GSTREAMER1_PLUGINS_BAD_VERSION 1.18.0

#define LIBEXIF_VERSION 0.6.20

%define DBUS_VERSION 1.13.16

#define LIBUSB_VERSION 1.0.22
#define LIBGPHOTO2_VERSION 2.5.16



#### DEFINES
%define DOTNET_VERSION 8.0

%define major_version 39
%define minor_version 0

%define linux_prefix /usr/lib/%{name}/sdk/%{major_version}
%define mingw64_prefix /usr/x86_64-w64-mingw32/sys-root/mingw/lib/%{name}/sdk/%{major_version}

Summary: 		Easy management of applications
Name: 			GSharpKit
Version:		%{major_version}.%{minor_version}
Release:		1%{?dist}
License:		GPL
Group: 			Applications/Desktop
Source1:		gsharpkit.repo
Source2:		RPM-GPG-KEY-gsharpkit
Source3:		microsoft-prod.repo
Source4:		RPM-GPG-KEY-microsoft
URL:			http://www.gsharpkit.com
Vendor:			GSharpKit
Packager:		Mikkel Kruse Johnsen <mikkel@gsharpkit.com>
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch
AutoReqProv:    	no

Requires:		GSharpKit-runtime = %{version}

%description
Easy management of applications


%package release
Summary:                Runtime environment for GSharpKit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:    	no

%description release
Easy management of applications


%package runtime
Summary: 		Runtime environment for GSharpKit
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch
AutoReqProv:            no

Requires:               dotnet-runtime-%{DOTNET_VERSION}

#Requires:		libcroco >= %{LIBCROCO_VERSION}
Requires:		libepoxy >= %{LIBEPOXY_VERSION}
Requires:		librsvg2 >= %{LIBRSVG2_VERSION}
Requires:		gtk3 >= %{GTK3_VERSION}
Requires:		gtk4 >= %{GTK4_VERSION}
Requires:		adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}

Requires:		libgdl >= %{GDL_VERSION}

Requires:		libsoup >= %{LIBSOUP_VERSION}
Requires:		hunspell >= %{HUNSPELL_VERSION}
Requires:		enchant >= %{ENCHANT_VERSION}

#Requires:		libusbx >= %{LIBUSB_VERSION}
#Requires:		libexif >= %{LIBEXIF_VERSION}
#Requires:		libgphoto2 >= %{LIBGPHOTO2_VERSION}

Requires:		libogg => %{LIBOGG_VERSION}
Requires:		libvorbis => %{LIBVORBIS_VERSION}
Requires:		libwebp => %{LIBWEBP_VERSION}
Requires:		gstreamer1 => %{GSTREAMER1_VERSION}
Requires:		gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:		gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:		gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}

%description runtime
Easy management of applications




%package sdk-%{major_version}
Summary: 		SDK for GSharpKit
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch
AutoReqProv:            no

Requires:		dotnet-sdk-%{DOTNET_VERSION}
BuildRequires:		dotnet-runtime-%{DOTNET_VERSION}

BuildRequires:		GtkSharp

%description sdk-%{major_version}
Easy management of applications

%package sdk-devel
Summary:                SDK for GSharpKit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

Requires:               gnome-common intltool glib2-devel redhat-rpm-config rpm-build fedora-packager
Requires:               meson

Requires:               dotnet-sdk-%{DOTNET_VERSION}

%description sdk-devel
Easy management of applications


%package sdk-mingw64
Summary:                SDK for GSharpKit Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

Requires:               redhat-rpm-config rpm-build
Requires:               msitools
Requires:               osslsigncode
Requires:               hunspell-da

Requires:               mingw64-winpthreads >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-termcap >= %{TERMCAP_VERSION}
Requires:               mingw64-zlib >= %{ZLIB_VERSION}
Requires:               mingw64-win-iconv >= %{ICONV_VERSION}
Requires:               mingw64-gettext >= %{GETTEXT_VERSION}
Requires:               mingw64-libffi >= %{LIBFFI_VERSION}
Requires:               mingw64-pcre >= %{PCRE_VERSION}
Requires:               mingw64-glib2 >= %{GLIB2_VERSION}
Requires:               mingw64-pixman >= %{PIXMAN_VERSION}
Requires:               mingw64-bzip2 >= %{BZIP2_VERSION}
Requires:               mingw64-freetype >= %{FREETYPE_VERSION}
Requires:               mingw64-expat >= %{EXPAT_VERSION}
Requires:               mingw64-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               mingw64-libpng >= %{LIBPNG_VERSION}
Requires:               mingw64-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               mingw64-libtiff >= %{LIBTIFF_VERSION}
Requires:               mingw64-cairo >= %{CAIRO_VERSION}
Requires:               mingw64-icu >= %{ICU_VERSION}
Requires:               mingw64-icu57 >= %{ICU_VERSION}
Requires:               mingw64-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               mingw64-fribidi >= %{FRIBIDI_VERSION}
Requires:               mingw64-pango >= %{PANGO_VERSION}
Requires:               mingw64-atk >= %{ATK_VERSION}
Requires:               mingw64-jasper >= %{JASPER_VERSION}
Requires:               mingw64-libxml2 >= %{LIBXML2_VERSION}
Requires:               mingw64-libpsl >= %{LIBPSL_VERSION}
Requires:               mingw64-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               mingw64-libcroco >= %{LIBCROCO_VERSION}
Requires:               mingw64-libepoxy >= %{LIBEPOXY_VERSION}
Requires:               mingw64-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               mingw64-gtk3 >= %{GTK3_VERSION}
Requires:               mingw64-gtk4 >= %{GTK4_VERSION}
Requires:               mingw64-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               mingw64-libgdl >= %{GDL_VERSION}

Requires:               mingw64-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               mingw64-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               mingw64-gmp >= %{GMP_VERSION}
Requires:               mingw64-nettle >= %{NETTLE_VERSION}
Requires:               mingw64-p11-kit >= %{P11_KIT_VERSION}
Requires:               mingw64-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               mingw64-readline >= %{READLINE_VERSION}
Requires:               mingw64-libunistring  >= %{LIBUNISTRING_VERSION}
Requires:               mingw64-gnutls  >= %{GNUTLS_VERSION}
Requires:               mingw64-openssl  >= %{OPENSSL_VERSION}
Requires:               mingw64-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               mingw64-libxslt >= %{LIBXSLT_VERSION}
Requires:               mingw64-sqlite >= %{SQLITE_VERSION}
Requires:               mingw64-libsoup >= %{LIBSOUP_VERSION}

Requires:               mingw64-hunspell >= %{HUNSPELL_VERSION}
Requires:               mingw64-enchant >= %{ENCHANT_VERSION}

Requires:               mingw64-libogg >= %{LIBOGG_VERSION}
Requires:               mingw64-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               mingw64-libwebp >= %{LIBWEBP_VERSION}
Requires:               mingw64-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               mingw64-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               mingw64-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:               mingw64-gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}

Requires:               mingw64-dbus >= %{DBUS_VERSION}

#Requires:		mingw64-libusbx >= %{LIBUSB_VERSION}
#Requires:		mingw64-libexif >= %{LIBEXIF_VERSION}
#Requires:		mingw64-libgphoto2 >= %{LIBGPHOTO2_VERSION}

%description sdk-mingw64
Easy management of applications for Windows 64 bit


%package sdk-mingw64-devel
Summary:                SDK for GSharpKit Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
AutoReqProv:            no

Requires:		GSharpKit-sdk-mingw64

Requires:               mingw-w64-tools
Requires:               mingw64-filesystem >= %{MINGW_FILESYSTEM_VERSION}
Requires:               mingw64-binutils >= %{BINUTILS_VERSION}
Requires:               mingw64-crt >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-headers >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw64-cpp >= %{COMPILER_VERSION}
Requires:               mingw64-gcc >= %{COMPILER_VERSION}
Requires:               mingw64-gcc-c++ >= %{COMPILER_VERSION}
Requires:               mingw64-gcc-objc >= %{COMPILER_VERSION}
Requires:               mingw64-pkg-config >= %{PKG_CONFIG_VERSION}
Requires:		mingw64-libidn

%description sdk-mingw64-devel
Easy management of applications for Windows


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

dotnet add package Mono.Posix.NETStandard --version 1.0.0

dotnet add package Mono.Data.Sqlite.Core --version 1.0.61.1

dotnet add package Npgsql --version 8.0.1

dotnet add package Mono.Addins --version 1.4.1
dotnet add package Mono.Addins.CecilReflector --version 1.4.1

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

dotnet add package ServiceStack --version 8.0.0
dotnet publish -o other

%install
#if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
#DESTDIR=$RPM_BUILD_ROOT make install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
cp %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

install -d -m 755 $RPM_BUILD_ROOT%{linux_prefix}
install -m 644 lin/*.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 lin/*.so $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 any/runtimes/unix/lib/net6.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{linux_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{linux_prefix}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}
install -m 644 win/*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 any/runtimes/unix/lib/net6.0/Microsoft.Data.SqlClient.dll $RPM_BUILD_ROOT%{mingw64_prefix}/
install -m 644 other/ServiceStack*.dll $RPM_BUILD_ROOT%{mingw64_prefix}/

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

rm -f $RPM_BUILD_ROOT%{linux_prefix}/Microsoft.SqlServer.Server.dll
rm -f $RPM_BUILD_ROOT%{mingw64_prefix}/Microsoft.SqlServer.Server.dll

%clean
#rm -rf $RPM_BUILD_ROOT

%files release
%defattr(-, root, root)
%{_sysconfdir}/yum.repos.d/gsharpkit.repo
%{_sysconfdir}/yum.repos.d/microsoft-prod.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-gsharpkit
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-microsoft

%files runtime
%defattr(-, root, root)

%files sdk-%{major_version}
%defattr(-, root, root)
%{linux_prefix}/*.dll
%{linux_prefix}/*.so

%files sdk-devel
%defattr(-, root, root)

%files sdk-mingw64
%defattr(-, root, root)
%{mingw64_prefix}/*.dll

%files sdk-mingw64-devel
%defattr(-, root, root)

###########################################################################
%changelog
* Thu Oct 03 2017 Mikkel Kruse Johnsen, GSharpKit <mikkel@gsharpkit.com>
- Renamed to GSharpKit
* Thu Jun 08 2010 Mikkel Kruse Johnsen, Appbox <mikkel@appbox.info>
- First rpm build.


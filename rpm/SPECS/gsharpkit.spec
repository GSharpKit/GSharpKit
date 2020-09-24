%define MINGW_FILESYSTEM_VERSION 113
%define BINUTILS_VERSION 2.32
%define HEADER_CRT_THREAD_VERSION 6.0.0
%define COMPILER_VERSION 9.2.1
%define PKG_CONFIG_VERSION 0.28
%define TERMCAP_VERSION 1.3.1
%define ZLIB_VERSION 1.2.11
%define ICONV_VERSION 0.0.8
%define GETTEXT_VERSION 0.20.1
%define LIBFFI_VERSION 3.1
%define PCRE_VERSION 8.43
%define GLIB2_VERSION 2.64.3
%define PIXMAN_VERSION 0.38.4
%define BZIP2_VERSION 1.0.8
%define FREETYPE_VERSION 2.10.1
%define EXPAT_VERSION 2.2.8
%define FONTCONFIG_VERSION 2.13.1
%define LIBPNG_VERSION 1.6.37
%define LIBJPEG_TURBO_VERSION 1.5.3
%define LIBTIFF_VERSION 4.0.9
%define CAIRO_VERSION 1.16.0
%define ICU_VERSION 65.1
%define HARFBUZZ_VERSION 2.6.4
%define FRIBIDI_VERSION 1.0.8
%define PANGO_VERSION 1.44.7
%define ATK_VERSION 2.34.1
%define JASPER_VERSION 1.900.29
%define LIBXML2_VERSION 2.9.10
%define LIBPSL_VERSION 0.21.0
%define LIBCROCO_VERSION 0.6.12
%define LIBEPOXY_VERSION 1.5.4
%define LIBRSVG2_VERSION 2.40.19
%define GDK_PIXBUF_VERSION 2.40.0
%define GTK3_VERSION 3.24.20
%define GDL_VERSION 3.34.0
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
%define GNUTLS_VERSION 3.5.16
%define OPENSSL_VERSION 1.1.1
%define GLIB_NETWORKING_VERSION 2.64.3

%define LIBXSLT_VERSION 1.1.33
%define SQLITE_VERSION 3.31.1
%define LIBSOUP_VERSION 2.70.0

%define HUNSPELL_VERSION 1.7.0
%define ENCHANT_VERSION 1.6.0

%define LIBOGG_VERSION 1.3.3
%define LIBVORBIS_VERSION 1.3.6
%define LIBWEBP_VERSION 1.1.0
%define GSTREAMER1_VERSION 1.16.2
%define GSTREAMER1_PLUGINS_BASE_VERSION 1.16.2
%define GSTREAMER1_PLUGINS_GOOD_VERSION 1.16.2
%define GSTREAMER1_PLUGINS_BAD_VERSION 1.16.2
%define WEBKITGTK3_VERSION 2.4.11
#define LIBEXIF_VERSION 0.6.20

%define DBUS_VERSION 1.12.12
%define DBUS_GLIB_VERSION 0.110

#define LIBUSB_VERSION 1.0.22
#define LIBGPHOTO2_VERSION 2.5.16
#define SANE_BACKENDS_VERSION 1.0.27
#define TWAIN_DSM_VERSION 2.3.1

%define MONO_CORE_VERSION 6.10.0.104
%define MONO_DATA_SQLITE_VERSION 1.0.61
%define MONO_POSIX_NETSTANDARD_VERSION 1.0.0
%define DBUS_SHARP_VERSION 2:0.9.2
%define DBUS_GLIB_SHARP_VERSION 0.6.0
%define GTK3_SHARP_VERSION 3.22.25.98
%define GDL_SHARP_VERSION 3.26.0
%define GST_SHARP_VERSION 1.16.0
%define WEBKITGTK3_SHARP_VERSION 2.4.11
%define GTK_MAC_INTEGRATION_SHARP_VERSION 2.0.7

%define MICROSOFT_CSHARP_VERSION 4.5.0
%define NPGSQL_VERSION 4.1.4
%define MONO_ADDINS_VERSION 1.3.8
%define NEWTONSOFT_JSON_VERSION 12.0.3
%define BOUNCY_CASTLE_VERSION 1.8.5
%define MIMEKIT_VERSION 2.9.1
%define MAILKIT_VERSION 2.8.0
%define SERVICE_STACK_VERSION 5.9.0
%define REST_SHARP_VERSION 106.11.4
%define SEALAPI_VERSION 4.1.0
%define PDFSHARP_MIGRADOC_VERSION 1.50.5147
%define SPRACHE_VERSION 2.2.0
#define SHARP_ZIP_LIB_VERSION 1.0.0
#define LIBGPHOTO2_SHARP_VERSION 0.3.2
#define SHARP_CAMERA_VERSION 0.3.7

Summary: 		Easy management of applications
Name: 			GSharpKit
Version:		32.4
Release:		1%{?dist}
License:		GPL
Group: 			Applications/Desktop
Source1:		yum_ignoreos.conf
Source2:		yum_ignoreos.py
Source3:		gsharpkit.repo
Source4:		RPM-GPG-KEY-gsharpkit
Source5:		macros.darwinx
Source6:		darwinx-cmake
Source7:		darwinx-configure 
Source8:		darwinx-make
Source9:		darwinx-pkg-config
Source10:		mono-centos7.repo
Source11:		RPM-GPG-KEY-xamarin
Source12:		microsoft-prod.repo
Source13:		RPM-GPG-KEY-microsoft
Source14:		mingw-mono.pc
URL:			http://www.gsharpkit.com
Vendor:			GSharpKit
Packager:		Mikkel Kruse Johnsen <mikkel@gsharpkit.com>
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch

Requires:		GSharpKit-runtime = %{version}

Obsoletes:		appbox
Provides:		appbox

%description
Easy management of applications


%package release
Summary:                Runtime environment for GSharpKit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-release
Provides:               appbox-release

%description release
Easy management of applications


%package runtime
Summary: 		Runtime environment for GSharpKit
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch
Obsoletes:              appbox-runtime
Provides:               appbox-runtime

#Obsoletes:		fedora-obsolete-packages

Requires:		mono-core >= %{MONO_CORE_VERSION}
Requires:		mono-extras >= %{MONO_CORE_VERSION}
Requires:		mono-locale-extras >= %{MONO_CORE_VERSION}
Requires:		mono-data >= %{MONO_CORE_VERSION}
Requires:		mono-data-sqlite >= %{MONO_CORE_VERSION}
Requires:		Microsoft.CSharp >= %{MICROSOFT_CSHARP_VERSION}
Requires:		Mono.Posix.NETStandard >= %{MONO_POSIX_NETSTANDARD_VERSION}
Requires:		Mono.Data.Sqlite >= %{MONO_DATA_SQLITE_VERSION}
Requires:		Npgsql >= %{NPGSQL_VERSION}
Requires:		mono-web >= %{MONO_CORE_VERSION}
Requires:		mono-wcf >= %{MONO_CORE_VERSION}
Requires:		mono-mvc >= %{MONO_CORE_VERSION}
Requires:		mono-winfxcore >= %{MONO_CORE_VERSION}

Requires:		Mono.Addins >= %{MONO_ADDINS_VERSION}
Requires:		dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:		dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:		dbus-sharp-glib-devel >= %{DBUS_GLIB_SHARP_VERSION}

Requires:		libcroco >= %{LIBCROCO_VERSION}
Requires:		libepoxy >= %{LIBEPOXY_VERSION}
Requires:		librsvg2 >= %{LIBRSVG2_VERSION}
Requires:		gtk3 >= %{GTK3_VERSION}
Requires:		adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:		GtkSharp >= %{GTK3_SHARP_VERSION}

Requires:		libgdl >= %{GDL_VERSION}
Requires:		GdlSharp >= %{GDL_SHARP_VERSION}

Requires:		libsoup >= %{LIBSOUP_VERSION}
Requires:		hunspell >= %{HUNSPELL_VERSION}
Requires:		enchant >= %{ENCHANT_VERSION}
Requires:		webkitgtk3 >= %{WEBKITGTK3_VERSION}
Requires:		webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}

#Requires:		libusbx >= %{LIBUSB_VERSION}
#Requires:		libexif >= %{LIBEXIF_VERSION}
#Requires:		libgphoto2 >= %{LIBGPHOTO2_VERSION}
#Requires:		sane-backends >= %{SANE_BACKENDS_VERSION}
#Requires:		twaindsm >= %{TWAIN_DSM_VERSION}

Requires:		libogg => %{LIBOGG_VERSION}
Requires:		libvorbis => %{LIBVORBIS_VERSION}
Requires:		libwebp => %{LIBWEBP_VERSION}
Requires:		gstreamer1 => %{GSTREAMER1_VERSION}
Requires:		gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:		gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:		gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:		GstSharp >= %{GST_SHARP_VERSION}
Requires:		Newtonsoft.Json >= %{NEWTONSOFT_JSON_VERSION}
Requires:		BouncyCastle >= %{BOUNCY_CASTLE_VERSION}
Requires:		MimeKit >= %{MIMEKIT_VERSION}
Requires:		MailKit >= %{MAILKIT_VERSION}
Requires:		ServiceStack >= %{SERVICE_STACK_VERSION}
Requires:		RestSharp >= %{REST_SHARP_VERSION}
Requires:		Seal.net >= %{SEALAPI_VERSION}
Requires:		Sprache >= %{SPRACHE_VERSION}
Requires:		PDFsharp-MigraDoc >= %{PDFSHARP_MIGRADOC_VERSION}
#Requires:		SharpZipLib >= %{SHARP_ZIP_LIB_VERSION}
#Requires:		libgphoto2-sharp >= %{LIBGPHOTO2_SHARP_VERSION}
#Requires:		SharpCamera >= %{SHARP_CAMERA_VERSION}

%description runtime
Easy management of applications




%package sdk
Summary: 		SDK for GSharpKit
License:		GPL
Group: 			Applications/Desktop
BuildArch:		noarch
Obsoletes:              appbox-sdk
Provides:               appbox-sdk
Provides:		distribution-release

Requires:		GSharpKit-runtime = %{version}

Requires:		gnome-common intltool glib2-devel redhat-rpm-config rpm-build fedora-packager
Requires:		meson

Requires:		gtk-sharp3-devel gtk-sharp3-gapi

Requires:		gnome-sharp
Requires:		dotnet-sdk-2.2 dotnet-sdk-3.1
Requires:		msbuild
Requires:		netstandard netstandard-targeting-pack-2.1


%description sdk
Easy management of applications




%package sdk-mingw32
Summary:                SDK for GSharpKit Mingw 32 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-mingw32
Provides:               appbox-sdk-mingw32


Requires:               mingw32-winpthreads >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-termcap >= %{TERMCAP_VERSION}
Requires:               mingw32-zlib >=	%{ZLIB_VERSION}
Requires:               mingw32-win-iconv >= %{ICONV_VERSION}
Requires:               mingw32-gettext >= %{GETTEXT_VERSION}
Requires:               mingw32-libffi >= %{LIBFFI_VERSION}
Requires:               mingw32-pcre >= %{PCRE_VERSION}
Requires:               mingw32-glib2 >= %{GLIB2_VERSION}
Requires:               mingw32-pixman >= %{PIXMAN_VERSION}
Requires:               mingw32-bzip2 >= %{BZIP2_VERSION}
Requires:               mingw32-freetype >= %{FREETYPE_VERSION}
Requires:               mingw32-expat >= %{EXPAT_VERSION}
Requires:               mingw32-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               mingw32-libpng >= %{LIBPNG_VERSION}
Requires:               mingw32-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               mingw32-libtiff >= %{LIBTIFF_VERSION}
Requires:               mingw32-cairo >= %{CAIRO_VERSION}
Requires:               mingw32-icu >= %{ICU_VERSION}
Requires:               mingw32-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               mingw32-fribidi >= %{FRIBIDI_VERSION}
Requires:               mingw32-pango >= %{PANGO_VERSION}
Requires:               mingw32-atk >= %{ATK_VERSION}
Requires:               mingw32-jasper >= %{JASPER_VERSION}
Requires:               mingw32-libxml2 >= %{LIBXML2_VERSION}
Requires:               mingw32-libpsl >= %{LIBPSL_VERSION}
Requires:               mingw32-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               mingw32-libcroco >= %{LIBCROCO_VERSION}
Requires:               mingw32-libepoxy >= %{LIBEPOXY_VERSION}
Requires:               mingw32-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               mingw32-gtk3 >= %{GTK3_VERSION}
Requires:               mingw32-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               mingw32-libgdl >= %{GDL_VERSION}

Requires:               mingw32-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               mingw32-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               mingw32-gmp >= %{GMP_VERSION}
Requires:               mingw32-nettle >= %{NETTLE_VERSION}
Requires:               mingw32-p11-kit >= %{P11_KIT_VERSION}
Requires:               mingw32-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               mingw32-readline >= %{READLINE_VERSION}
Requires:               mingw32-libunistring >= %{LIBUNISTRING_VERSION}
Requires:               mingw32-gnutls 	>= %{GNUTLS_VERSION}
Requires:               mingw32-openssl >= %{OPENSSL_VERSION}
Requires:               mingw32-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               mingw32-libxslt >= %{LIBXSLT_VERSION}
Requires:               mingw32-sqlite >= %{SQLITE_VERSION}
Requires:               mingw32-libsoup >= %{LIBSOUP_VERSION}

Requires:               mingw32-hunspell >= %{HUNSPELL_VERSION}
Requires:               mingw32-enchant >= %{ENCHANT_VERSION}

Requires:               mingw32-libogg >= %{LIBOGG_VERSION}
Requires:               mingw32-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               mingw32-libwebp >= %{LIBWEBP_VERSION}
Requires:               mingw32-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               mingw32-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               mingw32-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
Requires:               mingw32-gstreamer1-plugins-bad-free >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:               mingw32-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               mingw32-dbus >= %{DBUS_VERSION}
Requires:               mingw32-dbus-glib >= %{DBUS_GLIB_VERSION}

#Requires:		mingw32-libusbx >= %{LIBUSB_VERSION}
#Requires:		mingw32-libexif >= %{LIBEXIF_VERSION}
#Requires:		mingw32-libgphoto2 >= %{LIBGPHOTO2_VERSION}
#Requires:		mingw32-sane-backends >= %{SANE_BACKENDS_VERSION}
#Requires:		mingw32-twaindsm >= %{TWAIN_DSM_VERSION}

Requires:               mingw32-Microsoft.CSharp >= %{MICROSOFT_CSHARP_VERSION}
Requires:               mingw32-Mono.Posix.NETStandard >= %{MONO_POSIX_NETSTANDARD_VERSION}
Requires:               mingw32-Mono.Data.Sqlite >= %{MONO_DATA_SQLITE_VERSION}
#Requires:               mingw32-mono-core >= %{MONO_CORE_VERSION}
Requires:               mingw32-Npgsql >= %{NPGSQL_VERSION}
Requires:               mingw32-GtkSharp >= %{GTK3_SHARP_VERSION}
Requires:               mingw32-GdlSharp >= %{GDL_SHARP_VERSION}
Requires:               mingw32-Mono.Addins >= %{MONO_ADDINS_VERSION}
Requires:               mingw32-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               mingw32-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               mingw32-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:		mingw32-GstSharp >= %{GST_SHARP_VERSION}
Requires:		mingw32-Newtonsoft.Json >= %{NEWTONSOFT_JSON_VERSION}
Requires:               mingw32-BouncyCastle >= %{BOUNCY_CASTLE_VERSION}
Requires:               mingw32-MimeKit >= %{MIMEKIT_VERSION}
Requires:               mingw32-MailKit >= %{MAILKIT_VERSION}
Requires:		mingw32-ServiceStack >= %{SERVICE_STACK_VERSION}
Requires:		mingw32-RestSharp >= %{REST_SHARP_VERSION}
Requires:		mingw32-Seal.net >= %{SEALAPI_VERSION}
Requires:               mingw32-Sprache >= %{SPRACHE_VERSION}
Requires:               mingw32-PDFsharp-MigraDoc >= %{PDFSHARP_MIGRADOC_VERSION}
#Requires:		mingw32-SharpZipLib >= %{SHARP_ZIP_LIB_VERSION}
#Requires:		mingw32-libgphoto2-sharp >= %{LIBGPHOTO2_SHARP_VERSION}
#Requires:		mingw32-SharpCamera >= %{SHARP_CAMERA_VERSION}


%description sdk-mingw32
Easy management of applications for Windows 32 bit



%package sdk-mingw64
Summary:                SDK for GSharpKit Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-mingw64
Provides:               appbox-sdk-mingw64

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
Requires:               mingw64-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               mingw64-dbus >= %{DBUS_VERSION}
Requires:               mingw64-dbus-glib >= %{DBUS_GLIB_VERSION}

#Requires:		mingw64-libusbx >= %{LIBUSB_VERSION}
#Requires:		mingw64-libexif >= %{LIBEXIF_VERSION}
#Requires:		mingw64-libgphoto2 >= %{LIBGPHOTO2_VERSION}
#Requires:		mingw64-sane-backends >= %{SANE_BACKENDS_VERSION}
#Requires:		mingw64-twaindsm >= %{TWAIN_DSM_VERSION}

Requires:               mingw64-Microsoft.CSharp >= %{MICROSOFT_CSHARP_VERSION}
Requires:               mingw64-Mono.Posix.NETStandard >= %{MONO_POSIX_NETSTANDARD_VERSION}
Requires:               mingw64-Mono.Data.Sqlite >= %{MONO_DATA_SQLITE_VERSION}
#Requires:               mingw64-mono-core >= %{MONO_CORE_VERSION}
Requires:               mingw64-Npgsql >= %{NPGSQL_VERSION}
Requires:               mingw64-GtkSharp >= %{GTK3_SHARP_VERSION}
Requires:               mingw64-GdlSharp >= %{GDL_SHARP_VERSION}
Requires:               mingw64-Mono.Addins >= %{MONO_ADDINS_VERSION}
Requires:               mingw64-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               mingw64-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               mingw64-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:               mingw64-GstSharp >= %{GST_SHARP_VERSION}
Requires:               mingw64-Newtonsoft.Json >= %{NEWTONSOFT_JSON_VERSION}
Requires:               mingw64-BouncyCastle >= %{BOUNCY_CASTLE_VERSION}
Requires:               mingw64-MimeKit >= %{MIMEKIT_VERSION}
Requires:               mingw64-MailKit >= %{MAILKIT_VERSION}
Requires:		mingw64-ServiceStack >= %{SERVICE_STACK_VERSION}
Requires:		mingw64-RestSharp >= %{REST_SHARP_VERSION}
Requires:		mingw64-Seal.net >= %{SEALAPI_VERSION}
Requires:               mingw64-Sprache >= %{SPRACHE_VERSION}
Requires:               mingw64-PDFsharp-MigraDoc >= %{PDFSHARP_MIGRADOC_VERSION}
#Requires:		mingw64-SharpZipLib >= %{SHARP_ZIP_LIB_VERSION}
#Requires:		mingw64-libgphoto2-sharp >= %{LIBGPHOTO2_SHARP_VERSION}
#Requires:		mingw64-SharpCamera >= %{SHARP_CAMERA_VERSION}


%description sdk-mingw64
Easy management of applications for Windows 64 bit


%package sdk-mingw
Summary:                SDK for GSharpKit Mingw 32/64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-mingw
Provides:               appbox-sdk-mingw

Requires:		GSharpKit-sdk
Requires:		GSharpKit-sdk-mingw32
Requires:		GSharpKit-sdk-mingw64

%description sdk-mingw
Easy management of applications for Windows



%package sdk-mingw-devel
Summary:                SDK for GSharpKit Mingw 32/64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-mingw-devel
Provides:               appbox-sdk-mingw-devel

Requires:               GSharpKit-sdk-mingw32-devel
Requires:               GSharpKit-sdk-mingw64-devel

%description sdk-mingw-devel
Easy management of applications for Windows


%package sdk-mingw32-devel
Summary:                SDK for GSharpKit Mingw 32 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-mingw32-devel
Provides:               appbox-mingw32-devel


Requires:               GSharpKit-sdk-mingw32

Requires:		redhat-rpm-config rpm-build
Requires:		msitools
Requires:		osslsigncode
Requires:		hunspell-da
Requires:               mingw32-filesystem >= %{MINGW_FILESYSTEM_VERSION}
Requires:               mingw32-binutils >= %{BINUTILS_VERSION}
Requires:               mingw32-crt >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-headers >= %{HEADER_CRT_THREAD_VERSION}
Requires:               mingw32-cpp >= %{COMPILER_VERSION}
Requires:               mingw32-gcc >= %{COMPILER_VERSION}
Requires:               mingw32-gcc-c++ >= %{COMPILER_VERSION}
Requires:               mingw32-gcc-objc >= %{COMPILER_VERSION}
Requires:               mingw32-pkg-config >= %{PKG_CONFIG_VERSION}
Requires:		mingw32-libidn

%description sdk-mingw32-devel
Easy management of applications for Windows


%package sdk-mingw64-devel
Summary:                SDK for GSharpKit Mingw 64 bit
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-mingw64-devel
Provides:               appbox-sdk-mingw64-devel

Requires:		GSharpKit-sdk-mingw64

Requires:               redhat-rpm-config rpm-build
Requires:		msitools
Requires:		osslsigncode
Requires:		hunspell-da
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



%package sdk-darwinx
Summary:                SDK for GSharpKit Mac OS X
License:                GPL
Group:                  Applications/Desktop
BuildArch:              noarch
Obsoletes:              appbox-sdk-darwinx
Provides:               appbox-sdk-darwinx

Requires:		ige-mac-bundler >= %{GTK_MAC_BUNDLER_VERSION}
Requires:		hunspell-da
Requires:               darwinx-gettext >= %{GETTEXT_VERSION}
Requires:               darwinx-libffi >= %{LIBFFI_VERSION}
Requires:               darwinx-pcre >= %{PCRE_VERSION}
Requires:               darwinx-glib2 >= %{GLIB2_VERSION}
Requires:               darwinx-pixman >= %{PIXMAN_VERSION}
Requires:               darwinx-freetype >= %{FREETYPE_VERSION}
Requires:               darwinx-fontconfig >= %{FONTCONFIG_VERSION}
Requires:               darwinx-libpng >= %{LIBPNG_VERSION}
Requires:               darwinx-libjpeg-turbo >= %{LIBJPEG_TURBO_VERSION}
Requires:               darwinx-libtiff >= %{LIBTIFF_VERSION}
Requires:               darwinx-cairo >= %{CAIRO_VERSION}
Requires:               darwinx-icu >= %{ICU_VERSION}
Requires:               darwinx-harfbuzz >= %{HARFBUZZ_VERSION}
Requires:               darwinx-fribidi >= %{FRIBIDI_VERSION}
Requires:               darwinx-pango >= %{PANGO_VERSION}
Requires:               darwinx-atk >= %{ATK_VERSION}
Requires:               darwinx-jasper >= %{JASPER_VERSION}
Requires:               darwinx-libxml2 >= %{LIBXML2_VERSION}
Requires:               darwinx-libpsl >= %{LIBPSL_VERSION}
Requires:               darwinx-gdk-pixbuf >= %{GDK_PIXBUF_VERSION}
Requires:               darwinx-libcroco >= %{LIBCROCO_VERSION}
Requires:               darwinx-libepoxy >= %{LIBEPOXY_VERSION}
Requires:               darwinx-librsvg2 >= %{LIBRSVG2_VERSION}
Requires:               darwinx-gtk3 >= %{GTK3_VERSION}
Requires:               darwinx-adwaita-icon-theme >= %{GTK3_ADWAITA_VERSION}
Requires:               darwinx-libgdl >= %{GDL_VERSION}
Requires:		darwinx-gtk-mac-integration >= %{GTK_MAC_INTEGRATION_VERSION}

Requires:               darwinx-libgpg-error >= %{LIBGPG_ERROR_VERSION}
Requires:               darwinx-libgcrypt >= %{LIBGCRYPT_VERSION}
Requires:               darwinx-gmp >= %{GMP_VERSION}
Requires:               darwinx-nettle >= %{NETTLE_VERSION}
Requires:               darwinx-p11-kit >= %{P11_KIT_VERSION}
Requires:               darwinx-libtasn1 >= %{LIBTASN1_VERSION}
Requires:               darwinx-libunistring  >= %{LIBUNISTRING_VERSION}
Requires:               darwinx-gnutls  >= %{GNUTLS_VERSION}
#Requires:               darwinx-openssl  >= %{OPENSSL_VERSION}
Requires:               darwinx-glib-networking >= %{GLIB_NETWORKING_VERSION}

Requires:               darwinx-libxslt >= %{LIBXSLT_VERSION}
Requires:               darwinx-libsoup >= %{LIBSOUP_VERSION}

Requires:               darwinx-enchant >= %{ENCHANT_VERSION}

Requires:               darwinx-libogg >= %{LIBOGG_VERSION}
Requires:               darwinx-libvorbis >= %{LIBVORBIS_VERSION}
Requires:               darwinx-libwebp >= %{LIBWEBP_VERSION}
Requires:               darwinx-gstreamer1 >= %{GSTREAMER1_VERSION}
Requires:               darwinx-gstreamer1-plugins-base >= %{GSTREAMER1_PLUGINS_BASE_VERSION}
Requires:               darwinx-gstreamer1-plugins-good >= %{GSTREAMER1_PLUGINS_GOOD_VERSION}
#Requires:               darwinx-gstreamer1-plugins-bad >= %{GSTREAMER1_PLUGINS_BAD_VERSION}
Requires:               darwinx-webkitgtk3 >= %{WEBKITGTK3_VERSION}

Requires:               darwinx-dbus >= %{DBUS_VERSION}
Requires:               darwinx-dbus-glib >= %{DBUS_GLIB_VERSION}

#Requires:		darwinx-libusbx >= %{LIBUSB_VERSION}
#Requires:		darwinx-libexif >= %{LIBEXIF_VERSION}
#Requires:		darwinx-libgphoto2 >= %{LIBGPHOTO2_VERSION}
#Requires:		darwinx-sane-backends >= %{SANE_BACKENDS_VERSION}
#Requires:		darwinx-twaindsm >= %{TWAIN_DSM_VERSION} # Uses Twain.Framework on macOS

#Requires:               darwinx-Microsoft.CSharp >= %{MICROSOFT_CSHARP_VERSION}
Requires:               darwinx-Mono.Posix.NETStandard >= %{MONO_POSIX_NETSTANDARD_VERSION}
Requires:               darwinx-Mono.Data.Sqlite >= %{MONO_DATA_SQLITE_VERSION}
Requires:               darwinx-mono-core >= %{MONO_CORE_VERSION}
Requires:               darwinx-Npgsql >= %{NPGSQL_VERSION}
Requires:               darwinx-GtkSharp >= %{GTK3_SHARP_VERSION}
Requires:               darwinx-GdlSharp >= %{GDL_SHARP_VERSION}
Requires:		darwinx-gtk-mac-integration-sharp >= %{GTK_MAC_INTEGRATION_SHARP_VERSION}
Requires:               darwinx-Mono.Addins >= %{MONO_ADDINS_VERSION}
Requires:               darwinx-webkitgtk3-sharp >= %{WEBKITGTK3_SHARP_VERSION}
Requires:               darwinx-dbus-sharp >= %{DBUS_SHARP_VERSION}
Requires:               darwinx-dbus-sharp-glib >= %{DBUS_GLIB_SHARP_VERSION}
Requires:               darwinx-GstSharp >= %{GST_SHARP_VERSION}
Requires:               darwinx-Newtonsoft.Json >= %{NEWTONSOFT_JSON_VERSION}
Requires:               darwinx-BouncyCastle >= %{BOUNCY_CASTLE_VERSION}
Requires:               darwinx-MimeKit >= %{MIMEKIT_VERSION}
Requires:               darwinx-MailKit >= %{MAILKIT_VERSION}
Requires:               darwinx-ServiceStack >= %{SERVICE_STACK_VERSION}
Requires:		darwinx-RestSharp >= %{REST_SHARP_VERSION}
Requires:		darwinx-Seal.net >= %{SEALAPI_VERSION}
Requires:               darwinx-Sprache >= %{SPRACHE_VERSION}
Requires:               darwinx-PDFsharp-MigraDoc >= %{PDFSHARP_MIGRADOC_VERSION}
#Requires:		darwinx-SharpZipLib >= %{SHARP_ZIP_LIB_VERSION}
#Requires:		darwinx-libgphoto2-sharp >= %{LIBGPHOTO2_SHARP_VERSION}
#Requires:		darwinx-SharpCamera >= %{SHARP_CAMERA_VERSION}

%description sdk-darwinx
Easy management of applications for Mac OS X


%prep

#%setup -q

%build
#make all

%install
#if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
#DESTDIR=$RPM_BUILD_ROOT make install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/yum-plugins
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d

cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/yum-plugins

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
cp %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/
cp %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
cp %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
sed -i -e 's! -headerpad_max_install_names!!g' $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.darwinx

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/
cp %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT/usr/i686-w64-mingw32/sys-root/mingw/share/pkgconfig/
cp %{SOURCE14} $RPM_BUILD_ROOT/usr/i686-w64-mingw32/sys-root/mingw/share/pkgconfig/mono.pc

mkdir -p $RPM_BUILD_ROOT/usr/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig/
cp %{SOURCE14} $RPM_BUILD_ROOT/usr/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig/mono.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
#doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO LICENSE
#attr(0775,root,root) {_prefix}/bin/gsharpkit
#{_libdir}/mono/gsharpkit/GSharpKit.Config.dll
#{_libdir}/mono/gsharpkit/GSharpKit.Utils.dll
#{_libdir}/mono/gsharpkit/gsharpkit.exe
#{_libdir}/mono/gac
#{_datadir}/gsharpkit/ui/gsharpkit.xml
#{_datadir}/applications/gsharpkit.desktop
#{_datadir}/locale


%files release
%defattr(-, root, root)
%{_sysconfdir}/yum.repos.d/gsharpkit.repo
%{_sysconfdir}/yum.repos.d/mono-centos7.repo
%{_sysconfdir}/yum.repos.d/microsoft-prod.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-gsharpkit
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-xamarin
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-microsoft
%{_sysconfdir}/yum/pluginconf.d/yum_ignoreos.conf
%{_datadir}/yum-plugins/yum_ignoreos.py
#%{_datadir}/yum-plugins/yum_ignoreos.pyc
#%{_datadir}/yum-plugins/yum_ignoreos.pyo


%files runtime
%defattr(-, root, root)


%files sdk
%defattr(-, root, root)


%files sdk-mingw32
%defattr(-, root, root)


%files sdk-mingw64
%defattr(-, root, root)


%files sdk-mingw
%defattr(-, root, root)


%files sdk-mingw32-devel
%defattr(-, root, root)
/usr/i686-w64-mingw32/sys-root/mingw/share/pkgconfig/mono.pc

%files sdk-mingw64-devel
%defattr(-, root, root)
/usr/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig/mono.pc

%files sdk-mingw-devel
%defattr(-, root, root)


%files sdk-darwinx
%defattr(-, root, root)
%{_sysconfdir}/rpm/macros.darwinx
%{_bindir}/darwinx-cmake
%{_bindir}/darwinx-configure
%{_bindir}/darwinx-make
%{_bindir}/darwinx-pkg-config



###########################################################################
%changelog
* Thu Oct 03 2017 Mikkel Kruse Johnsen, GSharpKit <mikkel@gsharpkit.com>
- Renamed to GSharpKit
* Thu Jun 08 2010 Mikkel Kruse Johnsen, Appbox <mikkel@appbox.info>
- First rpm build.


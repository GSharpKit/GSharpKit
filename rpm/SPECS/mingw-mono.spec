%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name mono
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}
%define _binaries_in_noarch_packages_terminate_build 0

%define ver 4.8.0

Name:		mingw-mono
Version:	%{ver}.459
Release:	1%{?dist}
Summary:	The Mono CIL runtime, suitable for running .NET code
License:	LGPLv2
Group:		Development/Languages
URL:		http://www.mono-project.com/Main_Page
Source0:	http://download.mono-project.com/sources/mono/mono-%{version}.tar.bz2

Patch1: 	mono-2.0-monoservice.patch

Patch100:	mono-3.0-nodocs.patch
Patch102:	mingw-mono-2.8-config.patch
Patch103:	mono-3.6-genmdesc.patch
Patch104:	mono-4.6.2-keepalive.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	bison
BuildRequires:	glib2-devel
BuildRequires:	redhat-rpm-config
BuildRequires:	cmake

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

# We copy precompiled files from Linux
BuildRequires:	mono-core 		= %{version}
BuildRequires:  mono-extras 		= %{version}
BuildRequires:  mono-locale-extras 	= %{version}
BuildRequires:  mono-data 		= %{version}
BuildRequires:  mono-data-sqlite 	= %{version}
BuildRequires:  mono-winforms 		= %{version}
BuildRequires:  mono-web 		= %{version}
BuildRequires:  mono-wcf 		= %{version}
BuildRequires:  mono-winfx 		= %{version}
BuildRequires:  mono-devel 		= %{version}

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
Provides:	mingw32(msvcr120.dll)

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

%description -n mingw64-%{mingw_pkg_name}
This package contains the core of the Mono runtime including its
Virtual Machine, Just-in-time compiler, C# compiler, security
tools and libraries (corlib, XML, System.Security, ZipLib,


%prep
%setup -q -n mono-%{ver}
%patch1 -p1 -b .monoservice

%patch100 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

# Remove hardcoded lib directory for libMonoPosixHelper.so from the config
sed -i 's|$mono_libdir/||g' data/config.in

echo "const char *build_date = \"`date`\";" > mono/mini/buildver-sgen.h

%build
#autoreconf -i --force

export MINGW32_CFLAGS="%{mingw32_cflags} -DGC_NOT_DLL"
export MINGW64_CFLAGS="%{mingw64_cflags} -DGC_NOT_DLL"
export lt_cv_deplibs_check_method="pass_all"

%mingw_configure "--with-sigaltstack=no" "--with-tls=pthread" "--disable-static" "--disable-parallel-mark" "--with-sgen=yes" "--disable-boehm"

%mingw_make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT" program_transform_name=""

# Mingw32
rm -f %{buildroot}%{mingw32_bindir}/mono
cp %{buildroot}%{mingw32_bindir}/mono-sgen.exe %{buildroot}%{mingw32_bindir}/mono.exe
sed -s -i 's!-mno-cygwin!!g' %{buildroot}%{mingw32_libdir}/pkgconfig/mono-2.pc
sed -s -i 's!%{mingw32_bindir}/mono!mono!g' %{buildroot}%{mingw32_bindir}/mcs

# Mingw64
rm -f %{buildroot}%{mingw64_bindir}/mono
cp %{buildroot}%{mingw64_bindir}/mono-sgen.exe %{buildroot}%{mingw64_bindir}/mono.exe
sed -s -i 's!-mno-cygwin!!g' %{buildroot}%{mingw64_libdir}/pkgconfig/mono-2.pc
sed -s -i 's!%{mingw64_bindir}/mono!mono!g' %{buildroot}%{mingw64_bindir}/mcs


# Mingw32

install -d -m 755 %{buildroot}%{mingw32_libdir}/mono/gac

cp -rf -L /usr/lib/mono/4.0 %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L /usr/lib/mono/4.0-api %{buildroot}%{mingw32_libdir}/mono/

cp -rf -L /usr/lib/mono/4.5 %{buildroot}%{mingw32_libdir}/mono/
cp -rf -L /usr/lib/mono/4.5-api %{buildroot}%{mingw32_libdir}/mono/

# Mingw64

install -d -m 755 %{buildroot}%{mingw64_libdir}/mono/gac

cp -rf -L /usr/lib/mono/4.0 %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L /usr/lib/mono/4.0-api %{buildroot}%{mingw64_libdir}/mono/

cp -rf -L /usr/lib/mono/4.5 %{buildroot}%{mingw64_libdir}/mono/
cp -rf -L /usr/lib/mono/4.5-api %{buildroot}%{mingw64_libdir}/mono/


# mono-core
cp -rf /usr/lib/mono/gac/Commons.Xml.Relaxng %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/cscompmgd %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/CustomMarshalers %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.West %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/ICSharpCode.SharpZipLib %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.CSharp %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.VisualC %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Btls.Interface %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Cairo %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Cecil %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CompilerServices.SymbolWriter %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CSharp %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Management %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Parallel %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Posix %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Security %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Simd %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Tasklets %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Configuration %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Core %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Drawing %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Dynamic %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IO.Compression %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IO.Compression.FileSystem %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Json %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Json.Microsoft %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http.Formatting %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http.WebRequest %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Numerics %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Numerics.Vectors %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Reflection.Context %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.InteropServices.RuntimeInformation %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Security %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Threading.Tasks.Dataflow %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml.Linq %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml.Serialization %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Commons.Xml.Relaxng %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/cscompmgd %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/CustomMarshalers %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.West %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/ICSharpCode.SharpZipLib %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.CSharp %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.VisualC %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Btls.Interface %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Cairo %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Cecil %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CompilerServices.SymbolWriter %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CSharp %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Management %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Parallel %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Posix %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Security %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Simd %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Tasklets %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Configuration %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Core %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Drawing %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Dynamic %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IO.Compression %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IO.Compression.FileSystem %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Json %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Json.Microsoft %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http.Formatting %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Net.Http.WebRequest %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Numerics %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Numerics.Vectors %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Reflection.Context %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.InteropServices.RuntimeInformation %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Security %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Threading.Tasks.Dataflow %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml.Linq %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xml.Serialization %{buildroot}%{mingw64_libdir}/mono/gac/

# mono-extras
cp -rf /usr/lib/mono/gac/Mono.Messaging %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Messaging.RabbitMQ %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/mono-service %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/RabbitMQ.Client %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Configuration.Install %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Management %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Messaging %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Caching %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceProcess %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xaml %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Mono.Messaging %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Messaging.RabbitMQ %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/mono-service %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/RabbitMQ.Client %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Configuration.Install %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Management %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Messaging %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Caching %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceProcess %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Xaml %{buildroot}%{mingw64_libdir}/mono/gac/

# mono-locale-extras
cp -rf /usr/lib/mono/gac/I18N.CJK %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.MidEast %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.Other %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.Rare %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/I18N.CJK %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.MidEast %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.Other %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/I18N.Rare %{buildroot}%{mingw64_libdir}/mono/gac/


# mono-data
cp -rf /usr/lib/mono/gac/Mono.Data.Tds %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Novell.Directory.Ldap %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.DataSetExtensions %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.Entity %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.Linq %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.DirectoryServices %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.DirectoryServices.Protocols %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.EnterpriseServices %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Serialization %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Transactions %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/WebMatrix.Data %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Mono.Data.Tds %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Novell.Directory.Ldap %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.DataSetExtensions %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.Entity %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Data.Linq %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.DirectoryServices %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.DirectoryServices.Protocols %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.EnterpriseServices %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Serialization %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Transactions %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/WebMatrix.Data %{buildroot}%{mingw64_libdir}/mono/gac/

# mono-data-sqlite
cp -rf /usr/lib/mono/gac/Mono.Data.Sqlite %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Mono.Data.Sqlite %{buildroot}%{mingw64_libdir}/mono/gac/

# mono-winforms
cp -rf /usr/lib/mono/gac/Accessibility %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.WebBrowser %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Design %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Drawing.Design %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows.Forms %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows.Forms.DataVisualization %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Accessibility %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.WebBrowser %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Design %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Drawing.Design %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows.Forms %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Windows.Forms.DataVisualization %{buildroot}%{mingw64_libdir}/mono/gac/


# mono-web
cp -rf /usr/lib/mono/gac/Microsoft.Web.Infrastructure %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Http %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ComponentModel.Composition %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ComponentModel.DataAnnotations %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Remoting %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Serialization.Formatters.Soap %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Abstractions %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.ApplicationServices %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.DynamicData %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http.SelfHost %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http.WebHost %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Mobile %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Razor %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Routing %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Services %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages.Deployment %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages.Razor %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Microsoft.Web.Infrastructure %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Http %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ComponentModel.Composition %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ComponentModel.DataAnnotations %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Remoting %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.Serialization.Formatters.Soap %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Abstractions %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.ApplicationServices %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.DynamicData %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http.SelfHost %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Http.WebHost %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Mobile %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Razor %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Routing %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Services %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages.Deployment %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.WebPages.Razor %{buildroot}%{mingw64_libdir}/mono/gac/

# mono-wcf
cp -rf /usr/lib/mono/gac/System.Data.Services %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IdentityModel %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IdentityModel.Selectors %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.DurableInstancing %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Activation %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Discovery %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Internals %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Routing %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Web %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.Activities %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.ComponentModel %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.Runtime %{buildroot}%{mingw32_libdir}/mono/gac/


cp -rf /usr/lib/mono/gac/System.Data.Services %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IdentityModel %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.IdentityModel.Selectors %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Runtime.DurableInstancing %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Activation %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Discovery %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Internals %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Routing %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.ServiceModel.Web %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.Activities %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.ComponentModel %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Workflow.Runtime %{buildroot}%{mingw64_libdir}/mono/gac/


# mono-devel
cp -rf /usr/lib/mono/gac/Microsoft.Build %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Engine %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Framework %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.Core %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.v12.0 %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.v4.0 %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.Core %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.v12.0 %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.v4.0 %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CodeContracts %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Debugger.Soft %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.XBuild.Tasks %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/PEAPI %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/SMDiagnostics %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Deployment %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/Microsoft.Build %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Engine %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Framework %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.Core %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.v12.0 %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Tasks.v4.0 %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.Core %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.v12.0 %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Microsoft.Build.Utilities.v4.0 %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.CodeContracts %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.Debugger.Soft %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/Mono.XBuild.Tasks %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/PEAPI %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/SMDiagnostics %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Deployment %{buildroot}%{mingw64_libdir}/mono/gac/


# mono-mvc
cp -rf /usr/lib/mono/gac/System.Web.DynamicData %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Extensions %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Extensions.Design %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Mvc %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/System.Web.DynamicData %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Extensions %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Extensions.Design %{buildroot}%{mingw64_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/System.Web.Mvc %{buildroot}%{mingw64_libdir}/mono/gac/


# mono-winfxcore
cp -rf /usr/lib/mono/gac/System.Data.Services.Client %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/WindowsBase %{buildroot}%{mingw32_libdir}/mono/gac/

cp -rf /usr/lib/mono/gac/System.Data.Services.Client %{buildroot}%{mingw32_libdir}/mono/gac/
cp -rf /usr/lib/mono/gac/WindowsBase %{buildroot}%{mingw64_libdir}/mono/gac/

%clean
#rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_sysconfdir}
%{mingw32_bindir}
%{mingw32_libdir}
%{mingw32_datadir}
%{mingw32_includedir}


%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_sysconfdir}
%{mingw64_bindir}
%{mingw64_libdir}
%{mingw64_datadir}
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


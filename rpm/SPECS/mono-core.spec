#
# spec file for package mono-core
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Xamarin, Inc.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugzilla.xamarin.com/
#


%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define ext_man .gz
%else
%{!?ext_man: %define ext_man .gz}
%endif
%define llvm no
%global debug_package %{nil} 
%define sgen yes

%define ver 5.14.0.177

Name:           mono-core
Version:        %{ver}
Release:        1%{?dist}
Summary:        Cross-platform, Open Source, .NET development framework
License:        LGPL-2.1 and MIT and MS-PL
Group:          Development/Languages/Mono
Url:            http://www.mono-project.com
Source0:        http://download.mono-project.com/sources/mono/mono-%{version}.tar.bz2
Patch0:		mono-4.6.2-keepalive.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  which
BuildRequires:  gettext
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libgdiplus-devel
BuildRequires:  libtool
BuildRequires:  cmake
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
BuildRequires:  pkgconfig
BuildRequires:  libX11-devel
%else
BuildRequires:  pkg-config
BuildRequires:  xorg-x11-libX11-devel
%endif
BuildRequires:  zlib-devel
%ifnarch ia64 %arm aarch64 s390
BuildRequires:  valgrind-devel
%endif
%if %llvm == yes
BuildRequires:  llvm-mono-devel
%endif
Provides:       mono = %{version}
Provides:       mono-cairo = %{version}
Provides:       mono-drawing = %{version}
Provides:       mono-ikvm = %{version}
Provides:       mono-posix = %{version}
Provides:       mono-xml-relaxng = %{version}
Provides:       mono-ziplib = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %llvm == yes
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
Requires:       libmono-llvm0 = %{version}
%else
Recommends:     libmono-llvm0 = %{version}
%endif
%endif
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
Requires:       libgdiplus
%else
Recommends:     libgdiplus
%endif
Provides:       mono(Commons.Xml.Relaxng) = 1.0.5000.0
Provides:       mono(CustomMarshalers) = 1.0.5000.0
Provides:       mono(I18N) = 1.0.5000.0
Provides:       mono(I18N.West) = 1.0.5000.0
Provides:       mono(ICSharpCode.SharpZipLib) = 0.6.0.0
Provides:       mono(ICSharpCode.SharpZipLib) = 0.84.0.0
Provides:       mono(Mono.Cairo) = 1.0.5000.0
Provides:       mono(Mono.Cairo) = 2.0.0.0
Provides:       mono(Mono.CompilerServices.SymbolWriter) = 1.0.5000.0
Provides:       mono(Mono.Posix) = 1.0.5000.0
Provides:       mono(Mono.Security) = 1.0.5000.0
Provides:       mono(Mono.Security) = 2.0.0.0
Provides:       mono(System) = 1.0.5000.0
Provides:       mono(System) = 2.0.0.0
Provides:       mono(System.Configuration) = 2.0.0.0
Provides:       mono(System.Security) = 1.0.5000.0
Provides:       mono(System.Security) = 2.0.0.0
Provides:       mono(System.Xml) = 1.0.5000.0
Provides:       mono(System.Xml) = 2.0.0.0
Provides:       mono(mscorlib) = 1.0.5000.0
Provides:       mono(mscorlib) = 2.0.0.0
Provides:       mono(Microsoft.Build.Framework) = 14.1.0.0
Provides:       mono(Microsoft.Build.Tasks.Core) = 14.1.0.0
Provides:       mono(Microsoft.Build.Utilities.Core) = 14.1.0.0
Provides:	mono(Microsoft.CodeAnalysis.Features) = 42.42.42.42
Provides:	mono(System.Collections.Immutable) = 1.2.0.0
Provides:       mono(System.IO.Compression) = 4.1.0.0
Provides:	mono(System.IO.Compression) = 4.1.1.0
Provides:	mono(System.Net.Http) = 4.1.0.0
Provides:	mono(System.Reflection.Metadata) = 1.3.0.0
Provides:	mono(System.Security.Cryptography.Algorithms) = 4.0.0.0
Provides:	mono(System.Text.Encoding.CodePages) = 4.0.2.0
Provides:	mono(System.Threading.Tasks.Extensions) = 4.1.0.0
Provides:	mono(System.Xml.ReaderWriter) = 4.1.0.0
Provides:	mono(System.ValueTuple) = 4.0.1.0
Provides:	mono(System.Xml.XPath.XDocument) = 4.0.1.0
Provides:	mono(System.Runtime.Loader) = 4.0.0.0
Provides:	mono(System.Diagnostics.Process) = 4.0.0.0
Provides:	mono(System.Security.AccessControl) = 4.0.0.0
Provides:	mono(System.Security.Principal.Windows) = 4.0.0.0
Provides:       mono(System.Diagnostics.StackTrace) = 4.0.2.0
Provides:	mono(System.IO.Pipes.AccessControl) = 4.0.1.0

%description
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

%prep
%setup -q -n mono-%{ver}
%patch0 -p1

# Remove hardcoded lib directory for libMonoPosixHelper.so from the config
sed -i 's|$mono_libdir/||g' data/config.in

%build
./autogen.sh
# These are only needed if there are patches to the runtime
#rm -f libgc/libtool.m4
#autoreconf --force --install
#autoreconf --force --install libgc
export CFLAGS=" %{optflags} -fno-strict-aliasing"
%ifarch armv7l armv7hl
export MONO_CPU_ARCH="armv7l-thumb"
%endif
%ifarch armv5el
export MONO_CPU_ARCH="armv5el"
%endif
# distro specific configure options
%if %llvm == yes
export PATH=/opt/novell/llvm-mono/bin:$PATH
%endif
%configure \
  --with-sgen=%{sgen} \
%if %llvm == yes
  --enable-loadedllvm \
  --disable-system-aot \
%endif
%ifarch ppc
 --with-sigaltstack=no \
%endif
%ifnarch %ix86 x86_64
  --disable-system-aot \
%endif
  --with-ikvm=yes \
  --with-moonlight=no

make %{?_smp_mflags}

%install
%make_install

# Remove hardcoded lib directory from the config
sed -i s,%{_prefix}/lib/,,g %{buildroot}%{_sysconfdir}/mono/config

# remove .la files (they are generally bad news)
rm -f %{buildroot}%{_libdir}/*.la

# remove Windows-only stuff
rm -rf %{buildroot}%{_prefix}/lib/mono/*/Mono.Security.Win32*
rm -f %{buildroot}%{_libdir}/libMonoSupportW.*

# remove .a files for libraries that are really only for us
rm -f %{buildroot}%{_libdir}/libMonoPosixHelper.a
rm -f %{buildroot}%{_libdir}/libikvm-native.a
rm -f %{buildroot}%{_libdir}/libmono-llvm.a
rm -f %{buildroot}%{_libdir}/libmono-2.0.a
rm -f %{buildroot}%{_libdir}/libmonoboehm-2.0.a
rm -f %{buildroot}%{_libdir}/libmonosgen-2.0.a

# remove libgc cruft
rm -rf %{buildroot}%{_datadir}/libgc-mono

# remove stuff that we don't package
rm -f %{buildroot}%{_bindir}/cilc
rm -f %{buildroot}%{_mandir}/man1/cilc.1*
rm -f %{buildroot}%{_prefix}/lib/mono/*/browsercaps-updater.*
rm -f %{buildroot}%{_prefix}/lib/mono/*/culevel.*

# brp-compress doesn't search _mandir
# so we cheat it
ln -s . %{buildroot}%{_prefix}/symlink-for-brp-compress
RPM_BUILD_ROOT=%{buildroot}%{_prefix} /usr/lib/rpm/brp-compress
rm %{buildroot}%{_prefix}/symlink-for-brp-compress

# Fix non-executable-in-bin
chmod +x %{buildroot}%{_bindir}/mono-gdb.py
chmod +x %{buildroot}%{_bindir}/mono-sgen-gdb.py

# ERROR: link target doesn't exist (neither in build root nor in installed system):
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Microsoft.Build.dll
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Microsoft.Build.Engine.dll
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Mono.XBuild.Tasks.dll
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Microsoft.Build.Framework.dll
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Microsoft.Build.Tasks.v12.0.dll
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild/12.0/bin/Microsoft.Build.Utilities.v12.0.dll

rm -f %{buildroot}%{_prefix}/lib/mono/xbuild/15.0/Microsoft.Common.targets/ImportAfter/Microsoft.NuGet.ImportAfter.targets

# Part of the referenceassemblies
rm -rf %{buildroot}%{_prefix}/lib/mono/xbuild-frameworks/.NETPortable

%fdupes %{buildroot}%{_prefix}

%find_lang mcs

%if %sgen == no
# installed anyway but not packaged
rm %{buildroot}%{_bindir}/mono-sgen-gdb.py
%endif

%files -f mcs.lang
%defattr(-, root, root)
%doc COPYING.LIB LICENSE
%config %{_sysconfdir}/mono/2.0/machine.config
%config %{_sysconfdir}/mono/2.0/settings.map
%config %{_sysconfdir}/mono/4.0/machine.config
%config %{_sysconfdir}/mono/4.0/settings.map
%config %{_sysconfdir}/mono/4.5/machine.config
%config %{_sysconfdir}/mono/4.5/settings.map
%config %{_sysconfdir}/mono/config
%dir %{_prefix}/lib/mono
%dir %{_prefix}/lib/mono/4.5
%dir %{_prefix}/lib/mono/4.5/Facades
%dir %{_prefix}/lib/mono/gac
%dir %{_sysconfdir}/mono
%dir %{_sysconfdir}/mono/2.0
%dir %{_sysconfdir}/mono/4.0
%dir %{_sysconfdir}/mono/4.5
%{_bindir}/al
%{_bindir}/al2
%{_bindir}/cert-sync
%{_bindir}/certmgr
%{_bindir}/chktrust
%{_bindir}/crlupdate
%{_bindir}/csc
%{_bindir}/csc-dim
%{_bindir}/csi
%{_bindir}/csharp
%{_bindir}/dmcs
%{_bindir}/gacutil
%{_bindir}/gacutil2
%{_bindir}/ikdasm
%{_bindir}/illinkanalyzer
%{_bindir}/mcs
%{_bindir}/vbc
%{_bindir}/mono
%{_bindir}/mono-boehm
%{_bindir}/mono-configuration-crypto
%if %sgen == yes
%{_bindir}/mono-sgen
%endif
%{_bindir}/mono-test-install
%{_bindir}/mozroots
%{_bindir}/peverify
%{_bindir}/setreg
%{_bindir}/sn
%{_bindir}/mono-symbolicate
%{_bindir}/mono-package-runtime
%{_bindir}/monograph
%{_bindir}/sgen-grep-binprot
%{_libdir}/libMonoPosixHelper.so*
%{_libdir}/libikvm-native.so
%{_libdir}/libmono-btls-shared.so
%{_mandir}/man1/certmgr.1%ext_man
%{_mandir}/man1/chktrust.1%ext_man
%{_mandir}/man1/crlupdate.1%ext_man
%{_mandir}/man1/csharp.1%ext_man
%{_mandir}/man1/gacutil.1%ext_man
%{_mandir}/man1/illinkanalyzer.1%ext_man
%{_mandir}/man1/mcs.1%ext_man
%{_mandir}/man1/mono-configuration-crypto.1%ext_man
%{_mandir}/man1/mono.1%ext_man
%{_mandir}/man1/mozroots.1%ext_man
%{_mandir}/man1/setreg.1%ext_man
%{_mandir}/man1/sn.1%ext_man
%{_mandir}/man1/mono-symbolicate.1%ext_man
%{_mandir}/man5/mono-config.5%ext_man
%{_mandir}/man1/cert-sync.1%ext_man
%{_prefix}/lib/mono/4.5/System.IO.Compression.FileSystem.dll
%{_prefix}/lib/mono/4.5/System.IO.Compression.dll
%{_prefix}/lib/mono/4.5/al.*
%{_prefix}/lib/mono/4.5/cert-sync.*
%{_prefix}/lib/mono/4.5/certmgr.*
%{_prefix}/lib/mono/4.5/chktrust.*
%{_prefix}/lib/mono/4.5/crlupdate.*
%{_prefix}/lib/mono/4.5/csharp.*
%{_prefix}/lib/mono/4.5/gacutil.*
%{_prefix}/lib/mono/4.5/ikdasm.*
%{_prefix}/lib/mono/4.5/illinkanalyzer.*
%{_prefix}/lib/mono/4.5/mcs.*
%{_prefix}/lib/mono/4.5/vbc.*
%{_prefix}/lib/mono/4.5/csc.*
%{_prefix}/lib/mono/4.5/mozroots.*
%{_prefix}/lib/mono/4.5/setreg.*
%{_prefix}/lib/mono/4.5/sn.*
%{_prefix}/lib/mono/4.5/Commons.Xml.Relaxng.dll
%{_prefix}/lib/mono/4.5/CustomMarshalers.dll
%{_prefix}/lib/mono/4.5/I18N.West.dll
%{_prefix}/lib/mono/4.5/I18N.dll
%{_prefix}/lib/mono/4.5/ICSharpCode.SharpZipLib.dll
%{_prefix}/lib/mono/4.5/Microsoft.CodeAnalysis.dll*
%{_prefix}/lib/mono/4.5/Microsoft.CodeAnalysis.CSharp.dll*
%{_prefix}/lib/mono/4.5/Microsoft.CodeAnalysis.CSharp.Scripting.dll*
%{_prefix}/lib/mono/4.5/Microsoft.CodeAnalysis.Scripting.dll*
%{_prefix}/lib/mono/4.5/Microsoft.CodeAnalysis.VisualBasic.dll*
%{_prefix}/lib/mono/4.5/Microsoft.CSharp.dll
%{_prefix}/lib/mono/4.5/Microsoft.VisualC.dll
%{_prefix}/lib/mono/4.5/VBCSCompiler.exe*
%{_prefix}/lib/mono/4.5/Mono.Btls.Interface.dll
%{_prefix}/lib/mono/4.5/Mono.CSharp.dll
%{_prefix}/lib/mono/4.5/Mono.Cairo.dll
%{_prefix}/lib/mono/4.5/Mono.CompilerServices.SymbolWriter.dll
%{_prefix}/lib/mono/4.5/Mono.Management.dll
%{_prefix}/lib/mono/4.5/Mono.Parallel.dll
%{_prefix}/lib/mono/4.5/Mono.Posix.dll
%{_prefix}/lib/mono/4.5/Mono.Security.dll
%{_prefix}/lib/mono/4.5/Mono.Simd.dll
%{_prefix}/lib/mono/4.5/Mono.Tasklets.dll
%{_prefix}/lib/mono/4.5/Mono.Profiler.Log.dll
%{_prefix}/lib/mono/4.5/System.Collections.Immutable.dll*
%{_prefix}/lib/mono/4.5/System.Configuration.dll
%{_prefix}/lib/mono/4.5/System.Core.dll
%{_prefix}/lib/mono/4.5/System.Drawing.dll
%{_prefix}/lib/mono/4.5/System.Dynamic.dll
%{_prefix}/lib/mono/4.5/System.Json.dll
%{_prefix}/lib/mono/4.5/System.Json.Microsoft.dll
%{_prefix}/lib/mono/4.5/System.Net.dll
%{_prefix}/lib/mono/4.5/System.Net.Http.dll
%{_prefix}/lib/mono/4.5/System.Net.Http.Formatting.dll
%{_prefix}/lib/mono/4.5/System.Net.Http.WebRequest.dll
%{_prefix}/lib/mono/4.5/System.Numerics.dll
%{_prefix}/lib/mono/4.5/System.Numerics.Vectors.dll
%{_prefix}/lib/mono/4.5/System.Reflection.Context.dll
%{_prefix}/lib/mono/4.5/System.Reflection.Metadata.dll*
%{_prefix}/lib/mono/4.5/System.Security.dll
%{_prefix}/lib/mono/4.5/System.Threading.Tasks.Dataflow.dll
%{_prefix}/lib/mono/4.5/System.Windows.dll
%{_prefix}/lib/mono/4.5/System.Xml.Serialization.dll
%{_prefix}/lib/mono/4.5/System.Xml.Linq.dll
%{_prefix}/lib/mono/4.5/System.Xml.dll
%{_prefix}/lib/mono/4.5/System.dll
%{_prefix}/lib/mono/4.5/cscompmgd.dll
%{_prefix}/lib/mono/4.5/mscorlib.*
%{_prefix}/lib/mono/4.5/Facades/System*
%{_prefix}/lib/mono/4.5/Facades/Microsoft*
%{_prefix}/lib/mono/4.5/Facades/netstandard.dll
%{_prefix}/lib/mono/4.5/dim/*
%{_prefix}/lib/mono/gac/Commons.Xml.Relaxng
%{_prefix}/lib/mono/gac/CustomMarshalers
%{_prefix}/lib/mono/gac/I18N
%{_prefix}/lib/mono/gac/I18N.West
%{_prefix}/lib/mono/gac/ICSharpCode.SharpZipLib
%{_prefix}/lib/mono/gac/Microsoft.CSharp
%{_prefix}/lib/mono/gac/Microsoft.VisualC
%{_prefix}/lib/mono/gac/Mono.Btls.Interface
%{_prefix}/lib/mono/gac/Mono.CSharp
%{_prefix}/lib/mono/gac/Mono.Cairo
%{_prefix}/lib/mono/gac/Mono.Cecil
%{_prefix}/lib/mono/gac/Mono.CompilerServices.SymbolWriter
%{_prefix}/lib/mono/gac/Mono.Management
%{_prefix}/lib/mono/gac/Mono.Parallel
%{_prefix}/lib/mono/gac/Mono.Posix
%{_prefix}/lib/mono/gac/Mono.Security
%{_prefix}/lib/mono/gac/Mono.Simd
%{_prefix}/lib/mono/gac/Mono.Tasklets
%{_prefix}/lib/mono/gac/Mono.Profiler.Log
%{_prefix}/lib/mono/gac/System
%{_prefix}/lib/mono/gac/System.Configuration
%{_prefix}/lib/mono/gac/System.Core
%{_prefix}/lib/mono/gac/System.Drawing
%{_prefix}/lib/mono/gac/System.Dynamic
%{_prefix}/lib/mono/gac/System.Net
%{_prefix}/lib/mono/gac/System.Net.Http
%{_prefix}/lib/mono/gac/System.Net.Http.Formatting
%{_prefix}/lib/mono/gac/System.Net.Http.WebRequest
%{_prefix}/lib/mono/gac/System.Numerics
%{_prefix}/lib/mono/gac/System.Numerics.Vectors
%{_prefix}/lib/mono/gac/System.Reflection.Context
%{_prefix}/lib/mono/gac/System.Security
%{_prefix}/lib/mono/gac/System.Threading.Tasks.Dataflow
%{_prefix}/lib/mono/gac/System.Windows
%{_prefix}/lib/mono/gac/System.Xml.Serialization
%{_prefix}/lib/mono/gac/System.Xml
%{_prefix}/lib/mono/gac/System.Xml.Linq
%{_prefix}/lib/mono/gac/System.Json
%{_prefix}/lib/mono/gac/System.Json.Microsoft
%{_prefix}/lib/mono/gac/System.IO.Compression.FileSystem
%{_prefix}/lib/mono/gac/System.IO.Compression
%{_prefix}/lib/mono/gac/cscompmgd
%{_prefix}/lib/mono/mono-configuration-crypto


%post 
cert-sync /etc/pki/tls/certs/ca-bundle.crt

%package -n libmono-2_0-1
Summary:        A Library for embedding Mono in your Application
License:        LGPL-2.1
Requires:	libmonoboehm-2_0-1
Group:          Development/Libraries/C and C++

%description -n libmono-2_0-1
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

A Library for embedding Mono in your Application.

%files -n libmono-2_0-1
%defattr(-, root, root)
%{_libdir}/libmono-2.0.so.1*

%post -n libmono-2_0-1 -p /sbin/ldconfig

%postun -n libmono-2_0-1 -p /sbin/ldconfig

%package -n libmono-2_0-devel
Summary:        Development files for libmono
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       libmono-2_0-1 = %{version}
Requires:       libmonoboehm-2_0-devel
Requires:       mono-core = %{version}

%description -n libmono-2_0-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Development files for libmono.

%files -n libmono-2_0-devel
%defattr(-, root, root)
%{_bindir}/mono-gdb.py
%{_includedir}/mono-2.0
%{_libdir}/libmono-2.0.so
%{_libdir}/pkgconfig/mono-2.pc

%package -n libmonoboehm-2_0-1
Summary:        A Library for embedding Mono in your Application (Boehm GC)
License:        LGPL-2.1
Group:          Development/Libraries/C and C++

%description -n libmonoboehm-2_0-1
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

A Library for embedding Mono in your application using the conservative
Boehm garbage collector.

%files -n libmonoboehm-2_0-1
%defattr(-, root, root)
%{_libdir}/libmonoboehm-2.0.so.*

%post -n libmonoboehm-2_0-1 -p /sbin/ldconfig

%postun -n libmonoboehm-2_0-1 -p /sbin/ldconfig

%package -n libmonoboehm-2_0-devel
Summary:        Development files for libmonoboehm
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       libmono-2_0-devel
Requires:       libmonoboehm-2_0-1 = %{version}
Requires:       mono-core = %{version}

%description -n libmonoboehm-2_0-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Development files for libmonoboehm

%files -n libmonoboehm-2_0-devel
%defattr(-, root, root)
%{_libdir}/libmonoboehm-2.0.so

%if %sgen == yes
%package -n libmonosgen-2_0-1
Summary:        A Library for embedding Mono in your Application (SGen GC)
License:        LGPL-2.1
Group:          Development/Libraries/C and C++

%description -n libmonosgen-2_0-1
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

A Library for embedding Mono in your application using the precise SGen
garbage collector.

%files -n libmonosgen-2_0-1
%defattr(-, root, root)
%{_libdir}/libmonosgen-2.0.so.*

%post -n libmonosgen-2_0-1 -p /sbin/ldconfig

%postun -n libmonosgen-2_0-1 -p /sbin/ldconfig

%package -n libmonosgen-2_0-devel
Summary:        Development files for libmonosgen
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       libmono-2_0-devel
Requires:       libmonosgen-2_0-1 = %{version}
Requires:       mono-core = %{version}

%description -n libmonosgen-2_0-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Development files for libmonosgen.

%files -n libmonosgen-2_0-devel
%defattr(-, root, root)
%{_bindir}/mono-sgen-gdb.py
%{_libdir}/libmonosgen-2.0.so
%{_libdir}/pkgconfig/monosgen-2.pc
%endif

%if %llvm == yes
%package -n libmono-llvm0
Summary:        Loadable LLVM libary for mono
License:        LGPL-2.1
Group:          Development/Libraries/C and C++

%description -n libmono-llvm0
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Loadable LLVM libary for mono.

%files -n libmono-llvm0
%defattr(-, root, root)
%{_libdir}/libmono-llvm.so*

%post -n libmono-llvm0 -p /sbin/ldconfig

%postun -n libmono-llvm0 -p /sbin/ldconfig
%endif

%package -n mono-locale-extras
Summary:        Extra locale information
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:       mono(I18N.CJK) = 1.0.5000.0
Provides:       mono(I18N.MidEast) = 1.0.5000.0
Provides:       mono(I18N.Other) = 1.0.5000.0
Provides:       mono(I18N.Rare) = 1.0.5000.0

%description -n mono-locale-extras
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Extra locale information.

%files -n mono-locale-extras
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/I18N.CJK.dll
%{_prefix}/lib/mono/4.5/I18N.MidEast.dll
%{_prefix}/lib/mono/4.5/I18N.Other.dll
%{_prefix}/lib/mono/4.5/I18N.Rare.dll
%{_prefix}/lib/mono/gac/I18N.CJK
%{_prefix}/lib/mono/gac/I18N.MidEast
%{_prefix}/lib/mono/gac/I18N.Other
%{_prefix}/lib/mono/gac/I18N.Rare

%package -n mono-data
Summary:        Database connectivity for Mono
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:       mono-directory = %{version}
Provides:       mono-ms-enterprise = %{version}
Provides:       mono-novell-directory = %{version}
Provides:       mono(Mono.Data.Tds) = 1.0.5000.0
Provides:       mono(Novell.Directory.Ldap) = 1.0.5000.0
Provides:       mono(System.Data) = 1.0.5000.0
Provides:       mono(System.Data) = 2.0.0.0
Provides:       mono(System.DirectoryServices) = 1.0.5000.0
Provides:       mono(System.EnterpriseServices) = 1.0.5000.0

%description -n mono-data
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Database connectivity for Mono.

%files -n mono-data
%defattr(-, root, root)
%{_bindir}/sqlmetal
%{_bindir}/sqlsharp
%{_mandir}/man1/sqlsharp.1%ext_man
%{_prefix}/lib/mono/4.5/Mono.Data.Tds.dll
%{_prefix}/lib/mono/4.5/Novell.Directory.Ldap.dll
%{_prefix}/lib/mono/4.5/System.Data.DataSetExtensions.dll
%{_prefix}/lib/mono/4.5/System.Data.Linq.dll
%{_prefix}/lib/mono/4.5/System.Data.dll
%{_prefix}/lib/mono/4.5/System.Data.Entity.dll
%{_prefix}/lib/mono/4.5/System.DirectoryServices.dll
%{_prefix}/lib/mono/4.5/System.DirectoryServices.Protocols.dll
%{_prefix}/lib/mono/4.5/System.EnterpriseServices.dll
%{_prefix}/lib/mono/4.5/System.Runtime.Serialization.dll
%{_prefix}/lib/mono/4.5/System.Transactions.dll
%{_prefix}/lib/mono/4.5/WebMatrix.Data.dll
%{_prefix}/lib/mono/4.5/sqlmetal.*
%{_prefix}/lib/mono/4.5/sqlsharp.*
%{_prefix}/lib/mono/gac/Mono.Data.Tds
%{_prefix}/lib/mono/gac/Novell.Directory.Ldap
%{_prefix}/lib/mono/gac/System.Data
%{_prefix}/lib/mono/gac/System.Data.Entity
%{_prefix}/lib/mono/gac/System.Data.DataSetExtensions
%{_prefix}/lib/mono/gac/System.Data.Linq
%{_prefix}/lib/mono/gac/System.DirectoryServices
%{_prefix}/lib/mono/gac/System.DirectoryServices.Protocols
%{_prefix}/lib/mono/gac/System.EnterpriseServices
%{_prefix}/lib/mono/gac/System.Runtime.Serialization
%{_prefix}/lib/mono/gac/System.Transactions
%{_prefix}/lib/mono/gac/WebMatrix.Data

%package -n mono-winforms
Summary:        Mono's Windows Forms implementation
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:       mono-window-forms = %{version}
Provides:       mono(Accessibility) = 1.0.5000.0
Provides:       mono(System.Design) = 1.0.5000.0
Provides:       mono(System.Drawing) = 1.0.5000.0
Provides:       mono(System.Drawing) = 2.0.0.0
Provides:       mono(System.Drawing.Design) = 1.0.5000.0
Provides:       mono(System.Windows.Forms) = 1.0.5000.0
Provides:       mono(System.Windows.Forms) = 2.0.0.0
Provides:       mono(System.Runtime.WindowsRuntime) = 4.0.0.0
Provides:       mono(Windows) = 255.255.255.255


%description -n mono-winforms
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono's Windows Forms implementation.

%files -n mono-winforms
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/Accessibility.dll
%{_prefix}/lib/mono/4.5/Mono.WebBrowser.dll
%{_prefix}/lib/mono/4.5/System.Design.dll
%{_prefix}/lib/mono/4.5/System.Drawing.Design.dll
%{_prefix}/lib/mono/4.5/System.Windows.Forms.DataVisualization.dll
%{_prefix}/lib/mono/4.5/System.Windows.Forms.dll
%{_prefix}/lib/mono/gac/Accessibility
%{_prefix}/lib/mono/gac/Mono.WebBrowser
%{_prefix}/lib/mono/gac/System.Design
%{_prefix}/lib/mono/gac/System.Drawing.Design
%{_prefix}/lib/mono/gac/System.Windows.Forms
%{_prefix}/lib/mono/gac/System.Windows.Forms.DataVisualization

%package -n ibm-data-db2
Summary:        Database connectivity for DB2
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}

%description -n ibm-data-db2
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Database connectivity for DB2.

%files -n ibm-data-db2
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/IBM.Data.DB2.dll
%{_prefix}/lib/mono/gac/IBM.Data.DB2

%package -n mono-extras
Summary:        Extra packages
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:       mono-ms-extras = %{version}
Provides:       mono(Mono.Messaging) = 1.0.5000.0
Provides:       mono(Mono.Messaging.RabbitMQ) = 1.0.5000.0
Provides:       mono(RabbitMQ.Client) = 1.0.5000.0
Provides:       mono(System.Configuration.Install) = 1.0.5000.0
Provides:       mono(System.Management) = 1.0.5000.0
Provides:       mono(System.Messaging) = 1.0.5000.0
Provides:       mono(System.ServiceProcess) = 1.0.5000.0
Provides:       mono(mono-service) = 1.0.5000.0

%description -n mono-extras
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Extra packages.

%files -n mono-extras
%defattr(-, root, root)
%{_bindir}/mono-service
%{_bindir}/mono-service2
%{_mandir}/man1/mono-service.1%ext_man
%{_prefix}/lib/mono/4.5/installutil.*
%{_prefix}/lib/mono/4.5/mono-service.*
%{_prefix}/lib/mono/4.5/mono-symbolicate.*
%{_prefix}/lib/mono/4.5/Mono.Messaging.RabbitMQ.dll
%{_prefix}/lib/mono/4.5/Mono.Messaging.dll
%{_prefix}/lib/mono/4.5/RabbitMQ.Client.Apigen.*
%{_prefix}/lib/mono/4.5/RabbitMQ.Client.dll
%{_prefix}/lib/mono/4.5/System.Configuration.Install.dll
%{_prefix}/lib/mono/4.5/System.Management.dll
%{_prefix}/lib/mono/4.5/System.Messaging.dll
%{_prefix}/lib/mono/4.5/System.Runtime.Caching.dll
%{_prefix}/lib/mono/4.5/System.ServiceProcess.dll
%{_prefix}/lib/mono/4.5/System.Xaml.dll
%{_prefix}/lib/mono/gac/Mono.Messaging
%{_prefix}/lib/mono/gac/Mono.Messaging.RabbitMQ
%{_prefix}/lib/mono/gac/RabbitMQ.Client
%{_prefix}/lib/mono/gac/System.Configuration.Install
%{_prefix}/lib/mono/gac/System.Management
%{_prefix}/lib/mono/gac/System.Messaging
%{_prefix}/lib/mono/gac/System.Runtime.Caching
%{_prefix}/lib/mono/gac/System.ServiceProcess
%{_prefix}/lib/mono/gac/System.Xaml
%{_prefix}/lib/mono/gac/mono-service

%package -n mono-data-sqlite
Summary:        Database connectivity for Mono
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Requires:       mono-data = %{version}
Provides:       mono(Mono.Data.Sqlite) = 1.0.5000.0

%description -n mono-data-sqlite
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Database connectivity for Mono.

%files -n mono-data-sqlite
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/Mono.Data.Sqlite.dll
%{_prefix}/lib/mono/gac/Mono.Data.Sqlite

%package -n mono-wcf
Summary:        Mono implementation of WCF, Windows Communication Foundation
License:        MIT and MS-PL
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}

%description -n mono-wcf
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of WCF, Windows Communication Foundation

%files -n mono-wcf
%defattr(-, root, root)
%{_bindir}/svcutil
%{_libdir}/pkgconfig/wcf.pc
%{_prefix}/lib/mono/4.5/System.Data.Services.dll
%{_prefix}/lib/mono/4.5/System.IdentityModel.Selectors.dll
%{_prefix}/lib/mono/4.5/System.IdentityModel.dll
%{_prefix}/lib/mono/4.5/System.Runtime.DurableInstancing.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.Activation.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.Discovery.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.Routing.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.Web.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.dll
%{_prefix}/lib/mono/4.5/System.ServiceModel.Internals.dll
%{_prefix}/lib/mono/4.5/System.Workflow.Activities.dll
%{_prefix}/lib/mono/4.5/System.Workflow.ComponentModel.dll
%{_prefix}/lib/mono/4.5/System.Workflow.Runtime.dll
%{_prefix}/lib/mono/4.5/svcutil.*
%{_prefix}/lib/mono/gac/System.Data.Services
%{_prefix}/lib/mono/gac/System.IdentityModel
%{_prefix}/lib/mono/gac/System.IdentityModel.Selectors
%{_prefix}/lib/mono/gac/System.Runtime.DurableInstancing
%{_prefix}/lib/mono/gac/System.ServiceModel
%{_prefix}/lib/mono/gac/System.ServiceModel.Activation
%{_prefix}/lib/mono/gac/System.ServiceModel.Discovery
%{_prefix}/lib/mono/gac/System.ServiceModel.Routing
%{_prefix}/lib/mono/gac/System.ServiceModel.Web
%{_prefix}/lib/mono/gac/System.ServiceModel.Internals
%{_prefix}/lib/mono/gac/System.Workflow.Activities
%{_prefix}/lib/mono/gac/System.Workflow.ComponentModel
%{_prefix}/lib/mono/gac/System.Workflow.Runtime


%package -n mono-winfxcore
Summary:        Mono implementation of core WinFX APIs
License:        MIT and MS-PL
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:	mono-winfx
Obsoletes:	mono-winfx

%description -n mono-winfxcore
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of core WinFX APIs

%files -n mono-winfxcore
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/System.Data.Services.Client.dll*
%{_prefix}/lib/mono/4.5/WindowsBase.dll*
%{_prefix}/lib/mono/gac/System.Data.Services.Client
%{_prefix}/lib/mono/gac/WindowsBase

%package -n mono-web
Summary:        Mono implementation of ASP
License:        MIT and MS-PL
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:	mono-web-devel
Obsoletes:	mono-web-devel
Provides:       mono-remoting = %{version}
Provides:       mono-web-forms = %{version}
Provides:       mono-web-services = %{version}
Provides:       mono(Mono.Http) = 1.0.5000.0
Provides:       mono(System.Runtime.Remoting) = 1.0.5000.0
Provides:       mono(System.Runtime.Remoting) = 2.0.0.0
Provides:       mono(System.Runtime.Serialization.Formatters.Soap) = 1.0.5000.0
Provides:       mono(System.Web) = 1.0.5000.0
Provides:       mono(System.Web.Razor) = 2.0.0.0
Provides:       mono(System.Web.Services) = 1.0.5000.0
Provides:       mono(System.Web.WebPages.Deployment) = 2.1.0.0
Provides:       mono(System.Web.WebPages.Razor) = 2.0.0.0
Provides:	mono(System.Web.DataVisualization) = 4.0.0.0

%description -n mono-web
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of ASP.NET, Remoting and Web Services.

%files -n mono-web
%defattr(-, root, root)
%config %{_sysconfdir}/mono/2.0/Browsers
%config %{_sysconfdir}/mono/2.0/DefaultWsdlHelpGenerator.aspx
%config %{_sysconfdir}/mono/2.0/web.config
%config %{_sysconfdir}/mono/4.0/Browsers
%config %{_sysconfdir}/mono/4.0/DefaultWsdlHelpGenerator.aspx
%config %{_sysconfdir}/mono/4.0/web.config
%config %{_sysconfdir}/mono/4.5/Browsers
%config %{_sysconfdir}/mono/4.5/DefaultWsdlHelpGenerator.aspx
%config %{_sysconfdir}/mono/4.5/web.config
%config %{_sysconfdir}/mono/browscap.ini
%config %{_sysconfdir}/mono/mconfig/config.xml
%dir %{_sysconfdir}/mono/mconfig
%{_bindir}/disco
%{_bindir}/mconfig
%{_bindir}/soapsuds
%{_bindir}/wsdl
%{_bindir}/wsdl2
%{_bindir}/xsd
%{_libdir}/pkgconfig/aspnetwebstack.pc
%{_mandir}/man1/disco.1%ext_man
%{_mandir}/man1/mconfig.1%ext_man
%{_mandir}/man1/soapsuds.1%ext_man
%{_mandir}/man1/wsdl.1%ext_man
%{_mandir}/man1/xsd.1%ext_man
%{_prefix}/lib/mono/4.5/Mono.Http.dll
%{_prefix}/lib/mono/4.5/System.ComponentModel.Composition.dll
%{_prefix}/lib/mono/4.5/System.ComponentModel.DataAnnotations.dll
%{_prefix}/lib/mono/4.5/System.Runtime.Remoting.dll
%{_prefix}/lib/mono/4.5/System.Runtime.Serialization.Formatters.Soap.dll
%{_prefix}/lib/mono/4.5/System.Web.Abstractions.dll
%{_prefix}/lib/mono/4.5/System.Web.ApplicationServices.dll
%{_prefix}/lib/mono/4.5/System.Web.Http.dll
%{_prefix}/lib/mono/4.5/System.Web.Http.SelfHost.dll
%{_prefix}/lib/mono/4.5/System.Web.Http.WebHost.dll
%{_prefix}/lib/mono/4.5/System.Web.Mobile.dll
%{_prefix}/lib/mono/4.5/System.Web.RegularExpressions.dll
%{_prefix}/lib/mono/4.5/System.Web.Routing.dll
%{_prefix}/lib/mono/4.5/System.Web.Razor.dll
%{_prefix}/lib/mono/4.5/System.Web.Services.dll
%{_prefix}/lib/mono/4.5/System.Web.WebPages.Deployment.dll
%{_prefix}/lib/mono/4.5/System.Web.WebPages.Razor.dll
%{_prefix}/lib/mono/4.5/System.Web.WebPages.dll
%{_prefix}/lib/mono/4.5/System.Web.dll
%{_prefix}/lib/mono/4.5/disco.*
%{_prefix}/lib/mono/4.5/mconfig.*
%{_prefix}/lib/mono/4.5/soapsuds.*
%{_prefix}/lib/mono/4.5/wsdl.*
%{_prefix}/lib/mono/4.5/xsd.*
%{_prefix}/lib/mono/4.5/Microsoft.Web.Infrastructure.dll
%{_prefix}/lib/mono/gac/Microsoft.Web.Infrastructure
%{_prefix}/lib/mono/gac/Mono.Http
%{_prefix}/lib/mono/gac/System.ComponentModel.Composition
%{_prefix}/lib/mono/gac/System.ComponentModel.DataAnnotations
%{_prefix}/lib/mono/gac/System.Runtime.Remoting
%{_prefix}/lib/mono/gac/System.Runtime.Serialization.Formatters.Soap
%{_prefix}/lib/mono/gac/System.Web
%{_prefix}/lib/mono/gac/System.Web.Abstractions
%{_prefix}/lib/mono/gac/System.Web.ApplicationServices
%{_prefix}/lib/mono/gac/System.Web.Http
%{_prefix}/lib/mono/gac/System.Web.Http.SelfHost
%{_prefix}/lib/mono/gac/System.Web.Http.WebHost
%{_prefix}/lib/mono/gac/System.Web.Mobile
%{_prefix}/lib/mono/gac/System.Web.RegularExpressions
%{_prefix}/lib/mono/gac/System.Web.Routing
%{_prefix}/lib/mono/gac/System.Web.Razor
%{_prefix}/lib/mono/gac/System.Web.Services
%{_prefix}/lib/mono/gac/System.Web.WebPages.Deployment
%{_prefix}/lib/mono/gac/System.Web.WebPages.Razor
%{_prefix}/lib/mono/gac/System.Web.WebPages

%package -n mono-mvc
Summary:        Mono implementation of ASP
License:        MIT and MS-PL
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:	mono-mvc-devel
Obsoletes:	mono-mvc-devel

%description -n mono-mvc
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono implementation of ASP.NET MVC.

%files -n mono-mvc
%defattr(-, root, root)
%{_libdir}/pkgconfig/system.web.extensions.design_1.0.pc
%{_libdir}/pkgconfig/system.web.extensions_1.0.pc
%{_libdir}/pkgconfig/system.web.mvc.pc
%{_libdir}/pkgconfig/system.web.mvc2.pc
%{_libdir}/pkgconfig/system.web.mvc3.pc
%{_prefix}/lib/mono/4.5/System.Web.DynamicData.dll
%{_prefix}/lib/mono/4.5/System.Web.Extensions.Design.dll
%{_prefix}/lib/mono/4.5/System.Web.Extensions.dll
%{_prefix}/lib/mono/4.5/System.Web.Mvc.dll
%{_prefix}/lib/mono/gac/System.Web.DynamicData
%{_prefix}/lib/mono/gac/System.Web.Extensions
%{_prefix}/lib/mono/gac/System.Web.Extensions.Design
%{_prefix}/lib/mono/gac/System.Web.Mvc

%package -n mono-data-oracle
Summary:        Database connectivity for Mono
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Requires:       mono-data = %{version}
Provides:       mono(System.Data.OracleClient) = 1.0.5000.0

%description -n mono-data-oracle
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Database connectivity for Mono.

%files -n mono-data-oracle
%defattr(-, root, root)
%{_prefix}/lib/mono/4.5/System.Data.OracleClient.dll
%{_prefix}/lib/mono/gac/System.Data.OracleClient

%package -n mono-nunit
Summary:        NUnit Testing Framework
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}
Provides:	mono-nunit-devel
Obsoletes:	mono-nunit-devel

%description -n mono-nunit
NUnit is a unit-testing framework for all .Net languages.  Initially
ported from JUnit, the current release, version 2.2,  is the fourth
major release of this  Unit based unit testing tool for Microsoft .NET.
It is written entirely in C# and  has been completely redesigned to
take advantage of many .NET language		 features, for example
custom attributes and other reflection related capabilities. NUnit
brings xUnit to all .NET languages.

%files -n mono-nunit
%defattr(-, root, root)
%{_libdir}/pkgconfig/mono-nunit.pc
%{_bindir}/nunit-console
%{_bindir}/nunit-console2
%{_bindir}/nunit-console4
%{_prefix}/lib/mono/4.5/nunit-console-runner.dll
%{_prefix}/lib/mono/4.5/nunit-console.*
%{_prefix}/lib/mono/4.5/nunit.core.dll
%{_prefix}/lib/mono/4.5/nunit.core.extensions.dll
%{_prefix}/lib/mono/4.5/nunit.core.interfaces.dll
%{_prefix}/lib/mono/4.5/nunit.framework.dll
%{_prefix}/lib/mono/4.5/nunit.framework.extensions.dll
%{_prefix}/lib/mono/4.5/nunit.mocks.dll
%{_prefix}/lib/mono/4.5/nunit.util.dll
%{_prefix}/lib/mono/gac/nunit-console-runner
%{_prefix}/lib/mono/gac/nunit.core
%{_prefix}/lib/mono/gac/nunit.core.extensions
%{_prefix}/lib/mono/gac/nunit.core.interfaces
%{_prefix}/lib/mono/gac/nunit.framework
%{_prefix}/lib/mono/gac/nunit.framework.extensions
%{_prefix}/lib/mono/gac/nunit.mocks
%{_prefix}/lib/mono/gac/nunit.util

%package -n mono-devel
Summary:        Mono development tools
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       libgdiplus-devel
Requires:       mono-core = %{version}
# Required because they are referenced by .pc files
Requires:       mono-data = %{version}
Requires:       mono-data-oracle = %{version}
Requires:       mono-extras = %{version}
Requires:       mono-web = %{version}
Requires:       mono-winforms = %{version}
Requires:       pkgconfig
Provides:       mono-xbuild = %{version}
# We build natively on ppc64 now
%ifarch ppc64
Provides:       mono-biarchcompat = %{version}
%endif
Provides:       mono(PEAPI) = 1.0.5000.0
Provides:       mono(resgen) = 1.0.5000.0

%description -n mono-devel
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. This package contains compilers and
other tools needed to develop .NET applications.

Mono development tools.

%post -n mono-devel -p /sbin/ldconfig

%postun -n mono-devel -p /sbin/ldconfig

%files -n mono-devel
%defattr(-, root, root)
%{_bindir}/caspol
%{_bindir}/ccrewrite
%{_bindir}/cccheck
%{_bindir}/cert2spc
%{_bindir}/dtd2rng
%{_bindir}/dtd2xsd
%{_bindir}/genxs
%{_bindir}/httpcfg
%{_bindir}/ilasm
%{_bindir}/installvst
%{_bindir}/lc
%{_bindir}/macpack
%{_bindir}/makecert
%{_bindir}/mdbrebase
%{_bindir}/mkbundle
%{_bindir}/mono-api-info
%{_bindir}/mono-cil-strip
%{_bindir}/mono-find-provides
%{_bindir}/mono-find-requires
%{_bindir}/mono-heapviz
%{_bindir}/mono-shlib-cop
%{_bindir}/mono-xmltool
%{_bindir}/monodis
%{_bindir}/monolinker
%{_bindir}/monop
%{_bindir}/monop2
%{_bindir}/mprof-report
%{_bindir}/pdb2mdb
%{_bindir}/pedump
%{_bindir}/permview
%{_bindir}/resgen
%{_bindir}/resgen2
%{_bindir}/secutil
%{_bindir}/sgen
%{_bindir}/signcode
%{_bindir}/xbuild
%{_bindir}/mono-api-html
%dir %{_datadir}/mono-2.0
%dir %{_datadir}/mono-2.0/mono
%dir %{_datadir}/mono-2.0/mono/cil
%{_datadir}/mono-2.0/mono/cil/cil-opcodes.xml
%{_datadir}/mono-2.0/mono/profiler/mono-profiler-coverage.suppression
%{_libdir}/libmono-profiler-*.*
%{_libdir}/pkgconfig/cecil.pc
%{_libdir}/pkgconfig/dotnet.pc
%{_libdir}/pkgconfig/dotnet35.pc
%{_libdir}/pkgconfig/mono-cairo.pc
%{_libdir}/pkgconfig/mono-lineeditor.pc
%{_libdir}/pkgconfig/mono-options.pc
%{_libdir}/pkgconfig/mono.pc
%{_libdir}/pkgconfig/xbuild12.pc
%{_mandir}/man1/al.1%ext_man
%{_mandir}/man1/ccrewrite.1%ext_man
%{_mandir}/man1/cccheck.1%ext_man
%{_mandir}/man1/cert2spc.1%ext_man
%{_mandir}/man1/dtd2xsd.1%ext_man
%{_mandir}/man1/genxs.1%ext_man
%{_mandir}/man1/httpcfg.1%ext_man
%{_mandir}/man1/ilasm.1%ext_man
%{_mandir}/man1/lc.1%ext_man
%{_mandir}/man1/macpack.1%ext_man
%{_mandir}/man1/makecert.1%ext_man
%{_mandir}/man1/mdb2ppdb.1%ext_man
%{_mandir}/man1/mkbundle.1%ext_man
%{_mandir}/man1/mono-api-info.1%ext_man
%{_mandir}/man1/mono-cil-strip.1%ext_man
%{_mandir}/man1/mono-shlib-cop.1%ext_man
%{_mandir}/man1/mono-xmltool.1%ext_man
%{_mandir}/man1/monodis.1%ext_man
%{_mandir}/man1/monolinker.1%ext_man
%{_mandir}/man1/monop.1%ext_man
%{_mandir}/man1/mprof-report.1%ext_man
%{_mandir}/man1/pdb2mdb.1%ext_man
%{_mandir}/man1/permview.1%ext_man
%{_mandir}/man1/mono-profilers.1%ext_man
%{_mandir}/man1/resgen.1%ext_man
%{_mandir}/man1/secutil.1%ext_man
%{_mandir}/man1/sgen.1%ext_man
%{_mandir}/man1/signcode.1%ext_man
%{_mandir}/man1/xbuild.1%ext_man
%{_prefix}/lib/mono-source-libs
%{_prefix}/lib/mono/4.0
%{_prefix}/lib/mono/4.7.1-api
%{_prefix}/lib/mono/4.7-api
%{_prefix}/lib/mono/4.6.2-api
%{_prefix}/lib/mono/4.6.1-api
%{_prefix}/lib/mono/4.6-api
%{_prefix}/lib/mono/4.5.2-api
%{_prefix}/lib/mono/4.5.1-api
%{_prefix}/lib/mono/4.5-api
%{_prefix}/lib/mono/4.0-api
%{_prefix}/lib/mono/3.5-api
%{_prefix}/lib/mono/2.0-api
%{_prefix}/lib/mono/4.5/Microsoft.Build.dll
%{_prefix}/lib/mono/4.5/Microsoft.Build.Engine.dll
%{_prefix}/lib/mono/4.5/Microsoft.Build.Framework.dll
%{_prefix}/lib/mono/4.5/Microsoft.Build.Tasks.v4.0.dll
%{_prefix}/lib/mono/4.5/Microsoft.Build.Utilities.v4.0.dll
%{_prefix}/lib/mono/4.5/Mono.Debugger.Soft.dll
%{_prefix}/lib/mono/4.5/Mono.CodeContracts.dll
%{_prefix}/lib/mono/4.5/PEAPI.dll
%{_prefix}/lib/mono/4.5/caspol.*
%{_prefix}/lib/mono/4.5/cccheck.*
%{_prefix}/lib/mono/4.5/ccrewrite.*
%{_prefix}/lib/mono/4.5/cert2spc.*
%{_prefix}/lib/mono/4.5/csi.*
%{_prefix}/lib/mono/4.5/dtd2rng.*
%{_prefix}/lib/mono/4.5/dtd2xsd.*
%{_prefix}/lib/mono/4.5/genxs.*
%{_prefix}/lib/mono/4.5/httpcfg.*
%{_prefix}/lib/mono/4.5/ictool.*
%{_prefix}/lib/mono/4.5/ilasm.*
%{_prefix}/lib/mono/4.5/installvst.*
%{_prefix}/lib/mono/4.5/lc.*
%{_prefix}/lib/mono/4.5/macpack.*
%{_prefix}/lib/mono/4.5/makecert.*
%{_prefix}/lib/mono/4.5/mdbrebase.*
%{_prefix}/lib/mono/4.5/mkbundle.*
%{_prefix}/lib/mono/4.5/mono-api-html.*
%{_prefix}/lib/mono/4.5/mono-api-info.*
%{_prefix}/lib/mono/4.5/mono-cil-strip.*
%{_prefix}/lib/mono/4.5/mono-shlib-cop.*
%{_prefix}/lib/mono/4.5/mono-xmltool.*
%{_prefix}/lib/mono/4.5/monolinker.*
%{_prefix}/lib/mono/4.5/monop.*
%{_prefix}/lib/mono/4.5/pdb2mdb.*
%{_prefix}/lib/mono/4.5/permview.*
%{_prefix}/lib/mono/4.5/resgen.*
%{_prefix}/lib/mono/4.5/secutil.*
%{_prefix}/lib/mono/4.5/sgen.*
%{_prefix}/lib/mono/4.5/signcode.*
%{_prefix}/lib/mono/4.5/xbuild.*
%{_prefix}/lib/mono/4.5/MSBuild/
%{_prefix}/lib/mono/4.5/Microsoft.Build.xsd
%{_prefix}/lib/mono/4.5/Microsoft.CSharp.targets
%{_prefix}/lib/mono/4.5/Microsoft.Common.targets
%{_prefix}/lib/mono/4.5/Microsoft.Common.tasks
%{_prefix}/lib/mono/4.5/Microsoft.VisualBasic.targets
%{_prefix}/lib/mono/4.5/Mono.XBuild.Tasks.dll
%{_prefix}/lib/mono/4.5/SMDiagnostics.dll
%{_prefix}/lib/mono/4.5/System.Deployment.dll
%{_prefix}/lib/mono/gac/Microsoft.Build
%{_prefix}/lib/mono/gac/Microsoft.Build.Engine
%{_prefix}/lib/mono/gac/Microsoft.Build.Framework
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.v4.0
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.v12.0/
%{_prefix}/lib/mono/gac/Microsoft.Build.Tasks.Core/
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.v4.0
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.v12.0/
%{_prefix}/lib/mono/gac/Microsoft.Build.Utilities.Core/
%{_prefix}/lib/mono/gac/Mono.CodeContracts
%{_prefix}/lib/mono/gac/Mono.Debugger.Soft
%{_prefix}/lib/mono/gac/Mono.XBuild.Tasks/
%{_prefix}/lib/mono/gac/PEAPI
%{_prefix}/lib/mono/gac/SMDiagnostics
%{_prefix}/lib/mono/gac/System.Deployment
%{_prefix}/lib/mono/xbuild
%{_prefix}/lib/mono/xbuild-frameworks
%{_prefix}/lib/mono/msbuild/15.0/bin/Roslyn
%{_prefix}/lib64/mono/lldb

%package -n mono-reactive
Summary:        Reactive Extensions
License:        Apache-2.0
Group:          Development/Languages/Mono
Requires:       mono-core = %{version}

%description -n mono-reactive
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Microsoft's Reactive Extensions.

%files -n mono-reactive
%defattr(-, root, root)
%{_libdir}/pkgconfig/reactive.pc
%{_prefix}/lib/mono/4.5/System.Reactive.Core.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Debugger.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Experimental.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Interfaces.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Linq.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Observable.Aliases.dll
%{_prefix}/lib/mono/4.5/System.Reactive.PlatformServices.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Providers.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Runtime.Remoting.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Windows.Forms.dll
%{_prefix}/lib/mono/4.5/System.Reactive.Windows.Threading.dll
%{_prefix}/lib/mono/gac/System.Reactive.Core/
%{_prefix}/lib/mono/gac/System.Reactive.Debugger/
%{_prefix}/lib/mono/gac/System.Reactive.Experimental/
%{_prefix}/lib/mono/gac/System.Reactive.Interfaces/
%{_prefix}/lib/mono/gac/System.Reactive.Linq/
%{_prefix}/lib/mono/gac/System.Reactive.Observable.Aliases/
%{_prefix}/lib/mono/gac/System.Reactive.PlatformServices/
%{_prefix}/lib/mono/gac/System.Reactive.Providers/
%{_prefix}/lib/mono/gac/System.Reactive.Runtime.Remoting/
%{_prefix}/lib/mono/gac/System.Reactive.Windows.Forms/
%{_prefix}/lib/mono/gac/System.Reactive.Windows.Threading/

%package -n monodoc-core
Summary:        Monodoc - Documentation tools for C# code
License:        LGPL-2.1
Group:          Development/Tools/Other
Requires:       mono-core = %{version}
# Added to uncompress and compare documentation used by build-compare
Requires:       unzip
Provides:       monodoc
Provides:       monodoc-devel
Obsoletes:      monodoc
Obsoletes:      monodoc-devel

%description -n monodoc-core
Monodoc-core contains documentation tools for C#.

%files -n monodoc-core
%defattr(-, root, root)
%{_bindir}/mdassembler
%{_bindir}/mdoc
%{_bindir}/mdoc-assemble
%{_bindir}/mdoc-export-html
%{_bindir}/mdoc-export-msxdoc
%{_bindir}/mdoc-update
%{_bindir}/mdoc-validate
%{_bindir}/mdvalidater
%{_bindir}/mod
%{_bindir}/monodocer
%{_bindir}/monodocs2html
%{_bindir}/monodocs2slashdoc
%{_libdir}/pkgconfig/monodoc.pc
%{_mandir}/man1/mdassembler.1%ext_man
%{_mandir}/man1/mdoc-assemble.1%ext_man
%{_mandir}/man1/mdoc-export-html.1%ext_man
%{_mandir}/man1/mdoc-export-msxdoc.1%ext_man
%{_mandir}/man1/mdoc-update.1%ext_man
%{_mandir}/man1/mdoc-validate.1%ext_man
%{_mandir}/man1/mdoc.1%ext_man
%{_mandir}/man1/mdvalidater.1%ext_man
%{_mandir}/man1/monodocer.1%ext_man
%{_mandir}/man1/monodocs2html.1%ext_man
%{_mandir}/man5/mdoc.5%ext_man
%{_prefix}/lib/mono/4.5/mdoc.*
%{_prefix}/lib/mono/4.5/mod.*
%{_prefix}/lib/mono/gac/monodoc
%{_prefix}/lib/mono/monodoc
%{_prefix}/lib/monodoc

%package -n mono-complete
Summary:        Install everything built from the mono source tree
License:        LGPL-2.1
Group:          Development/Languages/Mono
Requires:       ibm-data-db2 = %{version}
Requires:       libmono-2_0-1 = %{version}
Requires:       libmono-2_0-devel = %{version}
Requires:       mono-core = %{version}
%if %llvm == yes
Requires:       libmono-llvm0 = %{version}
%endif
%if %sgen == yes
Requires:       libmonosgen-2_0-1 = %{version}
Requires:       libmonosgen-2_0-devel = %{version}
%endif
Requires:       libmonoboehm-2_0-1 = %{version}
Requires:       libmonoboehm-2_0-devel = %{version}
Requires:       mono-data = %{version}
Requires:       mono-data-oracle = %{version}
Requires:       mono-data-sqlite = %{version}
Requires:       mono-devel = %{version}
Requires:       mono-extras = %{version}
Requires:       mono-locale-extras = %{version}
Requires:       mono-mvc = %{version}
Requires:       mono-nunit = %{version}
Requires:       mono-reactive = %{version}
Requires:       mono-wcf = %{version}
Requires:       mono-web = %{version}
Requires:       mono-winforms = %{version}
Requires:       mono-winfxcore = %{version}
Requires:       monodoc-core = %{version}

%description -n mono-complete
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Install everything built from the mono source tree.  Note that this does
not install anything from outside the mono source (XSP, mono-basic, etc.).

%files -n mono-complete
%defattr(-, root, root)

%changelog


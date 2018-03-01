%{?mingw_package_header}

%global mingw_pkg_name SharpSSH
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:		mingw-SharpSSH
Version: 	1.1.1.13
Release: 	5%{?dist}
Summary: 	SharpSSH is a pure .NET implementation of the SSH2 client protocol suite.
Group: 		System Environment/Libraries
License: 	Tamir Gal (c) 2007 and jcraft.com
URL:		http://sourceforge.net/projects/sharpssh/
Source0: 	SharpSSH-%{version}.src.zip
Source1:	SharpSSH-License
Source2:	DiffieHellman.dll
Source3:	Org.Mentalis.Security.dll
Source4:	Tamir.SharpSSH.dll
Patch0:		SharpSSH-bigfiles.patch
Patch1:		SharpSSH-detailed.patch
BuildArch:      noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildRequires:	mono-core
BuildRequires:	monodevelop
BuildRequires:	mingw32-filesystem
BuildRequires:	mingw64-filesystem
BuildRequires: 	mingw-binutils-generic

%description
SharpSSH is a pure .NET implementation of the SSH2 client protocol suite. 
It provides an API for communication with SSH servers and can be integrated 
into any .NET application. 

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2
Requires:       mingw32-mono >= 2.11

%description -n mingw32-%{mingw_pkg_name}
SharpSSH is a pure .NET implementation of the SSH2 client protocol suite.
It provides an API for communication with SSH servers and can be integrated
into any .NET application.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-mono >= 2.11

%description -n mingw64-%{mingw_pkg_name}
SharpSSH is a pure .NET implementation of the SSH2 client protocol suite.
It provides an API for communication with SSH servers and can be integrated
into any .NET application.

%prep
%setup -q -n SharpSSH-%{version}.src
%patch0 -p1
%patch1 -p0

cat > SharpSSH.pc.32 << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_bindir}

Name: SharpSSH
Description: SharpSSH is a pure .NET implementation of the SSH2
Requires: 
Version: %{version}
Libs: -r:${libdir}/DiffieHellman.dll -r:${libdir}/Org.Mentalis.Security.dll -r:${libdir}/Tamir.SharpSSH.dll
Cflags:
EOF

cat > SharpSSH.pc.64 << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_bindir}

Name: SharpSSH
Description: SharpSSH is a pure .NET implementation of the SSH2
Requires:
Version: %{version}
Libs: -r:${libdir}/DiffieHellman.dll -r:${libdir}/Org.Mentalis.Security.dll -r:${libdir}/Tamir.SharpSSH.dll
Cflags:
EOF


%build
#mdtool project-export -f:"MSBuild (Visual Studio 2010)" SharpSSH.sln
#mdtool build --target:Build --configuration:Debug

%install  
rm -rf $RPM_BUILD_ROOT

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/SharpSSH
install -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{mingw32_datadir}/SharpSSH/License

#install -m 775 bin/Debug/*.exe $RPM_BUILD_ROOT%{mingw32_bindir}/
#install -m 664 bin/Debug/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}/
#install -m 664 bin/Debug/*.mdb $RPM_BUILD_ROOT%{mingw32_bindir}/

install -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{mingw32_bindir}/
install -m 664 %{SOURCE3} $RPM_BUILD_ROOT%{mingw32_bindir}/
install -m 664 %{SOURCE4} $RPM_BUILD_ROOT%{mingw32_bindir}/

install -m 644 SharpSSH.pc.32 $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/SharpSSH.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/SharpSSH
install -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{mingw64_datadir}/SharpSSH/License

#install -m 775 bin/Debug/*.exe $RPM_BUILD_ROOT%{mingw64_bindir}/
#install -m 664 bin/Debug/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}/
#install -m 664 bin/Debug/*.mdb $RPM_BUILD_ROOT%{mingw64_bindir}/

install -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{mingw64_bindir}/
install -m 664 %{SOURCE3} $RPM_BUILD_ROOT%{mingw64_bindir}/
install -m 664 %{SOURCE4} $RPM_BUILD_ROOT%{mingw64_bindir}/

install -m 644 SharpSSH.pc.64 $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/SharpSSH.pc


%clean
rm -rf $RPM_BUILD_ROOT

%files -n mingw32-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw32_datadir}/SharpSSH/License
%{mingw32_bindir}/*.dll
#%{mingw32_bindir}/*.exe
%{mingw32_libdir}/pkgconfig/SharpSSH.pc
#%{mingw32_bindir}/*.mdb
#%{mingw32_bindir}/sharpSshTest.exe

%files -n mingw64-%{mingw_pkg_name}
%defattr(-, root, root, -)
%{mingw64_datadir}/SharpSSH/License
%{mingw64_bindir}/*.dll
#%{mingw64_bindir}/*.exe
%{mingw64_libdir}/pkgconfig/SharpSSH.pc
#%{mingw64_bindir}/*.mdb
#%{mingw64_bindir}/sharpSshTest.exe



%changelog
* Wed Feb 09 2011 Mikkel Kruse Johnsen <mikkel@linet.dk>
- first draft of spec file


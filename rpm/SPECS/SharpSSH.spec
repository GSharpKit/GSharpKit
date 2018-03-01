%define debug_package %{nil}

Name:		SharpSSH
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
BuildRequires:	mono-devel

%description
SharpSSH is a pure .NET implementation of the SSH2 client protocol suite. 
It provides an API for communication with SSH servers and can be integrated 
into any .NET application. 

%prep
%setup -q -n SharpSSH-%{version}.src
%patch0 -p1
%patch1 -p0

cat > SharpSSH.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_bindir}

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
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/SharpSSH
install -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/SharpSSH/License

install -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/
install -m 664 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/
install -m 664 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/

install -m 644 SharpSSH.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/SharpSSH.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_datadir}/SharpSSH/License
%{_bindir}/*.dll
%{_datadir}/pkgconfig/SharpSSH.pc

%changelog
* Thu Jan 26 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- first draft of spec file


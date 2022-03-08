%{?mingw_package_header}

%global mingw_pkg_name Mono.Addins
%global mingw_build_win32 0
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /bin
%define api_version 1.0.0.0

Name:		mingw-Mono.Addins
Version:	1.3.12
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		https://github.com/mono/mono-addins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	mono-addins-%{version}.tar.xz

BuildArch: 	noarch

BuildRequires:  mingw32-filesystem mingw64-filesystem

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Obsoletes:      mingw64-mono-addins
Provides:       mingw64-mono-addins

%description -n mingw64-%{mingw_pkg_name}
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.


%prep

%setup -q -n mono-addins-%{version}
nuget install Mono.Cecil -Version 0.11.4

cat > mono-addins64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: %{mingw_pkg_name}
Description: %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Mono.Addins.dll -r:${libdir}/Mono.Addins.CecilReflector.dll -r:${libdir}/Mono.Cecil.dll
Cflags:
EOF

%build
dotnet restore
cd Mono.Addins.CecilReflector
dotnet msbuild /p:Configuration=Release Mono.Addins.CecilReflector.csproj

%install
%{__rm} -rf %{buildroot}

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 bin/netstandard2.0/Mono.Addins.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 bin/netstandard2.0/Mono.Addins.CecilReflector.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Mono.Cecil.0.11.4/lib/netstandard2.0/Mono.Cecil.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 mono-addins64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/mono-addins.pc

%clean
%{__rm} -rf %{buildroot}

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Mono.Addins.dll
%{mingw64_prefix}%{libdir}/Mono.Addins.CecilReflector.dll
%{mingw64_prefix}%{libdir}/Mono.Cecil.dll
%{mingw64_datadir}/pkgconfig/mono-addins.pc

%changelog
* Thu Jun 03 2010 Mikkel Kruse Johnsen <mikkel@linet.dk> - 0.5-1
- Updated to 0.5

* Mon Apr 13 2009 Jesse Keating <jkeating@redhat.com> - 0.4-6.20091702svn127062.1
- re-enable ppc

* Fri Apr 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-5.20091702svn127062.1
- Exclude ppc

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5.20091702svn127062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20091702svn127062
- update from svn

* Tue Feb 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20091002svn126354
- large update from svn
- now uses a tarball
- add mautil manual

* Thu Jan 29 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20081215svn105642
- update to 2.4 svn build
- remove mautil manuals

* Thu Dec 11 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-3
- Rebuild
- Correct licence to MIT
- Replaced patch with sed

* Tue Nov 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-2
- Fix archs

* Fri Nov 07 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-1
- new release
- removed scan fix patch

* Mon Jul 14 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2.2
- rebuild

* Thu May 01 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2.1
- rebuild

* Tue Apr 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2
- added BR pkgconfig

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-1
- bump (should fix the monodevelop problems)

* Tue Apr 15 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.3-5
- Add patch from Debian to make sure addins don't disappear in f-spot (#442343)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-4
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 <paul@all-the-johnsons.co.uk> 0.3-3
- removed debug package
- spec file fixes
- additional BRs for autoreconf
- excludearch ppc64 added

* Thu Jan 03 2008 <paul@all-the-johnsons.co.uk> 0.3-2
- enabled gui
- spec file fixes

* Wed Dec 19 2007 <paul@all-the-johnsons.co.uk> 0.3-1
- Initial import for FE

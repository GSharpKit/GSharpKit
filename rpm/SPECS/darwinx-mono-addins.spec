Name:		darwinx-mono-addins
Version:	1.3.3
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		http://www.mono-project.com/
Source0:	mono-addins-mono-addins-%{version}.tar.gz	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:	darwinx-mono-core >= 4.8, autoconf, automake
BuildRequires:	pkgconfig

Requires:  	darwinx-filesystem >= 18
Requires:	darwinx-mono-core >= 4.8

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

%prep
%setup -q -n mono-addins-mono-addins-%{version}

#sed -i '' 's!$(prefix)/lib!%{darwinx_libdir}!' configure

%build
sh autogen.sh --disable-gui
%{_darwinx_configure} --disable-gui

%{_darwinx_make}

sn -R bin/Mono.Addins.CecilReflector.dll mono-addins.snk
sn -R bin/Mono.Addins.dll mono-addins.snk
sn -R bin/Mono.Addins.MSBuild.dll mono-addins.snk
sn -R bin/Mono.Addins.Setup.dll mono-addins.snk

%install
%{__rm} -rf %{buildroot}
%{_darwinx_makeinstall} program_transform_name=""

%{__rm} -f $RPM_BUILD_ROOT%{_darwinx_bindir}/mautil
%{__mv} $RPM_BUILD_ROOT%{_darwinx_libdir}/mono/mono-addins/mautil.exe $RPM_BUILD_ROOT%{_darwinx_bindir}/

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_darwinx_bindir}/mautil.exe
%{_darwinx_libdir}/mono/mono-addins
#%{_darwinx_libdir}/mono/gac/Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/Mono.Addins
%{_darwinx_libdir}/mono/gac/Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/Mono.Addins.MSBuild
#%{_darwinx_libdir}/mono/gac/policy.0.2.Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/policy.0.2.Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/policy.0.2.Mono.Addins
%{_darwinx_libdir}/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/policy.0.2.Mono.Addins.MSBuild
#%{_darwinx_libdir}/mono/gac/policy.0.3.Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/policy.0.3.Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/policy.0.3.Mono.Addins
%{_darwinx_libdir}/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/policy.0.3.Mono.Addins.MSBuild
#%{_darwinx_libdir}/mono/gac/policy.0.4.Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/policy.0.4.Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/policy.0.4.Mono.Addins
%{_darwinx_libdir}/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/policy.0.4.Mono.Addins.MSBuild
#%{_darwinx_libdir}/mono/gac/policy.0.5.Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/policy.0.5.Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/policy.0.5.Mono.Addins
%{_darwinx_libdir}/mono/gac/policy.0.5.Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/policy.0.5.Mono.Addins.MSBuild
#%{_darwinx_libdir}/mono/gac/policy.0.6.Mono.Addins.Gui
%{_darwinx_libdir}/mono/gac/policy.0.6.Mono.Addins.Setup
%{_darwinx_libdir}/mono/gac/policy.0.6.Mono.Addins
%{_darwinx_libdir}/mono/gac/policy.0.6.Mono.Addins.CecilReflector
%{_darwinx_libdir}/mono/gac/policy.0.6.Mono.Addins.MSBuild
%{_darwinx_mandir}/man1/mautil.1
%{_darwinx_libdir}/pkgconfig/mono-addins*

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

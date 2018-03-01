%{?mingw_package_header}

%global mingw_pkg_name mono-addins
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

Name:		mingw-mono-addins
Version:	1.3.3
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		http://www.mono-project.com/
Source0:	mono-addins-mono-addins-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

BuildRequires:  mingw32-filesystem mingw64-filesystem
BuildRequires:	mono-devel >= 4.0, gtk-sharp3-devel, autoconf, automake
BuildRequires:	pkgconfig

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw32-glib2
Requires:       mingw32-mono-core >= 4.8

%description -n mingw32-%{mingw_pkg_name}
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}
Requires:       mingw64-glib2
Requires:       mingw64-mono-core >= 4.8

%description -n mingw64-%{mingw_pkg_name}
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.


%prep
%setup -q -n mono-addins-mono-addins-%{version}

%build
sh autogen.sh --disable-gui
make distclean
%mingw_configure "--disable-gui"

# Mingw32
cp mautil/*.csproj build_win32/mautil/
cp Mono.Addins/*.csproj build_win32/Mono.Addins/
cp Mono.Addins.CecilReflector/*.csproj build_win32/Mono.Addins.CecilReflector/
cp Mono.Addins.Gui/*.csproj build_win32/Mono.Addins.Gui/
cp -r Mono.Addins.Gui/icons build_win32/Mono.Addins.Gui/
cp -r Mono.Addins.Gui/gtk-gui build_win32/Mono.Addins.Gui/
cp Mono.Addins.MSBuild/*.csproj build_win32/Mono.Addins.MSBuild/
cp Mono.Addins.Setup/*.csproj build_win32/Mono.Addins.Setup/

cp mono-addins.snk build_win32/

sed -i -e 's!Compile Include="!Compile Include="../../mautil/!' build_win32/mautil/mautil.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins/!' build_win32/Mono.Addins/Mono.Addins.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.CecilReflector/!' build_win32/Mono.Addins.CecilReflector/Mono.Addins.CecilReflector.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.Gui/!' build_win32/Mono.Addins.Gui/Mono.Addins.Gui.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.MSBuild/!' build_win32/Mono.Addins.MSBuild/Mono.Addins.MSBuild.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.Setup/!' build_win32/Mono.Addins.Setup/Mono.Addins.Setup.csproj

# Mingw64
cp mautil/*.csproj build_win64/mautil/
cp Mono.Addins/*.csproj build_win64/Mono.Addins/
cp Mono.Addins.CecilReflector/*.csproj build_win64/Mono.Addins.CecilReflector/
cp Mono.Addins.Gui/*.csproj build_win64/Mono.Addins.Gui/
cp -r Mono.Addins.Gui/icons build_win64/Mono.Addins.Gui/
cp -r Mono.Addins.Gui/gtk-gui build_win64/Mono.Addins.Gui/
cp Mono.Addins.MSBuild/*.csproj build_win64/Mono.Addins.MSBuild/
cp Mono.Addins.Setup/*.csproj build_win64/Mono.Addins.Setup/

cp mono-addins.snk build_win64/

sed -i -e 's!Compile Include="!Compile Include="../../mautil/!' build_win64/mautil/mautil.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins/!' build_win64/Mono.Addins/Mono.Addins.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.CecilReflector/!' build_win64/Mono.Addins.CecilReflector/Mono.Addins.CecilReflector.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.Gui/!' build_win64/Mono.Addins.Gui/Mono.Addins.Gui.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.MSBuild/!' build_win64/Mono.Addins.MSBuild/Mono.Addins.MSBuild.csproj
sed -i -e 's!Compile Include="!Compile Include="../../Mono.Addins.Setup/!' build_win64/Mono.Addins.Setup/Mono.Addins.Setup.csproj

%mingw_make

sn -R build_win32/bin/Mono.Addins.CecilReflector.dll mono-addins.snk
sn -R build_win32/bin/Mono.Addins.dll mono-addins.snk
sn -R build_win32/bin/Mono.Addins.MSBuild.dll mono-addins.snk
sn -R build_win32/bin/Mono.Addins.Setup.dll mono-addins.snk

sn -R build_win64/bin/Mono.Addins.CecilReflector.dll mono-addins.snk
sn -R build_win64/bin/Mono.Addins.dll mono-addins.snk
sn -R build_win64/bin/Mono.Addins.MSBuild.dll mono-addins.snk
sn -R build_win64/bin/Mono.Addins.Setup.dll mono-addins.snk

%install
%{__rm} -rf %{buildroot}
%mingw_make_install program_transform_name="" DESTDIR=$RPM_BUILD_ROOT

# Mingw32
%{__rm} -f $RPM_BUILD_ROOT%{mingw32_bindir}/mautil
%{__mv} $RPM_BUILD_ROOT%{mingw32_libdir}/mono/mono-addins/mautil.exe $RPM_BUILD_ROOT%{mingw32_bindir}/

%{__mv} $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig $RPM_BUILD_ROOT%{mingw32_prefix}/share/

# Mingw64
%{__rm} -f $RPM_BUILD_ROOT%{mingw64_bindir}/mautil
%{__mv} $RPM_BUILD_ROOT%{mingw64_libdir}/mono/mono-addins/mautil.exe $RPM_BUILD_ROOT%{mingw64_bindir}/

%{__mv} $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig $RPM_BUILD_ROOT%{mingw64_prefix}/share/




%clean
%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name} 
%defattr(-,root,root,-)
%{mingw32_bindir}/mautil.exe
%{mingw32_libdir}/mono/mono-addins
#{mingw32_libdir}/mono/gac/Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/Mono.Addins
%{mingw32_libdir}/mono/gac/Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/Mono.Addins.MSBuild
#{mingw32_libdir}/mono/gac/policy.0.2.Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/policy.0.2.Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/policy.0.2.Mono.Addins
%{mingw32_libdir}/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/policy.0.2.Mono.Addins.MSBuild
#{mingw32_libdir}/mono/gac/policy.0.3.Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/policy.0.3.Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/policy.0.3.Mono.Addins
%{mingw32_libdir}/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/policy.0.3.Mono.Addins.MSBuild
#{mingw32_libdir}/mono/gac/policy.0.4.Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/policy.0.4.Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/policy.0.4.Mono.Addins
%{mingw32_libdir}/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/policy.0.4.Mono.Addins.MSBuild
#{mingw32_libdir}/mono/gac/policy.0.5.Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/policy.0.5.Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/policy.0.5.Mono.Addins
%{mingw32_libdir}/mono/gac/policy.0.5.Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/policy.0.5.Mono.Addins.MSBuild
#{mingw32_libdir}/mono/gac/policy.0.6.Mono.Addins.Gui
%{mingw32_libdir}/mono/gac/policy.0.6.Mono.Addins.Setup
%{mingw32_libdir}/mono/gac/policy.0.6.Mono.Addins
%{mingw32_libdir}/mono/gac/policy.0.6.Mono.Addins.CecilReflector
%{mingw32_libdir}/mono/gac/policy.0.6.Mono.Addins.MSBuild
%{mingw32_mandir}/man1/mautil.1
%{mingw32_datadir}/pkgconfig/mono-addins*

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_bindir}/mautil.exe
%{mingw64_libdir}/mono/mono-addins
#{mingw64_libdir}/mono/gac/Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/Mono.Addins
%{mingw64_libdir}/mono/gac/Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/Mono.Addins.MSBuild
#{mingw64_libdir}/mono/gac/policy.0.2.Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/policy.0.2.Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/policy.0.2.Mono.Addins
%{mingw64_libdir}/mono/gac/policy.0.2.Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/policy.0.2.Mono.Addins.MSBuild
#{mingw64_libdir}/mono/gac/policy.0.3.Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/policy.0.3.Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/policy.0.3.Mono.Addins
%{mingw64_libdir}/mono/gac/policy.0.3.Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/policy.0.3.Mono.Addins.MSBuild
#{mingw64_libdir}/mono/gac/policy.0.4.Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/policy.0.4.Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/policy.0.4.Mono.Addins
%{mingw64_libdir}/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/policy.0.4.Mono.Addins.MSBuild
#{mingw64_libdir}/mono/gac/policy.0.5.Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/policy.0.5.Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/policy.0.5.Mono.Addins
%{mingw64_libdir}/mono/gac/policy.0.5.Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/policy.0.5.Mono.Addins.MSBuild
#{mingw64_libdir}/mono/gac/policy.0.6.Mono.Addins.Gui
%{mingw64_libdir}/mono/gac/policy.0.6.Mono.Addins.Setup
%{mingw64_libdir}/mono/gac/policy.0.6.Mono.Addins
%{mingw64_libdir}/mono/gac/policy.0.6.Mono.Addins.CecilReflector
%{mingw64_libdir}/mono/gac/policy.0.6.Mono.Addins.MSBuild
%{mingw64_mandir}/man1/mautil.1
%{mingw64_datadir}/pkgconfig/mono-addins*

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

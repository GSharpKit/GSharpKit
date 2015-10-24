%global cecildll    %(rpm -ql mono-core | grep Cecil.dll$)
%global cecilmdbdll %(rpm -ql mono-core | grep Cecil.Mdb.dll$)
%global nunitver    2.4.8.0

%define rel 2

Name:           darwinx-monodevelop
Version:        4.2.2
Release:        1%{?dist}
Summary:        A full-featured IDE for Mono and Gtk#

Group:          Development/Tools
License:        GPLv2+
URL:            http://monodevelop.com/
Source0:        http://ftp.novell.com/pub/mono/sources/monodevelo/monodevelop-%{version}-%{rel}.tar.bz2
Source1:	maccore-20140417.tar.gz
Source2:	monomac-20140417.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-mono >= 3.0 darwinx-mono-addins >= 0.6
Requires:       darwinx-mono-addins >= 0.6

BuildArch:	noarch

%description
This package provides MonoDevelop, a full-featured IDE for Mono with
syntax colouring, code completion, debugging, project management and
support for C sharp, Visual Basic.NET, Java, Boo, Nemerle and MSIL.


%prep
%setup -q -n monodevelop-%{version} -b 1 -b 2
rm -rf external/monomac
rm -rf external/maccore
mv ../monomac-20140417 external/monomac
rm -rf external/monomac/maccore
mv ../maccore-20140417 external/monomac/maccore

# Remove so no dependency on System.Data.Entity and System.Web.WebPages.Deployment
rm src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/System.Web.Mvc.dll
rm src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/System.Web.Razor.dll
rm src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/System.Web.WebPages.dll
rm src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/System.Web.WebPages.Razor.dll

cp %{_darwinx_prefix}/lib/mono/4.5/System.Web.Mvc.dll src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/
cp %{_darwinx_prefix}/lib/mono/4.5/System.Web.Razor.dll src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/
cp %{_darwinx_prefix}/lib/mono/4.5/System.Web.WebPages.dll src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/
cp %{_darwinx_prefix}/lib/mono/4.5/System.Web.WebPages.Razor.dll src/addins/AspNet/MonoDevelop.AspNet.Mvc/lib/

%build
%{_darwinx_configure} \
	--disable-tests 		\
	--disable-update-mimedb 	\
	--disable-update-desktopdb	\
	--disable-subversion		\
	--disable-gnomeplatform		\
	--disable-macbundle		\
	--enable-macplatform		\
	--enable-monoextensions		\
	--enable-git

%{_darwinx_make}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_darwinx_bindir}/m*
%{_darwinx_prefix}/lib/monodevelop
%{_darwinx_mandir}/man1/m*
%{_darwinx_datadir}/applications/*.desktop
%{_darwinx_datadir}/icons/hicolor/
%{_darwinx_datadir}/mime/packages/monodevelop.xml
%{_darwinx_libdir}/pkgconfig/*.pc
%{_darwinx_datadir}/locale

%changelog
* Sat Jun 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-0
- Bump to 2.4 release

* Mon May 31 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3.1-2
- Build against mono-addins-0.5

* Fri May 28 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3.1-1
- Bump to 2.4 beta 2
- Fix mono.cecil patches - it's gone strange...

* Fri May 07 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3-1
- Bump to 2.4 beta 1
- Updated rmcecildeps patch

* Sun Apr 18 2010 Christian Krause <chkr@fedoraproject.org> - 2.2.2-2
- Fix monodevelop and mdtool wrapper scripts for x86_64

* Fri Mar 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.2-1
- Bump to 2.2.2 bug fix release

* Thu Feb 18 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-2
- Fixes for 64 bit as MD likes setting paths internally (thanks Chris for the fix)
- Fixed my name in the changelog!

* Thu Feb 04 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-1
- Bump to new 2.2.1 release

* Sat Dec 26 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2
- Patch monodevelop.pc file for more monocecil fixes

* Tue Dec 22 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Bump to 2.2 release
- Fix unbundle-cecil patch
- Copy system mono-cecil to build/bin

* Mon Oct 19 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.1.1-1
- Bump to 2.2 beta 2

* Wed Sep 30 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.1.0-3
- Fix for lib64

* Mon Sep 21 2009 Michel Salim <salimma@fedoraproject.org> - 2.1.0-2
- Properly disable bundled Mono.Cecil and NUnit
- Readjust launcher script (bz #523695)
- Remove unnecessary dependencies
- Clean up spec file

* Wed Sep 09 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.1.0-1
- Bump to 2.2 beta 1
- Fixed cecil patch
- Drop desktop patch

* Tue Jun 23 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.0-3
- Fix mdtool libdir issue
- Add additional arcs

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 2.0-2
- Rebuild against newer gecko

* Thu Mar 26 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.0-1
- Full 2.0 release

* Tue Mar 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.3-1.beta2
- Move back to tarballs
- Bump to beta2

* Fri Feb 27 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-2.beta1.20092202svn127584
- Added desktop file patch

* Sun Feb 22 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-1.beta1.20092202svn127584
- Update from svn
- Fix the month on the changelog
- renamed use-system-cecil patch to removed-contrib

* Tue Feb 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-beta1.20091003svn126521
- Update from svn
- retagged as beta 1
- ensure being built against mono-2.4 and mono-addins-0.4

* Tue Feb 03 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.20090203svn125551
- Update from svn

* Fri Jan 29 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.20090129svn124664
- Update from svn

* Sat Jan 24 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.20090124svn124411
- Update from svn

* Fri Jan 16 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.20090116svn123651
- Update from svn
- Altered nunit patch

* Sat Jan 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.200900109svn122940
- Update from svn

* Sun Jan 04 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.2-pre1.200900104svn122336
- Update from svn
- Reversioned as 1.9.1 is out there already

* Tue Dec 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-7.pre1.20081230svn122192
- Update from svn

* Wed Dec 24 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-7.pre1.20081224svn122090
- Update from svn

* Fri Dec 19 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-7.pre1.20081219svn121787
- Update from svn

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-6.pre1.20081217svn121699
- Actually use the svn version!

* Wed Dec 17 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-5.pre1.20081217svn121653
- Update

* Tue Dec 16 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-4.pre1.20081216svn121578
- Update

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-3.pre1
- missed a libdir...

* Sat Nov 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-2.pre1
- remove libdir patch, now using sed

* Sun Nov 23 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9.1-1.pre1
- Update to 1.9.1 preview 1
- Removed R mono-basic and vala

* Sat Oct 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-7
- Fix dependancies of R (BZ 467544)

* Tue Sep 09 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-6
- Added patch to build against 2.0 RC 1
- rebuild against 2.0 RC 1

* Mon Aug 25 2008 Michel Salim <salimma@fedoraproject.org> - 1.9-5
- Use system-provided nunit

* Sat Aug 23 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9-4
- Clean up build dependencies: database support now a separate package
- Clean up spec file and patches

* Fri Aug 08 2008 David Nielsen <gnomeuser@gmail.com> - 1.9-3
- rebase configure patch for fuzz
- file list fix up

* Thu Jul 10 2008 David Nielsen <gnomeuser@gmail.com> 1.9-2
- numerical compare for fedora version test, fixes compile on f10

* Mon Jul 07 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.9-1
- bump to latest beta for md2
- fixes to patch files for mono.cecil
- fix the archs to be mono package happy
- spec file fixes

* Tue May 06 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-6
- added br mono-tools
- removed prepackaged mime

* Thu May 01 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-5.1
- attempt a fix for a text editor to work
- rebuild

* Wed Apr 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-4
- mdtool fix

* Wed Apr 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-3
- remove BR ikvm-devel

* Fri Apr 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-2
- add in gtksourceview2 support

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 1.0-1
- bump to release

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.19-7
- remove ppc specific stuff
- enabled gnomeplatform and c and c++ projects
- add BR monobasic
- remove the debug package

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-6
- disable Requires on ikvm, since ikvm doesn't build from source at the moment

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-5
- ExcludeArch ppc (no mono-nunit22, due to no nant, means no ppc)

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-4
- buildrequires mono-core for gacutil

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.19-3
- use system Mono.Cecil
- use copies of built from source nunit22 rather than bundling (upstream should really uncouple this)

* Thu Feb 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.19-2
- added BR update-desktop-database

* Thu Feb 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.19-1
- bump to preview 1

* Fri Jan 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.18.1-1
- bump

* Wed Dec 19 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.18-1
- fix for BR boo where boo is not supported
- bump to MD0.18

* Tue Nov 13 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.17-4
- added R mono-data-sqlite

* Sun Nov 11 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.17-3
- excludearch ppc64

* Sun Nov 11 2007 David Nielsen <david@lovesunix.net> - 0.17-2
- Remove support for Fedora < 5
- rediff config patch

* Thu Nov  8 2007 David Nielsen <david@lovesunix.net> - 0.17-1
- Update to MonoDevelop Beta 2

* Wed Oct 17 2007 David Nielsen <david@lovesunix.net> - 0.16
- Update to MonoDevelop Beta 1

* Sat Aug 11 2007 David Nielsen <david@lovesunix.net> - 0.15
- bump to 0.15

* Thu Mar 08 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.13.1-1
- bugfixes to the source

* Fri Feb 23 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.13-1
- bump to new version

* Wed Dec 20 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-9
- disables version control
- requires gnome-sharp
- enable nemerle added
- enabled aspnet and aspnetedit (rawhide only - requires jscall-sharp)
- added R firefox > 1.99

* Wed Nov 01 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-7
- Added R gtk-sharp2-gapi

* Fri Oct 27 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-6
- fixed url
- added R apr-devel

* Wed Sep 27 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-5
- pkgconfig fix 

* Mon Sep 25 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-4
- added R mono-nunit

* Mon Sep 18 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-3
- rebuild to make use of the new boo

* Thu Sep 07 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-2
- minor spec file fixes

* Wed Sep 06 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.12-1
- Bump to new version
- Include the patches for all users
- Fixed so it uses ?fedora (silly me!)
- Added BR mono-nunit-devel (FC6)

* Mon Sep 04 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-21
- Revert 64 bit clean for FC-5 and still follow FC guidelines

* Sun Sep 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-20
- Added gtk sharp fix
- Added conditional so it builds for FC5

* Sun Aug 27 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-17
- 64 bit goodness restored

* Fri Aug 04 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-16
- fixed ownership problem in spec file
- added comment about the libdir hack

* Wed Aug 02 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-15
- removed R which, added R mono-nunit
- changed R bytefx-data-mysq to msql
- altered update-mime-info and added update-desktop-database
- added R pkgconfig to devel
- added comment as to why smp_flags are not used on the build

* Sat Jul 29 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-14
- Added additional Rs
- minor specfile tweaks

* Sun Jul 23 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-12
- fixed which problem
- fixes the libdir issue for 64 bit

* Sun Jul 09 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-11
- minor spec files changes to satisfy rpmlint
- added BR ikvm-devel

* Sun Jul 09 2006 John Mahowald  <jpmahowald@gmail.com> - 0.11-10
- libdir fixes
- BR mono-data-sqlite

* Sun Jul 09 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-9
- removed noarch
- added a couple of patches from the new nant package
- fixes for new mono guidelines

* Wed Jun 14 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-8
- Removed libdir hack
- Added BR pkgconfig
- Added R monodoc
- Altered configure line to satisfy the parts required

* Mon Jun 05 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-7
- Added additional fix for 64 bit systems

* Sun Jun 04 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-6
- Minor mod to the BR
- Fixed the desktop-file-install problem

* Sat Jun 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-5
- Removed duplicate desktop file

* Sat Jun 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-4
- Removed R filesystem
- Simplified mime-applications
- Added scriptlets to handle mime info
- Corrected handling of desktop icon
- Removed INSTALL file

* Sat Jun 03 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-3
- Added BR shared-mime-info
- Added R filesystem
- Made all of the bindir and datadir ownerships explicit

* Wed May 31 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-2
- Added devel
- Added fix for 64 bit systems

* Sun May 07 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.11-1
- bump to new version
- added exclude archs for x86_64 and ia64 due to build problems

* Wed Apr 26 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-8
- removed smp_flags
- added boo and ikvm support

* Sun Apr 23 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-7
- removed static usrlib
- added export macros to fix the x86_64 problem
- disabled boo

* Wed Apr 19 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-6
- spec file version correctly bumped
- small spec file fixed
- enable-boo and enable-java added to the %%configure line

* Mon Apr 18 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-5
- libdir now usr-lib irrespective of hardware built on

* Mon Apr 17 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-4
- Altered install script somewhat
- Changed the path for the monodevelop libdir to be FE compliant
- Fixed source and URL

* Sat Apr 15 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-3
- Add in boo and mono-debugger
- fixed a couple of minor spec file bugs
- fixed MonoDevelop.Core not being found in the addins

* Wed Apr 5 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-2
- Additional buildreqs and two typo fixed - thanks to Angel Marin again

* Wed Apr 5 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.10-1
- Bump to new version
- mods to spec file for new version

* Wed Apr 5 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.9-3
- minor tweaks
- fixed a couple of typos - thanks to Angel Marin for spotting them

* Wed Jan 25 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.9-2
- added deps for ikvm and bytefx-data-mysql
- removed language support for the moment

* Mon Jan 23 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.9-1
- Initial import


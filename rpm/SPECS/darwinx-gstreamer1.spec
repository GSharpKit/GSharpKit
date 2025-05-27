%define		api_version	1.0

Name:		darwinx-gstreamer1
Version: 	1.26.1
Release: 	1%{?dist}
Summary: 	GStreamer streaming media framework runtime

Group: 		Applications/Multimedia
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source0: 	http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.xz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	darwinx-filesystem-base >= 18
BuildRequires:	darwinx-gcc
BuildRequires:	darwinx-glib2
BuildRequires:	darwinx-gettext
BuildRequires:	darwinx-zlib
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	libtool

Requires:	darwinx-filesystem >= 18

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%prep
%setup -q -n gstreamer-%{version}

%build
%darwinx_meson \
	--default-library=shared \
	-Ddoc=disabled \
	-Dgst_debug=true \
	-Dlibunwind=disabled \
	-Dlibdw=disabled \
	-Ddbghelp=disabled \
	-Dintrospection=disabled \
	-Dnls=disabled \
	-Dbash-completion=disabled

%darwinx_meson_build

%install
rm -rf $RPM_BUILD_ROOT

%darwinx_meson_install

# Remove manpages.
rm -rf $RPM_BUILD_ROOT%{_darwinx_mandir}

# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc
rm -fr $RPM_BUILD_ROOT%{_darwinx_datadir}/gdb
rm -fr $RPM_BUILD_ROOT%{_darwinx_datadir}/gstreamer-%{api_version}/gdb

rm -f $RPM_BUILD_ROOT%{_darwinx_datadir}/cmake/FindGStreamer.cmake

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, wheel, -)
%{_darwinx_libdir}/libgstreamer-%{api_version}.0.dylib
%{_darwinx_libdir}/libgstbase-%{api_version}.0.dylib
%{_darwinx_libdir}/libgstcontroller-%{api_version}.0.dylib
%{_darwinx_libdir}/libgstnet-%{api_version}.0.dylib
%{_darwinx_libdir}/libgstcheck-%{api_version}.0.dylib

%{_darwinx_libdir}/libgstreamer-%{api_version}.dylib
%{_darwinx_libdir}/libgstbase-%{api_version}.dylib
%{_darwinx_libdir}/libgstcontroller-%{api_version}.dylib
%{_darwinx_libdir}/libgstnet-%{api_version}.dylib
%{_darwinx_libdir}/libgstcheck-%{api_version}.dylib

%dir %{_darwinx_libdir}/gstreamer-%{api_version}
%{_darwinx_libdir}/gstreamer-%{api_version}/libgstcoreelements.dylib
%{_darwinx_libdir}/gstreamer-%{api_version}/libgstcoretracers.dylib

%dir %{_darwinx_includedir}/gstreamer-%{api_version}
%dir %{_darwinx_includedir}/gstreamer-%{api_version}/gst
%{_darwinx_includedir}/gstreamer-%{api_version}/gst/*.h
%{_darwinx_includedir}/gstreamer-%{api_version}/gst/base
%{_darwinx_includedir}/gstreamer-%{api_version}/gst/check
%{_darwinx_includedir}/gstreamer-%{api_version}/gst/controller
%{_darwinx_includedir}/gstreamer-%{api_version}/gst/net

%{_darwinx_datadir}/aclocal/gst-element-check-%{api_version}.m4

%{_darwinx_libdir}/pkgconfig/gstreamer-%{api_version}.pc
%{_darwinx_libdir}/pkgconfig/gstreamer-base-%{api_version}.pc
%{_darwinx_libdir}/pkgconfig/gstreamer-controller-%{api_version}.pc
%{_darwinx_libdir}/pkgconfig/gstreamer-check-%{api_version}.pc
%{_darwinx_libdir}/pkgconfig/gstreamer-net-%{api_version}.pc

%{_darwinx_bindir}/gst-inspect-%{api_version}
%{_darwinx_bindir}/gst-launch-%{api_version}
%{_darwinx_bindir}/gst-typefind-%{api_version}
%{_darwinx_bindir}/gst-stats-%{api_version}
%{_darwinx_bindir}/gst-tester-%{api_version}
%{_darwinx_libexecdir}/gstreamer-%{api_version}/gst-plugin-scanner
%{_darwinx_libexecdir}/gstreamer-1.0/gst-ptp-helper
%{_darwinx_libexecdir}/gstreamer-1.0/gst-hotdoc-plugins-scanner
%{_darwinx_libexecdir}/gstreamer-1.0/gst-plugins-doc-cache-generator
%{_darwinx_libexecdir}/gstreamer-1.0/gst-completion-helper
   

%changelog
* Sun Jul  5 2009 - Levente Farkas <lfarkas@lfarkas.org> - 0.10.23-3
- more spec cleanup

* Fri Jun 19 2009 - Levente Farkas <lfarkas@lfarkas.org> - 0.10.23-2
- fix static libs

* Tue Jun 16 2009 - Levente Farkas <lfarkas@lfarkas.org> - 0.10.23-1
- add static sub-package

* Wed Mar 25 2009 - Levente Farkas <lfarkas@lfarkas.org> - 0.10.22-2
- add tools subpackage
- remove tools requires from

* Thu Mar 12 2009 - Zoltan Seress <gatesofdarkness@gmail.com> - 0.10.22-1
- Windows cross compilation

* Tue Jan 20 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.22-1
- Update to 0.10.22
- Remove upstreamed patches, update rpm provides patch

* Mon Jan 05 2009 - Bastien Nocera <bnocera@redhat.com> - 0.10.21-4
- Fix build with newer version of bison

* Thu Jan 01 2009 Rex Dieter <rdieter@fedoraprojet.org> - 0.10.21-3
- rebuild for pkgconfig deps (#478576)

* Tue Nov 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10.21-2
- fix gnome bz 555631 with patch from upstream cvs
- use system libtool to prevent rpaths

* Fri Oct 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.21-1
- Update to 0.10.21

* Sun Sep 14 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-6
- Hopefully fix RPM provides problem when the GStreamer plugin
  requires a library installed by the package itself

* Fri Sep 12 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-5
- Update rpm provides script and patch to:
  - filter out errors
  - only run gst-inspect on gstreamer plugins
  - print out protocol handlers provides correctly

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-4
- Add the rpm scripts install in /usr/lib/rpm, not under libdir on 64-bit

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-3
- Update filelist as well

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-2
- Update gstreamer provides work for the new RPM, see #438225

* Wed Jun 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.20-1
- Update to 0.10.20

* Mon Jun 02 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-3
- Package more documentation (#240656)

* Wed May 21 2008 - Tom "spot" Callaway <tcallawa@redhat.com> - 0.10.19-2
- fix license tag

* Fri Apr 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.19-1
- Update to 0.10.19

* Wed Mar 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.18-1
- Update to 0.10.18
- Add patch to gst-inspect to generate RPM provides
- Add RPM find-provides script

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17.2-1
- Update to 0.10.17.2 pre-release

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.17-2
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.17-1
- Update to 0.10.17

* Tue Jan 29 2008 - Bastien Nocera <bnocera@redhat.com> - 0.10.16-1
- Update to 0.10.16

* Fri Nov 16 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.15-1
- Update to 0.10.15

* Mon Oct  1 2007 Matthias Clasen <mclasen@redhat.com> - 0.10.14-4
- Add missing Requires (#312671)

* Tue Aug 14 2007 Matthias Clasen <mclasen@redhat.com> - 0.10.14-3
- Require check-devel (#251956)

* Sat Aug 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.14-1
- Update to 0.10.14

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-2
- Remove upstreamed docs patch

* Tue Jun 05 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.13-1
- Update to 0.10.13

* Thu Mar 08 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.12-1
- Update to 0.10.12

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.11-2
- Remove Requires on packages that BuildRequire us

* Tue Dec 12 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.11-1
- Update to 0.10.11

* Fri Oct 27 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.10-2
- Cleanups
- Attempt to fix multilib conflicts

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.10-1
- Update to 0.10.10

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.9-2
- Disable gtk-doc to fix multilib conflicts

* Thu Jul 20 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.9-1
- Update to new upstream version

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.8-4
- Re-add the gstreamer-plugins-good dependency

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.8-3.2
- Temporarily break the dependency cycle with gsteamer-plugins-good

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.10.8-3.1
- rebuild

* Wed Jun 28 2006 Karsten Hopp <karsten@redhat.de> 0.10.8-3
- remove RPATH pointing to RPM_BUILD_ROOT (#196870)

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.8-2
- Rebuild

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.8-1
- Update to 0.10.8

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 0.10.6-1
- Update to 0.10.6

* Tue Feb 14 2006 Rik van Riel <riel@redhat.com> - 0.10-3-3
- Obsolete gstreamer-plugins (#181296)

* Mon Feb 13 2006 Christopher Aillon <caillon@redhat.com> - 0.10.3-2
- Rebuild

* Fri Feb 10 2006 Christopher Aillon <caillon@redhat.com> - 0.10.3-1
- Update to 0.10.3

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.10.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.2-1
- Upgrade to 0.10.2

* Fri Jan 06 2006 John (J5) Palmieri <johnp@redhat.com> - 0.10.1-1
- New upstream version

* Fri Dec 16 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-1
- rebuilt for Fedora Core Development

* Wed Dec 14 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.2
- rebuilt against newer GLib and friends

* Mon Dec 05 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.10.0-0.gst.1
- new release

* Thu Dec 01 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.7-0.gst.1
- new release, with 0.10 api_version
- removed compprep and complete
- added plugins docs
- renamed libgstcorelements, libgstcoreindexers
- added libgstnet

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.5-0.gst.1
- new release

* Mon Oct 24 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.4-0.gst.1
- new release

* Mon Oct 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.3-0.gst.1
- new release

* Thu Sep 08 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.2-0.gst.1
- added libgstcheck
- new release

* Thu Jun 09 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.9.1-0.gst.1
- first development series release

* Tue May 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.10-0.gst.1
- new release
- up glib2 to 2.4 because disting on 2.4 builds marshalling code needing 2.4

* Mon May 02 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.9.2-0.gst.1
- new prerelease

* Tue Feb 08 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.9-0.gst.1
- new release
- switch back to the gst tag since fedora.us is gone

* Thu Feb 03 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.8.2-0.fdr.1
- new prerelease

* Thu Dec 23 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.8-0.fdr.1
- new upstream release

* Fri Dec 17 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.7.2-0.fdr.1
- new prerelease
- added fair gthread scheduler

* Wed Oct 06 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.7-0.fdr.1
- update for new GStreamer release

* Tue Oct 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.6-0.fdr.1
- update for new GStreamer release

* Sun Sep 26 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5.3-0.fdr.1
- update for new GStreamer prerelease

* Sun Sep 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5.2-0.fdr.1
- update for new GStreamer prerelease

* Mon Aug 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.5-0.fdr.1
- update for new GStreamer release

* Thu Aug 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.4.2-0.fdr.1
- update for new GStreamer prerelease
- set package name and origin

* Tue Jul 20 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.4-0.fdr.1
- update for new GStreamer release
- unbreak the postun script by not removing the cache dir

* Tue Jul 20 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3.3-0.fdr.1: update for new GStreamer prerelease

* Fri Jul 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3.2-0.fdr.1: update for new GStreamer prerelease

* Sat Jun 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.3-0.fdr.1: update for new GStreamer release

* Fri Jun 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.2-0.fdr.1: update for new GStreamer release

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.fdr.1: update for new GStreamer release

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- add entry schedulers, clean up scheduler file section

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.fdr.1: update for new GStreamer release, renamed base to gstreamer

* Tue Mar 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.6-0.fdr.1: updated for new GStreamer release, with maj/min set to 0.8

* Mon Mar 08 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.fdr.3: fix postun script

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.fdr.2: new release

* Wed Feb 11 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.4-0.fdr.1: synchronize with Matthias's package

* Sat Feb 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- make the package name gstreamer07 since this is an unstable release

* Wed Feb 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- put versioned tools inside base package, and put unversioned tools in tools

* Mon Dec 01 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- changed documentation buildrequires

* Sun Nov 09 2003 Christian Schaller <Uraeus@gnome.org>
- Fix spec to handle new bytestream library 

* Sun Aug 17 2003 Christian Schaller <uraeus@gnome.org>
- Remove docs build from RPM as the build is broken
- Fix stuff since more files are versioned now
- Remove wingo schedulers
- Remove putbits stuff

* Sun May 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- devhelp files are now generated by gtk-doc, changed accordingly

* Sun Mar 16 2003 Christian F.K. Schaller <Uraeus@gnome.org>
- Add gthread scheduler

* Sat Dec 07 2002 Thomas Vander Stichele <thomas at apestaart dot org>
- define api_version and use it everywhere
- full parallel installability

* Tue Nov 05 2002 Christian Schaller <Uraeus@linuxrising.org>
- Add optwingo scheduler
* Sat Oct 12 2002 Christian Schaller <Uraeus@linuxrising.org>
- Updated to work better with default RH8 rpm
- Added missing unspeced files
- Removed .a and .la files from buildroot

* Sat Sep 21 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added gst-md5sum

* Tue Sep 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adding flex to buildrequires

* Fri Sep 13 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Fixed the schedulers after the renaming
* Sun Sep 08 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added transfig to the BuildRequires:

* Sat Jun 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved header location

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added popt
- removed .la

* Fri Jun 07 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added release of gstreamer to req of gstreamer-devel
- changed location of API docs to be in gtk-doc like other gtk-doc stuff
- reordered SPEC file

* Mon Apr 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved html docs to gtk-doc standard directory

* Tue Mar 5 2002 Thomas Vander Stichele <thomas@apestaart.org>
- move version defines of glib2 and libxml2 to configure.ac
- add BuildRequires for these two libs

* Sun Mar 3 2002 Thomas Vander Stichele <thomas@apestaart.org>
- put html docs in canonical place, avoiding %%doc erasure
- added devhelp support, current install of it is hackish

* Sat Mar 2 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added documentation to build

* Mon Feb 11 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added libgstbasicscheduler
- renamed libgst to libgstreamer

* Fri Jan 04 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added configdir parameter as it seems the configdir gets weird otherwise

* Thu Jan 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- split off gstreamer-editor from core
- removed gstreamer-gnome-apps

* Sat Dec 29 2001 Rodney Dawes <dobey@free.fr>
- Cleaned up the spec file for the gstreamer core/plug-ins split
- Improve spec file

* Sat Dec 15 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split of more plugins from the core and put them into their own modules
- Includes colorspace, xfree and wav
- Improved package Require lines
- Added mp3encode (lame based) to the SPEC

* Wed Dec 12 2001 Christian Schaller <Uraeus@linuxrising.org>
- Thomas merged mpeg plugins into one
* Sat Dec 08 2001 Christian Schaller <Uraeus@linuxrising.org>
- More minor cleanups including some fixed descriptions from Andrew Mitchell

* Fri Dec 07 2001 Christian Schaller <Uraeus@linuxrising.org>
- Added logging to the make statement

* Wed Dec 05 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated in preparation for 0.3.0 release

* Fri Jun 29 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated for 0.2.1 release
- Split out the GUI packages into their own RPM
- added new plugins (FLAC, festival, quicktime etc.)

* Sat Jun 09 2001 Christian Schaller <Uraeus@linuxrising.org>
- Visualisation plugins bundled out togheter
- Moved files sections up close to their respective descriptions

* Sat Jun 02 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split the package into separate RPMS, 
  putting most plugins out by themselves.

* Fri Jun 01 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated with change suggestions from Dennis Bjorklund

* Tue Jan 09 2001 Erik Walthinsen <omega@cse.ogi.edu>
- updated to build -devel package as well

* Sun Jan 30 2000 Erik Walthinsen <omega@cse.ogi.edu>
- first draft of spec file


%define         debug_package %{nil}

Name:           mono-zeroconf
Version:        0.9.0
Release:        16%{?dist}
Summary:        Mono.Zeroconf networking library
Group:          Development/Languages
License:        MIT
URL:            http://banshee-project.org/files/mono-zeroconf
Source0:        %{name}-%{version}.tar.bz2
Patch0:		mono-zeroconf-0.9.0-profile.patch
BuildArch:      noarch
BuildRequires:  mono-devel monodoc-devel
Requires:       mono-core

Obsoletes:	mono-zeroconf-devel
Provides:	mono-zeroconf-devel

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-mdnsresponder --libdir=%{_prefix}/lib
#parallel build doesn't work
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig/

%files 
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog NEWS README
%{_bindir}/mzclient
%{_prefix}/lib/mono-zeroconf/
%{_prefix}/lib/mono/gac/Mono.Zeroconf
%{_prefix}/lib/mono/mono-zeroconf
%{_prefix}/lib/mono/gac/policy.*
%{_datadir}/pkgconfig/mono-zeroconf.pc
%{_prefix}/lib/monodoc/sources/mono-zeroconf*

%changelog
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Brent Baude <baude@us.ibm.com> - 0.9.0-11
- Changing ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Christian Krause <chkr@fedoraproject.org> - 0.9.0-6
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Fri Feb 25 2011 Dan Horák <dan[at]danny.cz> - 0.9.0-5
- updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 29 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.0-3
- ExcludeArch sparc64

* Thu Oct 22 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.0-2
- Make AvahiDbus the only provider for now

* Thu Oct 22 2009 Paul Lange <palango@gmx.de> - 0.9-1
- update to version 0.9
- move docs into devel package

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.6-10
- Rebuild for ppc64 packages due to obsolete of packageset last time.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.7.6-9
- Build arch ppc64.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.7.6-7
- add ppc

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-6
- Another fix for x86_64

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-5
- Remove patch file (use sed)
- Additional BRs and Rs

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-4
- remove ppc build for now

* Thu Dec 18 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-3
- rebuild (0.8.0 is buggy)

* Thu Aug 14 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-2
- bump to new version
- libdir clean now

* Tue Apr 07 2008 David Nielsen <gnomeuser@gmail.com> - 0.7.5-4
- Our CVS has odd bugs - pointless bump to make upgrade path work

* Mon Mar 31 2008 David Nielsen <gnomeuser@gmail.com> - 0.7.5-3
- Remove debuginfo

* Fri Feb 01 2008 David Nielsen <david@lovesunix.net> - 0.7.5-2
- Exclude ppc64
- Spec fixes

* Fri Feb 01 2008 David Nielsen <david@lovesunix.net> - 0.7.5-1
- bump to 0.7.5
- patch for libdir madness

* Fri Jan 04 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.3-2
- spec fixes

* Thu Dec 29 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.3-1
- Initial import for FE

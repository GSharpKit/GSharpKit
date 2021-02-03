%define libdir /lib

Name:		Mono.Addins
Version:	1.3.9
Release:	1%{?dist}
Summary:	Addins for mono
Group:		Development/Languages
License:	MIT
URL:		https://www.nuget.org/packages/Mono.Addins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	Mono.Addins-%{version}.tar.xz
Prefix:		/usr

BuildArch: 	noarch

Obsoletes:	mono-addins
Provides:	mono-addins

#BuildRequires:	nuget

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

%prep
%setup -q -n %{name}-%{version}
#nuget install %{name} -Version %{version}

cat > mono-addins.pc << \EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_prefix}%{libdir}

Name: %{name}
Description: %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/%{name}.dll
Cflags:
EOF

%build
nuget restore
cd Mono.Addins
msbuild /p:Configuration=Release Mono.Addins.csproj 

%install
%{__rm} -rf %{buildroot}

install -d -m 755 $RPM_BUILD_ROOT%{_prefix}%{libdir}
install -m 644 bin/netstandard2.0/%{name}.dll $RPM_BUILD_ROOT%{_prefix}%{libdir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pkgconfig/
install -m 644 mono-addins.pc $RPM_BUILD_ROOT%{_datadir}/pkgconfig/

%clean

%files
%defattr(-,root,root,-)
%{_prefix}%{libdir}/%{name}.dll
%{_datadir}/pkgconfig/mono-addins.pc

%changelog
* Wed Nov 14 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.3.8-1
- Updated to 1.3.8 from NuGet

* Fri Nov 17 2017 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.3.3-1
- Updated to 1.3.3

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

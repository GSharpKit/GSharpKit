Name:           darwinx-atk
Version:        2.28.1
Release:        1%{?dist}
Summary:        Cross compiled Atk library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://projects.gnome.org/accessibility/
Source:         http://ftp.gnome.org/pub/GNOME/sources/atk/2.26/atk-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 6
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-sdk
BuildRequires:  darwinx-gettext
BuildRequires:  darwinx-glib2

BuildRequires:  pkgconfig

%description
Cross compiled Atk library.


%package static
Summary:        Static version of the cross compiled Atk library
Requires:       %{name} = %{version}-%{release}

%description static
Static version of the cross compiled Atk library.


%prep
%setup -q -n atk-%{version}


%build
%{_darwinx_configure} --enable-static --enable-shared
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# Documentation duplicates what is in the native Fedora package.
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/gtk-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_darwinx_includedir}/atk-1.0
%{_darwinx_libdir}/libatk-1.0.0.dylib
%{_darwinx_libdir}/libatk-1.0.dylib
%{_darwinx_libdir}/libatk-1.0.la
%{_darwinx_libdir}/pkgconfig/atk.pc
%{_darwinx_datadir}/locale

%files -n darwinx-atk-static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libatk-1.0.a
  

%changelog
* Fri Nov  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Sun Jul 10 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.0-3
- Added support for darwinx

* Mon Oct  4 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0
- Renamed the package to cross-atk
- Obsoletes mingw32-atk and mingw32-atk-static
- Dropped upstreamed patch

* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.30.0-2
- Export the function atk_value_get_minimum_increment (required by GTK 2.21.7)

* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.30.0-1
- Update to 1.30.0

* Wed Dec  2 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.29.3-1
- Update to 1.29.3

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.27.90-1
- Update to 1.27.90
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0
- Use %%global instead of %%define

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 1.25.2-7
- Added -static subpackage
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.25.2-5
- Include license file.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.25.2-4
- Remove gtk-doc.
- Fix defattr line.
- Requires pkgconfig.
- Remove the atk*.def file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.25.2-1
- Rebase to latest Fedora native version 1.25.2.
- Use find_lang macro.
- Use smp_mflags.
- Fix URL.
- Fix Source URL.

* Wed Sep 24 2008 Daniel P. Berrange <berrange@redhat.com> - 1.24.0-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 1.24.0-1
- Update to 1.24.0 release

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 1.23.5-2
- Added dep on pkgconfig and glib2-devel (native)

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.23.5-1
- Initial RPM release

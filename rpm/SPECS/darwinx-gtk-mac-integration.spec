# Remove docs from Makefile.am and GTK_DOC* from configure
#aclocal --install --force -I /usr/darwinx/usr/share/aclocal/
#autoheader
#autoconf
#automake

Name:		darwinx-gtk-mac-integration
Version:	2.1.3
Release:	1%{?dist}
Summary:	Darwin API to integrate GTK+ OS X applications with the Mac desktop

License:	LGPLv2
Group:		Development/Libraries
URL:		http://sourceforge.net/projects/gtk-osx/files/
Source0:	gtk-mac-integration-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

BuildRequires:	darwinx-filesystem >= 13
BuildRequires:	darwinx-gtk3

Requires:       darwinx-gtk3

Obsoletes:	darwinx-ige-mac-integration

%description
API to integrate GTK+ OS X applications with the Mac desktop.


%package static
Summary:	Static version of the Darwin Ige-Mac-Integration library
Requires:	%{name} = %{version}-%{release}
Group:		Development/Libraries

%description static
Static version of the Darwin Gtk-Mac-Integration library.


%prep
%setup -q -n gtk-mac-integration-gtk-mac-integration-%{version}

sed -i '' 's!gtkdocize!#gtkdocize!g' autogen.sh
sed -i '' 's!GTK_DOC_CHECK!#GTK_DOC_CHECK!g' configure.ac
sed -i '' 's!    docs/Makefile!!g' configure.ac
sed -i '' 's!    docs/reference/Makefile!!g' configure.ac
sed -i '' 's!docs !!g' Makefile.am
sed -i '' 's!enable-gtk-doc!disable-gtk-doc!g' Makefile.am
sed -i '' 's!gtk-doc.make!!g' Makefile.am

%build
%{_darwinx_env}
sh autogen.sh --enable-static --enable-shared --enable-python=no --with-gtk3 --enable-introspection=no 
%{_darwinx_configure} --enable-static --enable-shared --enable-python=no --with-gtk3 --enable-introspection=no
%{_darwinx_make} %{?_smp_mflags} V=99


%install
rm -rf $RPM_BUILD_ROOT

%{_darwinx_makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%{_darwinx_includedir}/gtkmacintegration/
%{_darwinx_libdir}/libgtkmacintegration-gtk3.2.dylib
%{_darwinx_libdir}/libgtkmacintegration-gtk3.dylib
%{_darwinx_libdir}/libgtkmacintegration-gtk3.la
%{_darwinx_libdir}/pkgconfig/gtk-mac-integration-gtk3.pc
%{_darwinx_libdir}/pkgconfig/gtk-mac-integration.pc
%{_darwinx_datadir}/locale

%files static
%defattr(-,root,root,-)
%{_darwinx_libdir}/libgtkmacintegration-gtk3.a


%changelog
* Sat May  8 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.8.3-4.git20090608
- Rebuild for PPC fix in GLib
- Don't build for x86_64 (because pango doesn't support it yet)

* Sat Jul 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.8.3-3.git20090608
- Rebuild for universal binary support

* Sat Jun 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.8.3-2.git20090608
- Use macros instead of static paths

* Mon Jun  8 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.8.3-1.git20090608
- Initial release


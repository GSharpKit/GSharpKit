%{?ucrt_package_header}

%global bin_version 4.0.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           ucrt-gtk4
Version:        4.21.0
Release:        3%{?dist}
Summary:        MinGW Windows GTK+ library

License:        LGPLv2+
URL:            http://www.gtk.org
Source:         https://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  ucrt64-filesystem >= 107
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils

BuildRequires:  ucrt64-cairo
BuildRequires:  ucrt64-gdk-pixbuf
BuildRequires:  ucrt64-gettext
BuildRequires:  ucrt64-graphene
BuildRequires:  ucrt64-gstreamer1-plugins-bad-free >= 1.26.3-3
BuildRequires:  ucrt64-graphene
BuildRequires:  ucrt64-glib2
BuildRequires:  ucrt64-libepoxy
BuildRequires:  ucrt64-win-iconv
BuildRequires:  ucrt64-pango
BuildRequires:  ucrt64-pixman
BuildRequires:  ucrt64-zlib

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache


%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.


%package -n ucrt64-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       ucrt64-adwaita-icon-theme
# split out in a subpackage
Requires:       ucrt64-gtk4-update-icon-cache

%description -n ucrt64-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.


%package -n ucrt64-gtk4-update-icon-cache
Summary: Icon theme caching utility

%description -n ucrt64-gtk4-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.


%{?ucrt_debug_package}


%prep
%autosetup -p1 -n gtk-%{version}


%build
mkdir build_ucrt
pushd build_ucrt
%ucrt64_meson -Dintrospection=disabled -Dvulkan=disabled
ninja
popd


%install
pushd build_ucrt
DESTDIR=%{buildroot} ninja install
popd

# Remove desktop files and corresponding icons as they aren't useful for win32
rm -f %{buildroot}%{ucrt64_datadir}/applications/*.desktop
rm -rf %{buildroot}%{ucrt64_datadir}/icons/
rm -rf %{buildroot}%{ucrt64_datadir}/metainfo/

# Bash-completion files aren't interesting for ucrt
rm -rf %{buildroot}%{ucrt64_datadir}/bash-completion/



%files -n ucrt64-gtk4
%license COPYING
%{ucrt64_bindir}/gtk4-demo-application.exe
%{ucrt64_bindir}/gtk4-demo.exe
%{ucrt64_bindir}/gtk4-widget-factory.exe
%{ucrt64_bindir}/gtk4-builder-tool.exe
%{ucrt64_bindir}/gtk4-encode-symbolic-svg.exe
%{ucrt64_bindir}/gtk4-icon-editor.exe
%{ucrt64_bindir}/gtk4-query-settings.exe
%{ucrt64_bindir}/gtk4-node-editor.exe
%{ucrt64_bindir}/gtk4-path-tool.exe
%{ucrt64_bindir}/gtk4-print-editor.exe
%{ucrt64_bindir}/gtk4-rendernode-tool.exe
%{ucrt64_bindir}/gtk4-image-tool.exe
%{ucrt64_bindir}/libgtk-4-1.dll
%{ucrt64_includedir}/gtk-4.0/
%{ucrt64_libdir}/libgtk-4.dll.a
%{ucrt64_libdir}/pkgconfig/gtk4.pc
%{ucrt64_libdir}/pkgconfig/gtk4-win32.pc
%{ucrt64_datadir}/gettext/
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml
%{ucrt64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Inspector.gschema.xml
%{ucrt64_datadir}/gtk-4.0/
%{ucrt64_datadir}/locale/

%files -n ucrt64-gtk4-update-icon-cache
%license COPYING
%{ucrt64_bindir}/gtk4-update-icon-cache.exe


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Dec 08 2025 Sandro Mani <manisandro@gmail.com> - 4.21.0-2
- Rebuild (libtiff)

* Tue Sep 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.21.0-1
- new version

* Wed Jul 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.19.2-1
- new version

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.14.4-1
- new version

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.11.4-1
- new version

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.8.2-1
- Bump to 4.8.2 release

* Thu Aug 18 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.7.2-1
- initial packaging

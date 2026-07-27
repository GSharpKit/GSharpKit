%{?mingw_package_header}

%define debug_package %{nil}

%global mingw_build_win32 0
%global mingw_build_win64 1

%global glib_version 2.48
%global gtk_version 3.22

Name:           mingw-gtksourceview4
Version:        4.8.4
Release:        11%{?dist}
Summary:        Source code editing widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/4.8/gtksourceview-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gtksourceview/-/commit/2538a4daf1aba9c42c3dcfe2ff394874ac157c67
# https://gitlab.gnome.org/GNOME/gtksourceview/-/issues/278
# Fix some regexes to work with pcre2
Patch0:         0001-language-specs-use-N-U-escape-sequences.patch

BuildArch:      noarch

BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  meson

%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version 4 of GtkSourceView.

%package -n mingw64-gtksourceview4
Summary:        Source code editing widget

%description -n mingw64-gtksourceview4
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version 4 of GtkSourceView.

%prep
%autosetup -n gtksourceview-%{version} -p1

%build
%mingw_meson -Dgtk_doc=false -Dinstall_tests=false -Dgir=false -Dglade_catalog=false -Dvapi=false
%mingw_ninja


%install
%mingw_ninja_install

rm -f %{buildroot}%{mingw64_libdir}/libgtksourceview-4.dll.a


%files -n mingw64-gtksourceview4
%license COPYING
%{mingw64_bindir}/libgtksourceview-4-0.dll
%{mingw64_datadir}/gtksourceview-4/
%{mingw64_libdir}/pkgconfig/*.pc
%dir %{mingw64_includedir}/gtksourceview-4
%{mingw64_includedir}/gtksourceview-4/*
%{mingw64_datadir}/locale/*

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.8.4-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 31 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 4.8.4-4
- Disable glade catalog in RHEL builds

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 David King <amigadave@amigadave.com> - 4.8.4-1
- Update to 4.8.4

* Tue Jul 26 2022 Adam Williamson <awilliam@redhat.com> - 4.8.3-3
- Backport fix from main branch for regexes with pcre2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 4.8.3-1
- Update to 4.8.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 4.8.2-1
- Update to 4.8.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Kalev Lember <klember@redhat.com> - 4.8.1-1
- Update to 4.8.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 4.7.90-1
- Update to 4.7.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 4.6.1-1
- Update to 4.6.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 4.6.0-1
- Update to 4.6.0

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 4.5.91-1
- Update to 4.5.91

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 4.4.0-1
- Update to 4.4.0

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 4.3.92-1
- Update to 4.3.92

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Phil Wyett <philwyett@kathenas.org> - 4.3.1-1
- Update to 4.3.1
- Convert to meson

* Sat Mar 16 2019 Kalev Lember <klember@redhat.com> - 4.2.0-1
- Update to 4.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 4.0.3-2
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Pete Walter <pwalter@fedoraproject.org> - 4.0.3-1
- Initial packaging of GtkSourceView 4

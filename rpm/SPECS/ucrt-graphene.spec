%{?ucrt_package_header}

%global desc \
Graphene provides a small set of mathematical types needed to implement graphic \
libraries that deal with 2D and 3D transformations and projections. \
\
This package contains the MinGW Windows cross compiled graphene library.

Name:           ucrt-graphene
Version:        1.10.8
Release:        9%{?dist}
Summary:        Thin layer of types for graphic libraries

License:        MIT
URL:            https://github.com/ebassi/graphene
Source0:        %{url}/releases/download/%{version}/graphene-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson >= 0.50.1

BuildRequires:  ucrt64-filesystem >= 107
BuildRequires:  ucrt64-gcc-c++

BuildRequires:  ucrt64-glib2


%description %{desc}

%package -n ucrt64-graphene
Summary:        MinGW Windows graphene library

%description -n ucrt64-graphene %{desc}

%{?ucrt_debug_package}


%prep
%autosetup -p1 -n graphene-%{version}


%build
mkdir build_ucrt
pushd build_ucrt
%ucrt64_meson -Dintrospection=disabled
ninja
popd


%install
pushd build_ucrt
DESTDIR=%{buildroot} ninja install
popd

rm -rf %{buildroot}%{ucrt64_datadir}/installed-tests/
rm -rf %{buildroot}%{ucrt64_libexecdir}/installed-tests/


%files -n ucrt64-graphene
%license LICENSE.txt
%doc README.md
%{ucrt64_libdir}/libgraphene-1.0.dll.a
%{ucrt64_includedir}/graphene-1.0/
%dir %{ucrt64_libdir}/graphene-1.0
%{ucrt64_libdir}/graphene-1.0/include/
%{ucrt64_bindir}/libgraphene-1.0-0.dll
%{ucrt64_libdir}/pkgconfig/graphene-1.0.pc
%{ucrt64_libdir}/pkgconfig/graphene-gobject-1.0.pc


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Mar 26 2025 Tim Landscheidt <tim@tim-landscheidt.de> - 1.10.8-7
- Fix description for ucrt64-graphene

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.10.8-1
- Update to 1.10.8
  https://bugzilla.redhat.com/show_bug.cgi?id=2065973

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.10.6-3
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Marc-André Lureau <marcandre.lureau@redhat.com>
- Initial package. rhbz#2036610

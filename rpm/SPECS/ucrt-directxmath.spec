%{?ucrt_package_header}
# Header-only package
%global debug_package %{nil}

%global pkgname directxmath
%global tag apr2025

Name:          ucrt-%{pkgname}
Version:       3.20
Release:       6%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       MIT
URL:           https://github.com/microsoft/DirectXMath
Source0:       https://github.com/microsoft/DirectXMath/archive/%{tag}/%{pkgname}-%{version}.tar.gz
# Fix cmake module install dir
# Adapt header install dir
Patch0:        directxmath_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n ucrt64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n ucrt64-%{pkgname}
%{summary}.


%prep
%autosetup -p1 -n DirectXMath-%{tag}


%build
%ucrt64_cmake
%ucrt64_make


%install
%ucrt64_make install DESTDIR=%{buildroot}


%files -n ucrt64-%{pkgname}
%license LICENSE
%{ucrt64_includedir}/directxmath/
%{ucrt64_libdir}/pkgconfig/DirectXMath.pc
%{ucrt64_datadir}/cmake/directxmath/


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Jan 05 2026 Sandro Mani <manisandro@gmail.com> - 3.20-5
- Fix includedir in pc file

* Sat Dec 27 2025 Sandro Mani <manisandro@gmail.com> - 3.20-4
- Update to apr2025 release

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 17 2024 Sandro Mani <manisandro@gmail.com> - 3.20-1
- Update to 3.20

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 3.19-1
- Initial package
